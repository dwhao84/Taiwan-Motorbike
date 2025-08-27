#!/usr/bin/env python3
"""
Taiwan Specific Motorcycle Database Usage Example

This script demonstrates how to use the taiwan_specific_motorcycles.json database
containing curated Taiwan motorcycle models.
"""

import json
from collections import Counter

def load_taiwan_specific_database(filename='taiwan_specific_motorcycles.json'):
    """Load the Taiwan specific motorcycle database"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def filter_by_brand(motorcycles, brand):
    """Filter motorcycles by brand"""
    return [m for m in motorcycles if m['brand'].lower() == brand.lower()]

def filter_by_displacement(motorcycles, min_cc=None, max_cc=None):
    """Filter motorcycles by engine displacement"""
    result = []
    for m in motorcycles:
        displacement = m['engine']['displacement']
        if displacement == "Electric Motor":
            # Include electric motorcycles if no max limit specified
            if max_cc is None:
                result.append(m)
            continue
            
        cc_str = displacement.replace('cc', '')
        cc = int(cc_str)
        
        if min_cc and cc < min_cc:
            continue
        if max_cc and cc > max_cc:
            continue
        
        result.append(m)
    
    return result

def filter_by_price_range(motorcycles, max_price):
    """Filter motorcycles by maximum price"""
    result = []
    for m in motorcycles:
        price_range = m['price_range']
        # Extract the lower price from range like "NT$ 65,000 - 72,000"
        lower_price_str = price_range.split(' - ')[0].replace('NT$ ', '').replace(',', '')
        lower_price = int(lower_price_str)
        
        if lower_price <= max_price:
            result.append(m)
    
    return result

def analyze_taiwan_database(data):
    """Perform analysis of the Taiwan specific database"""
    motorcycles = data['motorcycles']
    
    print("=== Taiwan Specific Motorcycle Database Analysis ===")
    print(f"Total motorcycles: {len(motorcycles)}")
    print(f"Database last updated: {data.get('last_updated', 'Unknown')}")
    print()
    
    # Brand distribution
    brands = Counter(m['brand'] for m in motorcycles)
    print("Brand Distribution:")
    for brand, count in brands.most_common():
        print(f"  {brand}: {count} models")
    print()
    
    # Vehicle type distribution
    types = Counter(m['type'] for m in motorcycles)
    print("Vehicle Type Distribution:")
    for vtype, count in types.most_common():
        print(f"  {vtype}: {count} models")
    print()
    
    # Displacement analysis
    displacements = []
    electric_count = 0
    for m in motorcycles:
        displacement = m['engine']['displacement']
        if displacement == "Electric Motor":
            electric_count += 1
        else:
            cc_str = displacement.replace('cc', '')
            displacements.append(int(cc_str))
    
    if displacements:
        print("Displacement Statistics (Gas engines):")
        print(f"  Minimum: {min(displacements)}cc")
        print(f"  Maximum: {max(displacements)}cc")
        print(f"  Average: {sum(displacements) / len(displacements):.1f}cc")
    
    if electric_count > 0:
        print(f"  Electric motorcycles: {electric_count}")
    print()

def example_queries(motorcycles):
    """Demonstrate various database queries"""
    print("=== Example Queries ===")
    
    # 1. Find all SYM models
    sym_models = filter_by_brand(motorcycles, 'SYM')
    print(f"1. SYM models: {len(sym_models)} models")
    for bike in sym_models:
        print(f"   - {bike['model']} ({bike['engine']['displacement']})")
    print()
    
    # 2. Find motorcycles 125cc and under
    small_bikes = filter_by_displacement(motorcycles, max_cc=125)
    print(f"2. Motorcycles 125cc and under: {len(small_bikes)} models")
    
    # 3. Find motorcycles over 150cc
    larger_bikes = filter_by_displacement(motorcycles, min_cc=150)
    print(f"3. Motorcycles over 150cc: {len(larger_bikes)} models")
    for bike in larger_bikes:
        print(f"   - {bike['brand']} {bike['model']} ({bike['engine']['displacement']})")
    print()
    
    # 4. Find budget motorcycles under NT$ 70,000
    budget_bikes = filter_by_price_range(motorcycles, 70000)
    print(f"4. Budget motorcycles under NT$ 70,000: {len(budget_bikes)} models")
    for bike in budget_bikes:
        print(f"   - {bike['brand']} {bike['model']} - {bike['price_range']}")
    print()
    
    # 5. Show all models with Chinese and English names
    print("5. Models with Chinese names:")
    for bike in motorcycles:
        if 'model_english' in bike:
            print(f"   - {bike['model']} ({bike['model_english']}) - {bike['brand']}")
        else:
            print(f"   - {bike['model']} - {bike['brand']}")
    print()

def main():
    """Main function"""
    try:
        # Load the Taiwan specific database
        data = load_taiwan_specific_database()
        motorcycles = data['motorcycles']
        
        # Perform analysis
        analyze_taiwan_database(data)
        
        # Run example queries
        example_queries(motorcycles)
        
        # Show some detailed examples
        print("=== Detailed Examples ===")
        for i, bike in enumerate(motorcycles[:3]):
            print(f"{i+1}. {bike['brand']} {bike['model']}")
            if 'model_english' in bike:
                print(f"   English name: {bike['model_english']}")
            print(f"   Type: {bike['type']}")
            print(f"   Engine: {bike['engine']['displacement']} {bike['engine']['type']}")
            print(f"   Power: {bike['engine']['power']}")
            print(f"   Price: {bike['price_range']}")
            print(f"   Features: {', '.join(bike['features'])}")
            print()
            
    except FileNotFoundError:
        print("Error: taiwan_specific_motorcycles.json not found!")
        print("Please make sure the file exists in the current directory.")
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()