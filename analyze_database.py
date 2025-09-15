#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taiwan Motorcycle Database Usage Example

This script demonstrates various ways to use the TaiwanMotor.json database
for analysis and data exploration.
"""

import json
from collections import Counter, defaultdict

def load_database():
    """Load the Taiwan motorcycle database."""
    with open('TaiwanMotor.json', 'r', encoding='utf-8') as f:
        motorcycles = json.load(f)
    return motorcycles

def analyze_brands(motorcycles):
    """Analyze brand distribution in the database."""
    print("=== Brand Analysis ===")
    brand_counts = Counter(bike['brand'] for bike in motorcycles)
    
    print(f"Total brands: {len(brand_counts)}")
    print(f"Total motorcycles: {len(motorcycles)}")
    print("\nBrand distribution:")
    
    for brand, count in brand_counts.most_common():
        percentage = (count / len(motorcycles)) * 100
        print(f"  {brand:12} {count:3} models ({percentage:5.1f}%)")

def analyze_models_by_brand(motorcycles):
    """Show sample models for each brand."""
    print("\n=== Sample Models by Brand ===")
    brands = defaultdict(list)
    
    for bike in motorcycles:
        brands[bike['brand']].append(bike['model'])
    
    for brand, models in sorted(brands.items()):
        print(f"\n{brand} ({len(models)} models):")
        # Show first 5 models
        for i, model in enumerate(models[:5]):
            print(f"  • {model}")
        if len(models) > 5:
            print(f"  ... and {len(models) - 5} more models")

def search_models(motorcycles, keyword):
    """Search for models containing specific keywords."""
    matching_bikes = [bike for bike in motorcycles 
                     if keyword.lower() in bike['model'].lower()]
    return matching_bikes

def analyze_chinese_vs_english(motorcycles):
    """Analyze Chinese vs English model names."""
    print("\n=== Model Name Language Analysis ===")
    
    chinese_models = []
    english_models = []
    mixed_models = []
    
    for bike in motorcycles:
        model = bike['model']
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in model)
        has_english = any(char.isascii() and char.isalpha() for char in model)
        
        if has_chinese and has_english:
            mixed_models.append(bike)
        elif has_chinese:
            chinese_models.append(bike)
        else:
            english_models.append(bike)
    
    print(f"Models with Chinese names only: {len(chinese_models)}")
    print(f"Models with English names only: {len(english_models)}")
    print(f"Models with mixed names: {len(mixed_models)}")
    
    print("\nSample mixed language models:")
    for bike in mixed_models[:5]:
        print(f"  • {bike['brand']} {bike['model']}")

def find_electric_models(motorcycles):
    """Find electric motorcycle models."""
    print("\n=== Electric Motorcycle Analysis ===")
    
    # Gogoro is the main electric brand
    electric_bikes = [bike for bike in motorcycles if bike['brand'] == 'Gogoro']
    
    # Also check Aeon electric models
    aeon_electric = [bike for bike in motorcycles 
                    if bike['brand'] == 'Aeon' and 
                    ('EV' in bike['model'] or 'eReady' in bike['model'] or 'Ai-' in bike['model'])]
    
    all_electric = electric_bikes + aeon_electric
    
    print(f"Total electric models: {len(all_electric)}")
    print(f"Gogoro models: {len(electric_bikes)}")
    print(f"Aeon electric models: {len(aeon_electric)}")
    
    print("\nGogoro model series:")
    for bike in electric_bikes:
        print(f"  • {bike['model']}")

def find_popular_keywords(motorcycles):
    """Find popular keywords in model names."""
    print("\n=== Popular Model Keywords ===")
    
    keywords = ['ABS', 'Racing', 'Sport', 'GTR', 'Max', '125', '150', '250']
    
    for keyword in keywords:
        matches = search_models(motorcycles, keyword)
        if matches:
            print(f"\n'{keyword}' appears in {len(matches)} models:")
            for bike in matches[:3]:  # Show first 3
                print(f"  • {bike['brand']} {bike['model']}")
            if len(matches) > 3:
                print(f"  ... and {len(matches) - 3} more")

def main():
    """Main function to run all analyses."""
    print("Taiwan Motorcycle Database Analysis")
    print("=" * 50)
    
    try:
        motorcycles = load_database()
        
        analyze_brands(motorcycles)
        analyze_models_by_brand(motorcycles)
        analyze_chinese_vs_english(motorcycles)
        find_electric_models(motorcycles)
        find_popular_keywords(motorcycles)
        
        print("\n" + "=" * 50)
        print("Analysis complete!")
        
    except FileNotFoundError:
        print("Error: TaiwanMotor.json file not found!")
        print("Please make sure the file exists in the current directory.")
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()