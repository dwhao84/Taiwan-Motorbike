#!/usr/bin/env python3
"""
Taiwan Motorcycle Database Validation Script

This script validates that the generated Taiwan-specific motorcycle database
meets all the requirements specified in the problem statement.
"""

import json
import re
from collections import Counter

def load_database(filename='taiwan_specific_motorcycles.json'):
    """Load the Taiwan motorcycle database"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_database(data):
    """Validate the database meets all requirements"""
    motorcycles = data['motorcycles']
    total_entries = len(motorcycles)
    
    print("=== Taiwan Motorcycle Database Validation ===")
    print(f"Total entries: {total_entries}")
    print(f"Target: 2000+ entries - {'✓ PASS' if total_entries >= 2000 else '✗ FAIL'}")
    print()
    
    # Validate brands
    required_brands = {
        'SYM', 'KYMCO', 'PGO', 'AEON',  # Taiwan brands
        'YAMAHA', 'HONDA', 'SUZUKI', 'KAWASAKI',  # International brands
        'GOGORO'  # Electric brand
    }
    
    brands = set(m['brand'] for m in motorcycles)
    brand_counts = Counter(m['brand'] for m in motorcycles)
    
    print("Brand Coverage:")
    for brand in required_brands:
        if brand in brands:
            print(f"  ✓ {brand}: {brand_counts[brand]} entries")
        else:
            print(f"  ✗ {brand}: Missing")
    print(f"Total brands: {len(brands)}")
    print()
    
    # Validate required fields
    required_fields = [
        'brand', 'model', 'model_english', 'model_year', 'type',
        'engine', 'features', 'price_range', 'fuel_efficiency',
        'weight', 'seat_height', 'availability', 'category', 'target_audience'
    ]
    
    print("Required Fields Validation:")
    field_coverage = {}
    for field in required_fields:
        count = sum(1 for m in motorcycles if field in m and m[field] is not None)
        coverage = (count / total_entries) * 100
        field_coverage[field] = coverage
        status = "✓ PASS" if coverage >= 95 else "✗ FAIL"
        print(f"  {field}: {coverage:.1f}% coverage {status}")
    print()
    
    # Validate engine sub-fields
    print("Engine Fields Validation:")
    engine_fields = ['displacement', 'type', 'power']
    for field in engine_fields:
        count = sum(1 for m in motorcycles if 'engine' in m and field in m['engine'])
        coverage = (count / total_entries) * 100
        status = "✓ PASS" if coverage >= 95 else "✗ FAIL"
        print(f"  engine.{field}: {coverage:.1f}% coverage {status}")
    print()
    
    # Validate year range (2020-2025)
    years = [m['model_year'] for m in motorcycles if 'model_year' in m]
    year_range = (min(years), max(years)) if years else (None, None)
    print(f"Year Range: {year_range}")
    target_years = set(range(2020, 2026))
    actual_years = set(years)
    missing_years = target_years - actual_years
    if not missing_years:
        print("  ✓ PASS: All years 2020-2025 covered")
    else:
        print(f"  ✗ FAIL: Missing years {missing_years}")
    print()
    
    # Validate displacement categories
    print("Displacement Categories:")
    displacement_categories = {
        '50cc級距': (50, 80),
        '100cc級距': (90, 110),
        '125cc級距': (120, 150),
        '150cc級距': (150, 180),
        '200cc級距': (200, 300),
        '重機級距': (300, 2000),
        '電動車': (0, 0)  # Electric
    }
    
    for category, (min_cc, max_cc) in displacement_categories.items():
        if category == '電動車':
            count = sum(1 for m in motorcycles if m['engine']['displacement'] == 'Electric Motor')
        else:
            count = 0
            for m in motorcycles:
                disp_str = m['engine']['displacement']
                if 'cc' in disp_str:
                    try:
                        cc = int(disp_str.replace('cc', ''))
                        if min_cc <= cc <= max_cc:
                            count += 1
                    except ValueError:
                        pass
        
        print(f"  {category}: {count} entries")
    print()
    
    # Validate vehicle types
    print("Vehicle Type Distribution:")
    types = Counter(m['type'] for m in motorcycles)
    required_types = [
        'Urban Scooter', 'Sport Scooter', 'Maxi Scooter', 'Classic Scooter',
        'Sport Bike', 'Naked Bike', 'Electric Scooter'
    ]
    
    for vtype in required_types:
        count = types.get(vtype, 0)
        status = "✓" if count > 0 else "✗"
        print(f"  {status} {vtype}: {count}")
    print()
    
    # Validate price ranges
    print("Price Range Validation:")
    price_ranges = []
    for m in motorcycles:
        if 'price_range' in m and m['price_range']:
            price_str = m['price_range']
            # Extract numbers from "NT$ 123,456 - 234,567" format
            numbers = re.findall(r'[\d,]+', price_str)
            if len(numbers) >= 2:
                try:
                    min_price = int(numbers[0].replace(',', ''))
                    max_price = int(numbers[1].replace(',', ''))
                    price_ranges.append((min_price, max_price))
                except ValueError:
                    pass
    
    if price_ranges:
        all_prices = [p for pair in price_ranges for p in pair]
        min_price = min(all_prices)
        max_price = max(all_prices)
        print(f"  Price range: NT$ {min_price:,} - NT$ {max_price:,}")
        print(f"  Entries with valid prices: {len(price_ranges)}")
        
        # Check if covers required range (50,000 to 1,000,000+)
        covers_entry = min_price <= 80000
        covers_premium = max_price >= 500000
        print(f"  ✓ Covers entry level (<80k): {covers_entry}")
        print(f"  ✓ Covers premium (>500k): {covers_premium}")
    print()
    
    # Validate electric vehicle features
    print("Electric Vehicle Validation:")
    electric_bikes = [m for m in motorcycles if m['engine']['displacement'] == 'Electric Motor']
    print(f"  Electric motorcycles: {len(electric_bikes)}")
    
    electric_with_battery = sum(1 for m in electric_bikes if 'battery_capacity' in m)
    electric_with_range = sum(1 for m in electric_bikes if 'range' in m)
    
    print(f"  With battery capacity: {electric_with_battery}")
    print(f"  With range specification: {electric_with_range}")
    print()
    
    # Market categories validation
    print("Market Categories:")
    categories = Counter(m['category'] for m in motorcycles if 'category' in m)
    for category, count in categories.most_common():
        print(f"  {category}: {count}")
    print()
    
    # Target audience validation
    print("Target Audiences:")
    audiences = Counter(m['target_audience'] for m in motorcycles if 'target_audience' in m)
    for audience, count in audiences.most_common():
        print(f"  {audience}: {count}")
    print()
    
    # Generate summary
    print("=== VALIDATION SUMMARY ===")
    total_checks = 0
    passed_checks = 0
    
    # Basic checks
    if total_entries >= 2000:
        passed_checks += 1
    total_checks += 1
    
    # Brand checks
    for brand in required_brands:
        if brand in brands:
            passed_checks += 1
        total_checks += 1
    
    # Field coverage checks
    for field, coverage in field_coverage.items():
        if coverage >= 95:
            passed_checks += 1
        total_checks += 1
    
    # Year coverage check
    if not missing_years:
        passed_checks += 1
    total_checks += 1
    
    success_rate = (passed_checks / total_checks) * 100
    print(f"Validation Score: {passed_checks}/{total_checks} ({success_rate:.1f}%)")
    
    if success_rate >= 90:
        print("🎉 Database validation PASSED! Ready for use.")
    elif success_rate >= 75:
        print("⚠️  Database validation partially passed. Some issues need attention.")
    else:
        print("❌ Database validation FAILED. Significant issues need fixing.")
    
    return success_rate >= 90

def main():
    """Main validation function"""
    try:
        data = load_database()
        validate_database(data)
    except FileNotFoundError:
        print("Error: taiwan_specific_motorcycles.json not found!")
        print("Please run generate_taiwan_specific_database.py first.")
    except Exception as e:
        print(f"Error during validation: {e}")

if __name__ == "__main__":
    main()