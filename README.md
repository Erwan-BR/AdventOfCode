# IBA Cocktail Scraper 🍸

A comprehensive Python system for scraping, parsing, and analyzing cocktail recipes from the International Bartenders Association (IBA) official website.

## Features

- **🌐 Web Scraping**: Extracts all official IBA cocktails from iba-world.com
- **🔍 Smart Parsing**: Advanced regex-based quantity parser for ingredient measurements
- **📊 Data Analysis**: Helper functions for cocktail discovery and analysis
- **💾 Data Persistence**: Save/load cocktail data to/from JSON
- **🍹 Recipe Search**: Find cocktails by ingredients, categories, or multiple criteria
- **📏 Unit Conversion**: Handles various measurement units (ml, cl, oz, dashes, etc.)

## Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from iba_cocktail_scraper import IBACocktailScraper, CocktailHelper

# Initialize scraper
scraper = IBACocktailScraper(delay=1.5)

# Scrape all cocktails
cocktails = scraper.scrape_all_cocktails()

# Initialize helper for searching
helper = CocktailHelper(cocktails)

# Find cocktails with gin
gin_cocktails = helper.find_cocktails_by_ingredient("gin")
print(f"Found {len(gin_cocktails)} cocktails with gin")
```

### Quantity Parsing

```python
from iba_cocktail_scraper import QuantityParser

parser = QuantityParser()

# Parse various quantity formats
quantities = ["30 ml", "1.5 oz", "1/2 oz", "2-3 dashes", "to taste"]

for qty in quantities:
    parsed = parser.parse_quantity(qty)
    print(f"{qty} → {parsed.amount} {parsed.unit}")
```

### Finding Cocktails by Ingredients

```python
# Find cocktails with specific ingredient
vodka_cocktails = helper.find_cocktails_by_ingredient("vodka")

# Find cocktails with multiple ingredients (ALL required)
gin_lemon_cocktails = helper.find_cocktails_by_multiple_ingredients(
    ["gin", "lemon"], require_all=True
)

# Find cocktails with any of the ingredients
whiskey_cocktails = helper.find_cocktails_by_multiple_ingredients(
    ["bourbon", "rye", "scotch"], require_all=False
)
```

## Demo Script

Run the comprehensive demo to see all features in action:

```bash
python demo.py
```

The demo will:
1. Test the quantity parser with various formats
2. Scrape cocktails (or load from cache)
3. Demonstrate search functions
4. Show cocktail recommendations based on available ingredients
5. Display detailed cocktail recipes

## Core Classes

### `IBACocktailScraper`

Main scraper class for extracting cocktail data from the IBA website.

**Key Methods:**
- `scrape_all_cocktails()`: Scrapes all cocktails and returns a dictionary
- `parse_cocktail_page(url, category)`: Parses individual cocktail page
- `get_all_cocktail_urls()`: Discovers cocktail URLs by category

### `QuantityParser`

Advanced parser for ingredient quantities using regex patterns.

**Supported Formats:**
- Standard measurements: `30 ml`, `1.5 oz`, `2 cl`
- Fractions: `1/2 oz`, `3/4 cl`, `1 1/2 oz`
- Ranges: `2-3 dashes`, `15-20 ml`
- Special units: `pinch`, `splash`, `slice`, `sprig`
- Descriptive: `to taste`, `as needed`, `garnish`

**Key Methods:**
- `parse_quantity(text)`: Parses quantity text into structured format
- `convert_to_ml(quantity)`: Converts any quantity to milliliters
- `normalize_quantities(ingredients)`: Normalizes all quantities to ml

### `CocktailHelper`

Helper class providing search and analysis functions.

**Key Methods:**
- `find_cocktails_by_ingredient(ingredient, exact_match=False)`: Find by single ingredient
- `find_cocktails_by_multiple_ingredients(ingredients, require_all=True)`: Find by multiple ingredients
- `get_all_ingredients()`: Get ingredient usage statistics
- `get_cocktails_by_category(category)`: Filter by IBA category
- `get_cocktail_stats()`: Get database statistics

### Data Structures

#### `IngredientQuantity`
```python
@dataclass
class IngredientQuantity:
    amount: float
    unit: str
    original_text: str
    is_range: bool = False
    min_amount: Optional[float] = None
    max_amount: Optional[float] = None
```

#### `Ingredient`
```python
@dataclass
class Ingredient:
    name: str
    quantity: IngredientQuantity
    category: str = "unknown"
```

#### `Cocktail`
```python
@dataclass
class Cocktail:
    name: str
    category: str  # The Unforgettables, Contemporary Classics, New Era
    ingredients: List[Ingredient]
    method: str
    garnish: str
    glass_type: str = ""
    views: int = 0
    url: str = ""
