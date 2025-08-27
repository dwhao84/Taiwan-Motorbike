#!/usr/bin/env python3
"""
Taiwan Specific Motorcycle Database Usage Example

This script demonstrates how to work with the Taiwan-specific motorcycle database
containing 2000+ entries covering all major brands and categories.
"""

import json
from collections import Counter
import re

def load_taiwan_database(filename='taiwan_specific_motorcycles.json'):
    """Load the Taiwan motorcycle database"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_database(data):
    """Perform comprehensive analysis of the Taiwan database"""
    motorcycles = data['motorcycles']
    
    print("=== Taiwan Motorcycle Database Analysis ===")
    print(f"Total motorcycles: {len(motorcycles)}")
    print(f"Database last updated: {data.get('last_updated', 'Unknown')}")
    print()
    
    # Brand analysis
    brands = Counter(m['brand'] for m in motorcycles)
    print("Brand Distribution:")
    taiwan_brands = ['SYM', 'KYMCO', 'PGO', 'AEON']
    international_brands = ['YAMAHA', 'HONDA', 'SUZUKI', 'KAWASAKI']
    electric_brands = ['GOGORO']
    
    print("  Taiwan Brands:")
    for brand in taiwan_brands:
        count = brands.get(brand, 0)
        print(f"    {brand}: {count}")
    
    print("  International Brands in Taiwan:")
    for brand in international_brands:
        count = brands.get(brand, 0)
        print(f"    {brand}: {count}")
    
    print("  Electric Brands:")
    for brand in electric_brands:
        count = brands.get(brand, 0)
        print(f"    {brand}: {count}")
    print()
    
    # Vehicle type analysis
    types = Counter(m['type'] for m in motorcycles)
    print("Vehicle Type Distribution:")
    for vtype, count in types.most_common():
        print(f"  {vtype}: {count}")
    print()
    
    # Year coverage
    years = Counter(m['model_year'] for m in motorcycles)
    print("Model Year Distribution:")
    for year in sorted(years.keys()):
        print(f"  {year}: {years[year]}")
    print()
    
    # Displacement analysis
    print("Displacement Analysis:")
    displacement_categories = {
        '50cc級距 (50-80cc)': (50, 80),
        '100cc級距 (90-110cc)': (90, 110),
        '125cc級距 (120-150cc)': (120, 150),
        '150cc級距 (150-180cc)': (150, 180),
        '200cc級距 (200-300cc)': (200, 300),
        '重機級距 (300cc+)': (300, 2000),
        '電動車': None
    }
    
    for category, disp_range in displacement_categories.items():
        if category == '電動車':
            count = sum(1 for m in motorcycles if m['engine']['displacement'] == 'Electric Motor')
        else:
            count = 0
            for m in motorcycles:
                disp_str = m['engine']['displacement']
                if 'cc' in disp_str:
                    try:
                        cc = int(disp_str.replace('cc', ''))
                        if disp_range[0] <= cc <= disp_range[1]:
                            count += 1
                    except ValueError:
                        pass
        print(f"  {category}: {count}")
    print()
    
    # Price analysis
    print("Price Range Analysis:")
    price_categories = {
        'Entry Level (< NT$ 80,000)': (0, 80000),
        'Commuter (NT$ 80,000 - 120,000)': (80000, 120000),
        'Family (NT$ 120,000 - 200,000)': (120000, 200000),
        'Sport/Premium (NT$ 200,000 - 500,000)': (200000, 500000),
        'Heavy Bike (NT$ 500,000+)': (500000, 2000000)
    }
    
    for category, (min_price, max_price) in price_categories.items():
        count = 0
        for m in motorcycles:
            price_str = m['price_range']
            numbers = re.findall(r'[\d,]+', price_str)
            if len(numbers) >= 2:
                try:
                    min_p = int(numbers[0].replace(',', ''))
                    max_p = int(numbers[1].replace(',', ''))
                    avg_price = (min_p + max_p) / 2
                    if min_price <= avg_price <= max_price:
                        count += 1
                except ValueError:
                    pass
        print(f"  {category}: {count}")
    print()
    
    # Market category analysis
    categories = Counter(m['category'] for m in motorcycles)
    print("Market Categories:")
    for category, count in categories.most_common():
        print(f"  {category}: {count}")
    print()
    
    # Target audience analysis
    audiences = Counter(m['target_audience'] for m in motorcycles)
    print("Target Audiences:")
    for audience, count in audiences.most_common():
        print(f"  {audience}: {count}")
    print()

def example_queries(motorcycles):
    """Demonstrate various database queries"""
    print("=== Example Queries ===")
    
    # 1. Find entry-level scooters for students
    print("1. Entry-level scooters for students (< NT$ 80,000):")
    entry_level = []
    for m in motorcycles:
        price_str = m['price_range']
        numbers = re.findall(r'[\d,]+', price_str)
        if len(numbers) >= 2:
            try:
                max_price = int(numbers[1].replace(',', ''))
                if (max_price < 80000 and 
                    'Scooter' in m['type'] and 
                    m['target_audience'] == '學生族群'):
                    entry_level.append(m)
            except ValueError:
                pass
    
    for bike in entry_level[:5]:
        print(f"  • {bike['brand']} {bike['model']} - {bike['price_range']}")
    print(f"  Total found: {len(entry_level)}")
    print()
    
    # 2. Electric vehicles
    print("2. Electric vehicles:")
    electric = [m for m in motorcycles if m['engine']['displacement'] == 'Electric Motor']
    for bike in electric[:5]:
        battery = bike.get('battery_capacity', 'N/A')
        range_km = bike.get('range', 'N/A')
        print(f"  • {bike['brand']} {bike['model']}")
        print(f"    Battery: {battery}, Range: {range_km}, Price: {bike['price_range']}")
    print(f"  Total found: {len(electric)}")
    print()
    
    # 3. Heavy bikes (300cc+)
    print("3. Heavy bikes (300cc+):")
    heavy_bikes = []
    for m in motorcycles:
        disp_str = m['engine']['displacement']
        if 'cc' in disp_str:
            try:
                cc = int(disp_str.replace('cc', ''))
                if cc >= 300:
                    heavy_bikes.append(m)
            except ValueError:
                pass
    
    for bike in heavy_bikes[:5]:
        print(f"  • {bike['brand']} {bike['model']} - {bike['engine']['displacement']}")
        print(f"    Power: {bike['engine']['power']}, Price: {bike['price_range']}")
    print(f"  Total found: {len(heavy_bikes)}")
    print()
    
    # 4. Latest models (2024-2025)
    print("4. Latest models (2024-2025):")
    latest = [m for m in motorcycles if m['model_year'] >= 2024]
    for bike in latest[:5]:
        print(f"  • {bike['brand']} {bike['model']} ({bike['model_year']})")
        print(f"    Type: {bike['type']}, Price: {bike['price_range']}")
    print(f"  Total found: {len(latest)}")
    print()
    
    # 5. Sport bikes from Japanese brands
    print("5. Sport bikes from Japanese brands:")
    japanese_brands = ['YAMAHA', 'HONDA', 'SUZUKI', 'KAWASAKI']
    sport_bikes = [m for m in motorcycles 
                   if m['brand'] in japanese_brands and 
                   'Sport' in m['type']]
    
    for bike in sport_bikes[:5]:
        print(f"  • {bike['brand']} {bike['model']}")
        print(f"    Engine: {bike['engine']['displacement']} {bike['engine']['power']}")
        print(f"    Price: {bike['price_range']}")
    print(f"  Total found: {len(sport_bikes)}")
    print()

def filter_by_criteria(motorcycles, **criteria):
    """Filter motorcycles by various criteria"""
    filtered = motorcycles.copy()
    
    for key, value in criteria.items():
        if key == 'brand':
            filtered = [m for m in filtered if m['brand'] == value]
        elif key == 'type':
            filtered = [m for m in filtered if m['type'] == value]
        elif key == 'max_price':
            new_filtered = []
            for m in filtered:
                price_str = m['price_range']
                numbers = re.findall(r'[\d,]+', price_str)
                if len(numbers) >= 2:
                    try:
                        max_price = int(numbers[1].replace(',', ''))
                        if max_price <= value:
                            new_filtered.append(m)
                    except ValueError:
                        pass
            filtered = new_filtered
        elif key == 'min_year':
            filtered = [m for m in filtered if m['model_year'] >= value]
        elif key == 'category':
            filtered = [m for m in filtered if m['category'] == value]
    
    return filtered

def main():
    """Main demonstration function"""
    # Load the database
    try:
        data = load_taiwan_database()
        motorcycles = data['motorcycles']
    except FileNotFoundError:
        print("Error: taiwan_specific_motorcycles.json not found!")
        print("Please run generate_taiwan_specific_database.py first.")
        return
    
    # Perform analysis
    analyze_database(data)
    
    # Run example queries
    example_queries(motorcycles)
    
    # Demonstrate filtering
    print("=== Custom Filtering Examples ===")
    
    # Find affordable Yamaha scooters
    print("Affordable Yamaha scooters under NT$ 100,000:")
    yamaha_scooters = filter_by_criteria(
        motorcycles, 
        brand='YAMAHA', 
        max_price=100000
    )
    yamaha_scooters = [m for m in yamaha_scooters if 'Scooter' in m['type']]
    
    for bike in yamaha_scooters[:3]:
        print(f"  • {bike['model']} - {bike['price_range']}")
        print(f"    Features: {', '.join(bike['features'][:3])}")
    print(f"  Total found: {len(yamaha_scooters)}")
    print()
    
    # Find new electric vehicles
    print("Latest electric vehicles (2023+):")
    new_electric = filter_by_criteria(
        motorcycles,
        min_year=2023
    )
    new_electric = [m for m in new_electric if m['engine']['displacement'] == 'Electric Motor']
    
    for bike in new_electric[:3]:
        print(f"  • {bike['brand']} {bike['model']} ({bike['model_year']})")
        battery = bike.get('battery_capacity', 'N/A')
        range_km = bike.get('range', 'N/A')
        print(f"    Battery: {battery}, Range: {range_km}")
    print(f"  Total found: {len(new_electric)}")
    print()
    
    print("=== Database Ready for Use! ===")
    print("The Taiwan motorcycle database contains comprehensive data")
    print("covering all major brands, vehicle types, and price ranges")
    print("suitable for the Taiwan market.")

if __name__ == "__main__":
    main()