#!/usr/bin/env python3
"""
IBA Cocktail Scraper Demo
========================

This demo script shows how to use the IBA cocktail scraper and all its features:
1. Scraping cocktails from the IBA website
2. Parsing ingredient quantities with regex
3. Finding cocktails by ingredients
4. Working with the cocktail database

Run this script to see the system in action!
"""

from iba_cocktail_scraper import (
    IBACocktailScraper, 
    CocktailHelper, 
    QuantityParser,
    save_cocktails_to_json,
    load_cocktails_from_json
)
import os

def demo_quantity_parser():
    """Demonstrate the quantity parser functionality"""
    print("=" * 60)
    print("QUANTITY PARSER DEMONSTRATION")
    print("=" * 60)
    
    parser = QuantityParser()
    
    # Test various quantity formats
    test_quantities = [
        "30 ml",           # Standard measurement
        "1.5 oz",          # Decimal measurement
        "1/2 oz",          # Simple fraction
        "1 1/2 cl",        # Mixed fraction
        "2-3 dashes",      # Range with special unit
        "15-20 ml",        # Range with standard unit
        "to taste",        # Descriptive
        "2 slices",        # Countable items
        "1 sprig",         # Garnish items
        "3/4 cup",         # Different fraction format
        "45",              # Number only (assumes ml)
        "splash",          # Just unit
        "2 pinches"        # Multiple special units
    ]
    
    print("\nTesting quantity parsing:")
    print("-" * 40)
    for qty in test_quantities:
        parsed = parser.parse_quantity(qty)
        ml_equivalent = parser.convert_to_ml(parsed)
        
        print(f"Input: '{qty}'")
        print(f"  → Amount: {parsed.amount}")
        print(f"  → Unit: {parsed.unit}")
        print(f"  → Range: {parsed.is_range}")
        if parsed.is_range:
            print(f"  → Min: {parsed.min_amount}, Max: {parsed.max_amount}")
        print(f"  → ML equivalent: {ml_equivalent:.2f} ml")
        print()

def demo_scraping():
    """Demonstrate cocktail scraping"""
    print("=" * 60)
    print("COCKTAIL SCRAPING DEMONSTRATION")
    print("=" * 60)
    
    # Check if we already have scraped data
    if os.path.exists("iba_cocktails.json"):
        print("Found existing cocktail data. Loading from file...")
        cocktails = load_cocktails_from_json("iba_cocktails.json")
        print(f"Loaded {len(cocktails)} cocktails from cache.")
    else:
        print("No cached data found. Starting fresh scraping...")
        print("Note: This will take several minutes and make many web requests.")
        print("The scraper is respectful with delays between requests.")
        
        scraper = IBACocktailScraper(delay=1.5)  # 1.5 second delay between requests
        cocktails = scraper.scrape_all_cocktails()
        
        if cocktails:
            save_cocktails_to_json(cocktails)
            print(f"Successfully scraped and saved {len(cocktails)} cocktails!")
        else:
            print("Failed to scrape cocktails. Check your internet connection.")
            return None
    
    return cocktails

def demo_helper_functions(cocktails):
    """Demonstrate the helper functions"""
    print("=" * 60)
    print("HELPER FUNCTIONS DEMONSTRATION")
    print("=" * 60)
    
    helper = CocktailHelper(cocktails)
    
    # Get database statistics
    print("\n1. DATABASE STATISTICS:")
    print("-" * 30)
    stats = helper.get_cocktail_stats()
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # Find cocktails by single ingredient
    print("\n2. FINDING COCKTAILS BY INGREDIENT:")
    print("-" * 40)
    
    ingredients_to_test = ["gin", "vodka", "rum", "whiskey", "tequila"]
    
    for ingredient in ingredients_to_test:
        matching_cocktails = helper.find_cocktails_by_ingredient(ingredient)
        print(f"\nCocktails with {ingredient} ({len(matching_cocktails)} found):")
        for cocktail in matching_cocktails[:3]:  # Show first 3
            print(f"  • {cocktail.name} ({cocktail.category})")
    
    # Find cocktails by multiple ingredients
    print("\n3. FINDING COCKTAILS BY MULTIPLE INGREDIENTS:")
    print("-" * 50)
    
    # Test requiring ALL ingredients
    multi_ingredients = ["gin", "lemon"]
    matching_all = helper.find_cocktails_by_multiple_ingredients(
        multi_ingredients, require_all=True
    )
    print(f"\nCocktails with BOTH gin AND lemon ({len(matching_all)} found):")
    for cocktail in matching_all[:5]:
        print(f"  • {cocktail.name}")
    
    # Test requiring ANY ingredient
    matching_any = helper.find_cocktails_by_multiple_ingredients(
        ["bourbon", "rye"], require_all=False
    )
    print(f"\nCocktails with bourbon OR rye ({len(matching_any)} found):")
    for cocktail in matching_any[:5]:
        print(f"  • {cocktail.name}")
    
    # Get cocktails by category
    print("\n4. COCKTAILS BY CATEGORY:")
    print("-" * 30)
    
    categories = ["The Unforgettables", "Contemporary Classics", "New Era"]
    for category in categories:
        category_cocktails = helper.get_cocktails_by_category(category)
        print(f"\n{category} ({len(category_cocktails)} cocktails):")
        for cocktail in category_cocktails[:3]:  # Show first 3
            print(f"  • {cocktail.name}")
    
    # Show detailed recipe for a few cocktails
    print("\n5. DETAILED COCKTAIL RECIPES:")
    print("-" * 35)
    
    sample_cocktails = list(cocktails.values())[:3]  # Get first 3 cocktails
    
    for cocktail in sample_cocktails:
        print(f"\n🍸 {cocktail.name.upper()}")
        print(f"Category: {cocktail.category}")
        print(f"Views: {cocktail.views:,}" if cocktail.views > 0 else "Views: N/A")
        print(f"URL: {cocktail.url}")
        
        print("\nIngredients:")
        for ingredient in cocktail.ingredients:
            qty = ingredient.quantity
            if qty.is_range:
                print(f"  • {qty.min_amount}-{qty.max_amount} {qty.unit} {ingredient.name}")
            else:
                print(f"  • {qty.amount} {qty.unit} {ingredient.name}")
        
        print(f"\nMethod: {cocktail.method}")
        if cocktail.garnish:
            print(f"Garnish: {cocktail.garnish}")
        print("-" * 40)