```

## Advanced Usage Examples

### Building a Home Bar Recommendation System

```python
def recommend_cocktails(home_bar_ingredients, cocktails):
    helper = CocktailHelper(cocktails)
    recommendations = []
    
    for cocktail in cocktails.values():
        # Calculate ingredient match percentage
        cocktail_ingredients = [ing.name.lower() for ing in cocktail.ingredients]
        matches = sum(1 for bar_item in home_bar_ingredients 
                     if any(bar_item.lower() in ci or ci in bar_item.lower() 
                           for ci in cocktail_ingredients))
        
        match_percentage = matches / len(cocktail.ingredients)
        
        if match_percentage >= 0.7:  # 70% ingredient match
            recommendations.append((cocktail, match_percentage))
    
    return sorted(recommendations, key=lambda x: x[1], reverse=True)

# Example usage
home_bar = ["gin", "vodka", "lime juice", "simple syrup", "tonic water"]
recommendations = recommend_cocktails(home_bar, cocktails)
```

### Analyzing Cocktail Trends

```python
def analyze_ingredient_trends(cocktails):
    helper = CocktailHelper(cocktails)
    
    # Get ingredient popularity by category
    categories = ["The Unforgettables", "Contemporary Classics", "New Era"]
    
    for category in categories:
        category_cocktails = helper.get_cocktails_by_category(category)
        category_helper = CocktailHelper({c.name: c for c in category_cocktails})
        
        print(f"\n{category}:")
        ingredients = category_helper.get_all_ingredients()
        for ingredient, count in list(ingredients.items())[:5]:
            print(f"  {ingredient}: {count} cocktails")
```

### Custom Quantity Analysis

```python
def analyze_alcohol_content(cocktail):
    """Estimate alcohol content of a cocktail"""
    parser = QuantityParser()
    total_volume = 0
    alcohol_volume = 0
    
    # Approximate alcohol percentages for common spirits
    alcohol_percentages = {
        'vodka': 0.4, 'gin': 0.4, 'rum': 0.4, 'whiskey': 0.4,
        'bourbon': 0.4, 'scotch': 0.4, 'tequila': 0.4,
        'liqueur': 0.2, 'vermouth': 0.15, 'wine': 0.12
    }
    
    for ingredient in cocktail.ingredients:
        volume_ml = parser.convert_to_ml(ingredient.quantity)
        total_volume += volume_ml
        
        # Estimate alcohol content
        for spirit, percentage in alcohol_percentages.items():
            if spirit in ingredient.name.lower():
                alcohol_volume += volume_ml * percentage
                break
    
    if total_volume > 0:
        abv = (alcohol_volume / total_volume) * 100
        return round(abv, 1)
    return 0
```

## Data Persistence

Save and load cocktail data:

```python
from iba_cocktail_scraper import save_cocktails_to_json, load_cocktails_from_json

# Save cocktails to JSON file
save_cocktails_to_json(cocktails, "my_cocktails.json")

# Load cocktails from JSON file
loaded_cocktails = load_cocktails_from_json("my_cocktails.json")
```

## Error Handling

The scraper includes comprehensive error handling:

- Network timeouts and connection errors
- Missing or malformed HTML elements
- Invalid quantity formats
- Rate limiting with respectful delays

## Ethical Usage

This scraper is designed to be respectful:
- Uses delays between requests (default 1.5 seconds)
- Includes proper User-Agent headers
- Handles errors gracefully
- Caches results to avoid repeated requests

## IBA Categories

The scraper organizes cocktails into three official IBA categories:

1. **The Unforgettables**: Classic cocktails that have stood the test of time
2. **Contemporary Classics**: Modern classics that have gained widespread acceptance
3. **New Era**: Recently added cocktails representing current trends

## Dependencies

- `requests`: HTTP library for web scraping
- `beautifulsoup4`: HTML parsing library
- `lxml`: Fast XML/HTML parser (optional but recommended)

## License

This project is for educational and personal use. Please respect the IBA website's terms of service and use responsibly.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Troubleshooting

### Common Issues

1. **No cocktails scraped**: Check internet connection and verify IBA website is accessible
2. **Parsing errors**: Some cocktail pages may have different HTML structure
3. **Rate limiting**: Increase delay between requests if you encounter 429 errors

### Debug Mode

Enable debug mode for verbose logging:

```python
scraper = IBACocktailScraper(delay=2.0)  # Increase delay
# Add debug prints in the parsing methods
```

## Example Output

```
🍸 MARTINI
Category: The Unforgettables
Views: 150,000
URL: https://iba-world.com/dry-martini/

Ingredients:
  • 60.0 ml Gin
  • 10.0 ml Dry Vermouth

Method: Stir over ice, strain into chilled glass
Garnish: Lemon twist or olive
```

---

**Happy mixing! 🥂**
