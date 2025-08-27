#!/usr/bin/env python3
"""
Example usage of the Taiwan Motorcycle Database

This script demonstrates how to load and use the motorcycle database
for various analysis and filtering tasks.
"""

import json
from collections import Counter

def load_database(filename='complete_motorcycle_database.json'):
    """Load the motorcycle database"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def filter_by_brand(motorcycles, brand):
    """Filter motorcycles by brand"""
    return [m for m in motorcycles if m['brand'].lower() == brand.lower()]

def filter_by_displacement(motorcycles, min_cc=None, max_cc=None):
    """Filter motorcycles by engine displacement"""
    result = []
    for m in motorcycles:
        cc_str = m['engine']['displacement'].replace('cc', '')
        cc = int(cc_str)
        
        if min_cc and cc < min_cc:
            continue
        if max_cc and cc > max_cc:
            continue
        
        result.append(m)
    
    return result

def filter_by_type(motorcycles, vehicle_type):
    """Filter motorcycles by vehicle type"""
    return [m for m in motorcycles if vehicle_type.lower() in m['type'].lower()]

def filter_by_price_range(motorcycles, max_price_nt):
    """Filter motorcycles by maximum price"""
    result = []
    for m in motorcycles:
        # Extract price from string like "NT$ 47,500 - 52,500"
        price_str = m['price_range'].replace('NT$', '').replace(',', '').strip()
        price_parts = price_str.split(' - ')
        min_price = int(price_parts[0].strip())
        
        if min_price <= max_price_nt:
            result.append(m)
    
    return result

def analyze_database(data):
    """Perform basic analysis of the database"""
    motorcycles = data['motorcycles']
    
    print("=== Taiwan Motorcycle Database Analysis ===")
    print(f"Total motorcycles: {len(motorcycles)}")
    print(f"Database last updated: {data.get('last_updated', 'Unknown')}")
    print()
    
    # Brand distribution
    brands = Counter(m['brand'] for m in motorcycles)
    print("Brand Distribution:")
    for brand, count in brands.most_common():
        print(f"  {brand}: {count}")
    print()
    
    # Vehicle type distribution
    types = Counter(m['type'] for m in motorcycles)
    print("Vehicle Type Distribution:")
    for vtype, count in types.most_common(10):  # Top 10
        print(f"  {vtype}: {count}")
    print()
    
    # Displacement distribution
    displacements = []
    for m in motorcycles:
        cc_str = m['engine']['displacement'].replace('cc', '')
        displacements.append(int(cc_str))
    
    print("Displacement Statistics:")
    print(f"  Minimum: {min(displacements)}cc")
    print(f"  Maximum: {max(displacements)}cc")
    print(f"  Average: {sum(displacements) / len(displacements):.1f}cc")
    print()

def example_queries(motorcycles):
    """Demonstrate various database queries"""
    print("=== Example Queries ===")
    
    # 1. Find all Honda scooters
    honda_scooters = filter_by_type(filter_by_brand(motorcycles, 'Honda'), 'scooter')
    print(f"1. Honda scooters: {len(honda_scooters)} models")
    
    # 2. Find motorcycles under 150cc
    small_bikes = filter_by_displacement(motorcycles, max_cc=150)
    print(f"2. Motorcycles 150cc and under: {len(small_bikes)} models")
    
    # 3. Find sport bikes over 500cc
    big_sport_bikes = filter_by_displacement(filter_by_type(motorcycles, 'sport'), min_cc=500)
    print(f"3. Sport bikes over 500cc: {len(big_sport_bikes)} models")
    
    # 4. Find budget motorcycles under NT$ 100,000
    budget_bikes = filter_by_price_range(motorcycles, 100000)
    print(f"4. Motorcycles under NT$ 100,000: {len(budget_bikes)} models")
    
    # 5. Show some specific examples
    print("\n5. Example motorcycles:")
    sample_bikes = motorcycles[:5]
    for bike in sample_bikes:
        print(f"   {bike['brand']} {bike['model']}")
        print(f"     Type: {bike['type']}")
        print(f"     Engine: {bike['engine']['displacement']} {bike['engine']['type']}")
        print(f"     Power: {bike['engine']['power']}")
        print(f"     Price: {bike['price_range']}")
        print(f"     Features: {', '.join(bike['features'])}")
        print()

def main():
    """Main function demonstrating database usage"""
    # Load the database
    try:
        data = load_database()
        motorcycles = data['motorcycles']
    except FileNotFoundError:
        print("Error: complete_motorcycle_database.json not found!")
        print("Please run generate_motorcycle_database.py first to create the database.")
        return
    
    # Perform analysis
    analyze_database(data)
    
    # Run example queries
    example_queries(motorcycles)
    
    print("=== Custom Query Example ===")
    print("Find all Yamaha motorcycles between 250cc and 600cc:")
    yamaha_mid = filter_by_displacement(filter_by_brand(motorcycles, 'Yamaha'), 250, 600)
    
    for bike in yamaha_mid[:5]:  # Show first 5 results
        print(f"  {bike['model']} - {bike['engine']['displacement']} ({bike['price_range']})")

if __name__ == "__main__":
    main()