def demo_advanced_features(cocktails):
    """Demonstrate advanced features"""
    print("=" * 60)
    print("ADVANCED FEATURES DEMONSTRATION")
    print("=" * 60)
    
    helper = CocktailHelper(cocktails)
    
    # Get most popular ingredients
    print("\n1. MOST POPULAR INGREDIENTS:")
    print("-" * 35)
    all_ingredients = helper.get_all_ingredients()
    top_10 = dict(list(all_ingredients.items())[:10])
    
    for ingredient, count in top_10.items():
        print(f"  {ingredient}: {count} cocktails")
    
    # Find cocktails you can make with specific ingredients
    print("\n2. COCKTAIL RECOMMENDATIONS:")
    print("-" * 35)
    
    # Simulate a home bar inventory
    home_bar = ["gin", "vodka", "lime", "lemon", "simple syrup", "tonic", "soda"]
    
    print(f"Your home bar: {', '.join(home_bar)}")
    print("\nCocktails you can make:")
    
    possible_cocktails = []
    for cocktail in cocktails.values():
        cocktail_ingredients = [ing.name.lower() for ing in cocktail.ingredients]
        
        # Check if we have most of the ingredients (at least 60%)
        matches = sum(1 for bar_item in home_bar 
                     if any(bar_item in ci or ci in bar_item 
                           for ci in cocktail_ingredients))
        
        if matches >= len(cocktail.ingredients) * 0.6:  # 60% ingredient match
            possible_cocktails.append((cocktail, matches))
    
    # Sort by number of matching ingredients
    possible_cocktails.sort(key=lambda x: x[1], reverse=True)
    
    for cocktail, matches in possible_cocktails[:5]:
        missing_ingredients = []
        for ingredient in cocktail.ingredients:
            ing_name = ingredient.name.lower()
            if not any(bar_item in ing_name or ing_name in bar_item 
                      for bar_item in home_bar):
                missing_ingredients.append(ingredient.name)
        
        print(f"\n  🍹 {cocktail.name}")
        print(f"     Match: {matches}/{len(cocktail.ingredients)} ingredients")
        if missing_ingredients:
            print(f"     Missing: {', '.join(missing_ingredients)}")
        else:
            print(f"     ✅ You have everything!")

def main():
    """Main demo function"""
    print("🍸 IBA COCKTAIL SCRAPER DEMO 🍸")
    print("Welcome to the comprehensive cocktail database system!")
    print()
    
    # Demo 1: Quantity Parser
    demo_quantity_parser()
    
    # Demo 2: Scraping (or loading cached data)
    cocktails = demo_scraping()
    
    if not cocktails:
        print("Cannot continue without cocktail data. Exiting.")
        return
    
    # Demo 3: Helper Functions
    demo_helper_functions(cocktails)
    
    # Demo 4: Advanced Features
    demo_advanced_features(cocktails)
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETE!")
    print("=" * 60)
    print(f"Total cocktails in database: {len(cocktails)}")
    print("Data saved to: iba_cocktails.json")
    print("\nYou can now use this system to:")
    print("• Find cocktails by ingredients")
    print("• Parse ingredient quantities")
    print("• Analyze cocktail trends")
    print("• Build your own cocktail applications")
    print("\nEnjoy exploring the world of cocktails! 🥂")

if __name__ == "__main__":
    main()