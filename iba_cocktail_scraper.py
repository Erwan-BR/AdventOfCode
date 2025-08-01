"""
IBA Cocktail Scraper
====================

A comprehensive system for scraping cocktail recipes from the International Bartenders Association (IBA) website.
Includes functions for parsing ingredient quantities and finding cocktails by ingredients.

Features:
- Scrapes all official IBA cocktails from iba-world.com
- Parses ingredient quantities using robust regex patterns
- Provides helper functions for cocktail discovery
- Handles various measurement formats (ml, cl, oz, dashes, drops, etc.)
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Optional, Tuple, Union
import json
from dataclasses import dataclass, asdict
from fractions import Fraction


@dataclass
class IngredientQuantity:
    """Structured representation of ingredient quantity"""
    amount: float
    unit: str
    original_text: str
    is_range: bool = False
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None


@dataclass
class Ingredient:
    """Structured representation of a cocktail ingredient"""
    name: str
    quantity: IngredientQuantity
    category: str = "unknown"  # spirit, liqueur, mixer, garnish, etc.


@dataclass
class Cocktail:
    """Structured representation of a cocktail recipe"""
    name: str
    category: str  # The Unforgettables, Contemporary Classics, New Era
    ingredients: List[Ingredient]
    method: str
    garnish: str
    glass_type: str = ""
    views: int = 0
    url: str = ""


class QuantityParser:
    """
    Advanced quantity parser using robust regex patterns to handle various measurement formats
    """
    
    def __init__(self):
        # Comprehensive regex patterns for different quantity formats
        self.patterns = {
            # Standard measurements with units (30 ml, 1.5 oz, 2 cl)
            'standard': re.compile(r'(\d+(?:\.\d+)?)\s*(ml|cl|oz|l|dl)', re.IGNORECASE),
            
            # Fractions (1/2 oz, 3/4 cl, 1 1/2 ml)
            'fraction': re.compile(r'(\d+)?\s*(\d+)/(\d+)\s*(ml|cl|oz|l|dl)', re.IGNORECASE),
            
            # Mixed fractions (1 1/2 oz)
            'mixed_fraction': re.compile(r'(\d+)\s+(\d+)/(\d+)\s*(ml|cl|oz|l|dl)', re.IGNORECASE),
            
            # Ranges (1-2 ml, 15-30 ml)
            'range': re.compile(r'(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*(ml|cl|oz|l|dl)', re.IGNORECASE),
            
            # Dashes and drops
            'dashes': re.compile(r'(\d+(?:\.\d+)?)\s*(dash|dashes|drop|drops|splash|splashes)', re.IGNORECASE),
            
            # Special measurements (pinch, handful, etc.)
            'special': re.compile(r'(\d+(?:\.\d+)?)?\s*(pinch|pinches|handful|handfuls|slice|slices|piece|pieces|sprig|sprigs|leaf|leaves)', re.IGNORECASE),
            
            # Just numbers (assume ml if no unit specified)
            'number_only': re.compile(r'^(\d+(?:\.\d+)?)$'),
            
            # Descriptive quantities (to taste, as needed, etc.)
            'descriptive': re.compile(r'(to taste|as needed|garnish|float|top up|fill)', re.IGNORECASE),
        }
        
        # Unit conversion to ml (base unit)
        self.unit_conversions = {
            'ml': 1.0,
            'cl': 10.0,
            'dl': 100.0,
            'l': 1000.0,
            'oz': 29.5735,  # US fluid ounce
            'dash': 0.625,  # Standard dash measurement
            'drop': 0.05,   # Standard drop measurement
            'splash': 5.0,  # Approximate splash
            'pinch': 0.3,   # Approximate pinch
            'slice': 1.0,   # Nominal value for counting
            'piece': 1.0,   # Nominal value for counting
            'sprig': 1.0,   # Nominal value for counting
            'leaf': 1.0,    # Nominal value for counting
        }

    def parse_quantity(self, quantity_text: str) -> IngredientQuantity:
        """
        Parse ingredient quantity text into structured format
        
        Args:
            quantity_text: Raw quantity text (e.g., "30 ml", "1-2 dashes", "1/2 oz")
            
        Returns:
            IngredientQuantity object with parsed data
        """
        if not quantity_text:
            return IngredientQuantity(0, "unknown", quantity_text)
        
        text = quantity_text.strip()
        
        # Try range pattern first
        range_match = self.patterns['range'].search(text)
        if range_match:
            min_amt, max_amt, unit = range_match.groups()
            return IngredientQuantity(
                amount=float(max_amt),
                unit=unit.lower(),
                original_text=text,
                is_range=True,
                min_amount=float(min_amt),
                max_amount=float(max_amt)
            )
        
        # Try mixed fraction (1 1/2 oz)
        mixed_fraction_match = self.patterns['mixed_fraction'].search(text)
        if mixed_fraction_match:
            whole, numerator, denominator, unit = mixed_fraction_match.groups()
            fraction_value = float(whole) + float(numerator) / float(denominator)
            return IngredientQuantity(fraction_value, unit.lower(), text)
        
        # Try simple fraction (1/2 oz)
        fraction_match = self.patterns['fraction'].search(text)
        if fraction_match:
            whole, numerator, denominator, unit = fraction_match.groups()
            if whole:
                fraction_value = float(whole) + float(numerator) / float(denominator)
            else:
                fraction_value = float(numerator) / float(denominator)
            return IngredientQuantity(fraction_value, unit.lower(), text)
        
        # Try standard measurement
        standard_match = self.patterns['standard'].search(text)
        if standard_match:
            amount, unit = standard_match.groups()
            return IngredientQuantity(float(amount), unit.lower(), text)
        
        # Try dashes/drops
        dashes_match = self.patterns['dashes'].search(text)
        if dashes_match:
            amount, unit = dashes_match.groups()
            amount = float(amount) if amount else 1.0
            return IngredientQuantity(amount, unit.lower().rstrip('s'), text)
        
        # Try special measurements
        special_match = self.patterns['special'].search(text)
        if special_match:
            amount, unit = special_match.groups()
            amount = float(amount) if amount else 1.0
            return IngredientQuantity(amount, unit.lower().rstrip('s'), text)
        
        # Try number only (assume ml)
        number_match = self.patterns['number_only'].search(text)
        if number_match:
            amount = number_match.group(1)
            return IngredientQuantity(float(amount), "ml", text)
        
        # Try descriptive
        descriptive_match = self.patterns['descriptive'].search(text)
        if descriptive_match:
            return IngredientQuantity(0, descriptive_match.group(1).lower(), text)
        
        # If nothing matches, return as-is
        return IngredientQuantity(0, "unknown", text)

    def convert_to_ml(self, quantity: IngredientQuantity) -> float:
        """Convert quantity to milliliters"""
        if quantity.unit in self.unit_conversions:
            return quantity.amount * self.unit_conversions[quantity.unit]
        return quantity.amount  # Return as-is if unknown unit

    def normalize_quantities(self, ingredients: List[Ingredient]) -> List[Ingredient]:
        """Normalize all ingredient quantities to ml for comparison"""
        for ingredient in ingredients:
            ml_amount = self.convert_to_ml(ingredient.quantity)
            ingredient.quantity.amount = ml_amount
            ingredient.quantity.unit = "ml"
        return ingredients


class IBACocktailScraper:
    """
    Main scraper class for extracting cocktail data from the IBA website
    """
    
    def __init__(self, delay: float = 1.0):
        self.base_url = "https://iba-world.com"
        self.delay = delay  # Delay between requests to be respectful
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.quantity_parser = QuantityParser()
        
    def get_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a web page"""
        try:
            time.sleep(self.delay)  # Be respectful to the server
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def get_all_cocktail_urls(self) -> Dict[str, List[str]]:
        """Get URLs for all cocktails organized by category"""
        categories = {
            'The Unforgettables': f"{self.base_url}/cocktails/the-unforgettables/",
            'Contemporary Classics': f"{self.base_url}/cocktails/contemporary-classics/",
            'New Era': f"{self.base_url}/cocktails/new-era/"
        }
        
        all_urls = {}
        
        for category, category_url in categories.items():
            print(f"Fetching {category} cocktails...")
            soup = self.get_page(category_url)
            if not soup:
                continue
                
            cocktail_urls = []
            
            # Find all cocktail links on the category page
            cocktail_links = soup.find_all('a', href=True)
            for link in cocktail_links:
                href = link.get('href')
                if href and ('cocktail' in href.lower() or any(word in href.lower() for word in ['alexander', 'americano', 'aviation', 'bellini'])):
                    full_url = urljoin(self.base_url, href)
                    if full_url not in cocktail_urls:
                        cocktail_urls.append(full_url)
            
            # Also try the main cocktails page approach
            main_cocktails_url = f"{self.base_url}/cocktails/all-cocktails/"
            soup = self.get_page(main_cocktails_url)
            if soup:
                # Look for cocktail names and construct URLs
                cocktail_elements = soup.find_all(text=re.compile(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'))
                for element in cocktail_elements:
                    text = element.strip()
                    if len(text) > 2 and text[0].isupper():
                        # Try to construct URL
                        cocktail_slug = text.lower().replace(' ', '-').replace("'", "").replace("#", "")
                        potential_url = f"{self.base_url}/{cocktail_slug}/"
                        if potential_url not in cocktail_urls:
                            cocktail_urls.append(potential_url)
            
            all_urls[category] = cocktail_urls
            print(f"Found {len(cocktail_urls)} potential URLs for {category}")
        
        return all_urls

    def parse_cocktail_page(self, url: str, category: str) -> Optional[Cocktail]:
        """Parse individual cocktail page"""
        soup = self.get_page(url)
        if not soup:
            return None
        
        try:
            # Extract cocktail name
            name_element = soup.find('h1')
            if not name_element:
                return None
            name = name_element.get_text().strip()
            
            # Extract views if available
            views = 0
            views_text = soup.find(text=re.compile(r'\d+(?:,\d+)*(?:\.\d+)?[KM]?\s*views'))
            if views_text:
                views_match = re.search(r'(\d+(?:,\d+)*(?:\.\d+)?)([KM]?)', views_text)
                if views_match:
                    num, multiplier = views_match.groups()
                    views = float(num.replace(',', ''))
                    if multiplier == 'K':
                        views *= 1000
                    elif multiplier == 'M':
                        views *= 1000000
                    views = int(views)
            
            # Extract ingredients
            ingredients = []
            ingredients_section = soup.find('h4', text='Ingredients')
            if ingredients_section:
                ingredients_list = ingredients_section.find_next('ul')
                if ingredients_list:
                    for li in ingredients_list.find_all('li'):
                        ingredient_text = li.get_text().strip()
                        if ingredient_text:
                            # Parse ingredient text (e.g., "30 ml Cognac")
                            parts = ingredient_text.split(' ', 2)
                            if len(parts) >= 2:
                                # Try to identify quantity and name
                                quantity_text = ' '.join(parts[:2]) if not parts[0].replace('.', '').isdigit() else parts[0]
                                name_text = ' '.join(parts[1:]) if not parts[0].replace('.', '').isdigit() else ' '.join(parts[1:])
                                
                                # If the first part is not a number, the whole thing might be the name
                                if not re.search(r'\d', parts[0]):
                                    quantity_text = ""
                                    name_text = ingredient_text
                                
                                quantity = self.quantity_parser.parse_quantity(quantity_text)
                                ingredient = Ingredient(name=name_text.strip(), quantity=quantity)
                                ingredients.append(ingredient)
            
            # Extract method
            method = ""
            method_section = soup.find('h4', text='Method')
            if method_section:
                method_content = method_section.find_next(['p', 'div'])
                if method_content:
                    method = method_content.get_text().strip()
            
            # Extract garnish
            garnish = ""
            garnish_section = soup.find('h4', text='Garnish')
            if garnish_section:
                garnish_content = garnish_section.find_next(['p', 'div'])
                if garnish_content:
                    garnish = garnish_content.get_text().strip()
            
            return Cocktail(
                name=name,
                category=category,
                ingredients=ingredients,
                method=method,
                garnish=garnish,
                views=views,
                url=url
            )
            
        except Exception as e:
            print(f"Error parsing cocktail page {url}: {e}")
            return None

    def scrape_all_cocktails(self) -> Dict[str, Cocktail]:
        """
        Scrape all cocktails from the IBA website
        
        Returns:
            Dictionary mapping cocktail names to Cocktail objects
        """
        print("Starting IBA cocktail scraping...")
        
        # Get all cocktail URLs
        category_urls = self.get_all_cocktail_urls()
        
        all_cocktails = {}
        
        # Well-known cocktail names to try if automatic discovery fails
        known_cocktails = [
            'alexander', 'americano', 'angel-face', 'aviation', 'bees-knees',
            'bellini', 'between-the-sheets', 'black-russian', 'bloody-mary',
            'boulevardier', 'bramble', 'brandy-crusta', 'caipirinha',
            'canchanchara', 'cardinale', 'casino', 'champagne-cocktail',
            'chartreuse-swizzle', 'clover-club', 'corpse-reviver-2',
            'cosmopolitan', 'cuba-libre', 'daiquiri', 'dark-n-stormy',
            'dry-martini', 'espresso-martini', 'french-75', 'french-martini',
            'gimlet', 'gin-fizz', 'grasshopper', 'harvey-wallbanger',
            'hemingway-special', 'horse-neck', 'hot-toddy', 'irish-coffee',
            'john-collins', 'kir', 'long-island-iced-tea', 'mai-tai',
            'manhattan', 'margarita', 'martinez', 'mary-pickford',
            'mimosa', 'mint-julep', 'mojito', 'moscow-mule', 'negroni',
            'new-york-sour', 'old-fashioned', 'paloma', 'paper-plane',
            'penicillin', 'pina-colada', 'pisco-sour', 'planters-punch',
            'porto-flip', 'porn-star-martini', 'ramos-gin-fizz', 'rusty-nail',
            'sazerac', 'sea-breeze', 'sex-on-the-beach', 'sidecar',
            'singapore-sling', 'southside', 'spritz', 'stinger',
            'tequila-sunrise', 'tommy-margarita', 'trinidad-sour',
            'unforgiven', 'vesper', 'whiskey-sour', 'white-lady',
            'yellow-bird', 'zombie'
        ]
        
        # Try known cocktails first
        for cocktail_name in known_cocktails:
            url = f"{self.base_url}/{cocktail_name}/"
            print(f"Trying to scrape: {cocktail_name}")
            
            # Determine category (simplified logic)
            category = "Unknown"
            if cocktail_name in ['alexander', 'americano', 'angel-face', 'aviation']:
                category = "The Unforgettables"
            elif cocktail_name in ['bellini', 'black-russian', 'bloody-mary']:
                category = "Contemporary Classics"
            elif cocktail_name in ['bees-knees', 'bramble', 'chartreuse-swizzle']:
                category = "New Era"
            
            cocktail = self.parse_cocktail_page(url, category)
            if cocktail and cocktail.ingredients:  # Only add if we got ingredients
                all_cocktails[cocktail.name] = cocktail
                print(f"✓ Successfully scraped: {cocktail.name}")
            else:
                print(f"✗ Failed to scrape: {cocktail_name}")
        
        # Try URLs from category pages
        for category, urls in category_urls.items():
            for url in urls[:10]:  # Limit to avoid too many requests
                cocktail = self.parse_cocktail_page(url, category)
                if cocktail and cocktail.ingredients and cocktail.name not in all_cocktails:
                    all_cocktails[cocktail.name] = cocktail
                    print(f"✓ Successfully scraped: {cocktail.name} from category page")
        
        print(f"\nScraping complete! Found {len(all_cocktails)} cocktails.")
        return all_cocktails


class CocktailHelper:
    """
    Helper functions for working with cocktail data
    """
    
    def __init__(self, cocktails: Dict[str, Cocktail]):
        self.cocktails = cocktails
        self.quantity_parser = QuantityParser()
    
    def find_cocktails_by_ingredient(self, ingredient_name: str, exact_match: bool = False) -> List[Cocktail]:
        """
        Find all cocktails that contain a specific ingredient
        
        Args:
            ingredient_name: Name of ingredient to search for
            exact_match: If True, requires exact match; if False, allows partial matches
            
        Returns:
            List of Cocktail objects containing the ingredient
        """
        matching_cocktails = []
        search_term = ingredient_name.lower().strip()
        
        for cocktail in self.cocktails.values():
            for ingredient in cocktail.ingredients:
                ingredient_lower = ingredient.name.lower()
                
                if exact_match:
                    if search_term == ingredient_lower:
                        matching_cocktails.append(cocktail)
                        break
                else:
                    if search_term in ingredient_lower or ingredient_lower in search_term:
                        matching_cocktails.append(cocktail)
                        break
        
        return matching_cocktails
    
    def get_all_ingredients(self) -> Dict[str, int]:
        """
        Get all unique ingredients with their usage count
        
        Returns:
            Dictionary mapping ingredient names to usage count
        """
        ingredient_counts = {}
        
        for cocktail in self.cocktails.values():
            for ingredient in cocktail.ingredients:
                name = ingredient.name.strip()
                ingredient_counts[name] = ingredient_counts.get(name, 0) + 1
        
        return dict(sorted(ingredient_counts.items(), key=lambda x: x[1], reverse=True))
    
    def find_cocktails_by_multiple_ingredients(self, ingredients: List[str], require_all: bool = True) -> List[Cocktail]:
        """
        Find cocktails that contain multiple specific ingredients
        
        Args:
            ingredients: List of ingredient names to search for
            require_all: If True, cocktail must contain ALL ingredients; if False, ANY ingredient
            
        Returns:
            List of matching Cocktail objects
        """
        matching_cocktails = []
        search_terms = [ing.lower().strip() for ing in ingredients]
        
        for cocktail in self.cocktails.values():
            cocktail_ingredients = [ing.name.lower() for ing in cocktail.ingredients]
            
            if require_all:
                # Check if all search terms are found
                matches = sum(1 for term in search_terms 
                            if any(term in ci or ci in term for ci in cocktail_ingredients))
                if matches == len(search_terms):
                    matching_cocktails.append(cocktail)
            else:
                # Check if any search term is found
                if any(any(term in ci or ci in term for ci in cocktail_ingredients) 
                      for term in search_terms):
                    matching_cocktails.append(cocktail)
        
        return matching_cocktails
    
    def get_cocktails_by_category(self, category: str) -> List[Cocktail]:
        """Get all cocktails from a specific category"""
        return [cocktail for cocktail in self.cocktails.values() 
                if cocktail.category.lower() == category.lower()]
    
    def get_cocktail_stats(self) -> Dict[str, any]:
        """Get statistical information about the cocktail collection"""
        total_cocktails = len(self.cocktails)
        categories = {}
        total_ingredients = 0
        
        for cocktail in self.cocktails.values():
            categories[cocktail.category] = categories.get(cocktail.category, 0) + 1
            total_ingredients += len(cocktail.ingredients)
        
        unique_ingredients = len(self.get_all_ingredients())
        avg_ingredients = total_ingredients / total_cocktails if total_cocktails > 0 else 0
        
        return {
            'total_cocktails': total_cocktails,
            'categories': categories,
            'unique_ingredients': unique_ingredients,
            'average_ingredients_per_cocktail': round(avg_ingredients, 2),
            'most_popular_ingredients': dict(list(self.get_all_ingredients().items())[:10])
        }


def save_cocktails_to_json(cocktails: Dict[str, Cocktail], filename: str = "iba_cocktails.json"):
    """Save cocktail data to JSON file"""
    # Convert cocktails to dictionary format
    cocktails_dict = {}
    for name, cocktail in cocktails.items():
        cocktails_dict[name] = asdict(cocktail)
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(cocktails_dict, f, indent=2, ensure_ascii=False)
    print(f"Cocktails saved to {filename}")


def load_cocktails_from_json(filename: str = "iba_cocktails.json") -> Dict[str, Cocktail]:
    """Load cocktail data from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cocktails = {}
    for name, cocktail_data in data.items():
        # Reconstruct Ingredient objects
        ingredients = []
        for ing_data in cocktail_data['ingredients']:
            quantity = IngredientQuantity(**ing_data['quantity'])
            ingredient = Ingredient(
                name=ing_data['name'],
                quantity=quantity,
                category=ing_data.get('category', 'unknown')
            )
            ingredients.append(ingredient)
        
        # Reconstruct Cocktail object
        cocktail = Cocktail(
            name=cocktail_data['name'],
            category=cocktail_data['category'],
            ingredients=ingredients,
            method=cocktail_data['method'],
            garnish=cocktail_data['garnish'],
            glass_type=cocktail_data.get('glass_type', ''),
            views=cocktail_data.get('views', 0),
            url=cocktail_data.get('url', '')
        )
        cocktails[name] = cocktail
    
    return cocktails


# Example usage and testing
if __name__ == "__main__":
    # Initialize the scraper
    scraper = IBACocktailScraper(delay=1.5)
    
    # Test quantity parser
    print("Testing Quantity Parser:")
    parser = QuantityParser()
    test_quantities = [
        "30 ml",
        "1.5 oz",
        "1/2 oz",
        "1 1/2 cl",
        "2-3 dashes",
        "15-20 ml",
        "to taste",
        "2 slices",
        "1 sprig"
    ]
    
    for qty in test_quantities:
        parsed = parser.parse_quantity(qty)
        print(f"  '{qty}' -> Amount: {parsed.amount}, Unit: {parsed.unit}, Range: {parsed.is_range}")
    
    print("\n" + "="*50)
    print("Starting cocktail scraping...")
    
    # Scrape all cocktails
    cocktails = scraper.scrape_all_cocktails()
    
    if cocktails:
        # Save to JSON
        save_cocktails_to_json(cocktails)
        
        # Initialize helper
        helper = CocktailHelper(cocktails)
        
        # Print statistics
        print("\nCocktail Database Statistics:")
        stats = helper.get_cocktail_stats()
        for key, value in stats.items():
            print(f"  {key}: {value}")
        
        # Test ingredient search
        print(f"\nCocktails with gin:")
        gin_cocktails = helper.find_cocktails_by_ingredient("gin")
        for cocktail in gin_cocktails[:5]:  # Show first 5
            print(f"  - {cocktail.name}")
        
        print(f"\nCocktails with vodka:")
        vodka_cocktails = helper.find_cocktails_by_ingredient("vodka")
        for cocktail in vodka_cocktails[:5]:  # Show first 5
            print(f"  - {cocktail.name}")
        
        # Example cocktail details
        if cocktails:
            example_cocktail = list(cocktails.values())[0]
            print(f"\nExample cocktail - {example_cocktail.name}:")
            print(f"  Category: {example_cocktail.category}")
            print(f"  Ingredients:")
            for ing in example_cocktail.ingredients:
                print(f"    - {ing.quantity.amount} {ing.quantity.unit} {ing.name}")
            print(f"  Method: {example_cocktail.method}")
            print(f"  Garnish: {example_cocktail.garnish}")
    else:
        print("No cocktails were successfully scraped.")