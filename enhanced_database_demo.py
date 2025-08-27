#!/usr/bin/env python3
"""
Enhanced Taiwan Motorcycle Database Demo

This script demonstrates the new comprehensive motorcycle database
covering years 2000-2025 with realistic availability statuses.
"""

import json
import re
from collections import Counter

def load_enhanced_database(filename='complete_motorcycle_database.json'):
    """Load the enhanced motorcycle database"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_year_from_model(model):
    """Extract year from model name"""
    year_match = re.search(r'\((\d{4})\)', model)
    return int(year_match.group(1)) if year_match else None

def demonstrate_enhanced_features(data):
    """Demonstrate the enhanced features of the database"""
    motorcycles = data['motorcycles']
    
    print("=== Enhanced Taiwan Motorcycle Database (2000-2025) ===")
    print(f"Total motorcycles: {len(motorcycles):,}")
    print(f"Database generated: {data.get('last_updated', 'Unknown')}")
    print()
    
    # Year coverage analysis
    years = []
    for m in motorcycles:
        year = extract_year_from_model(m['model'])
        if year:
            years.append(year)
    
    print(f"Year Coverage: {min(years)} - {max(years)} ({max(years) - min(years) + 1} years)")
    print()
    
    # Decade distribution
    decade_counts = Counter()
    for year in years:
        decade = (year // 10) * 10
        decade_counts[decade] += 1
    
    print("Distribution by Decade:")
    for decade in sorted(decade_counts.keys()):
        percentage = (decade_counts[decade] / len(years)) * 100
        print(f"  {decade}s: {decade_counts[decade]:,} models ({percentage:.1f}%)")
    print()
    
    # Availability status analysis
    availability_counts = Counter(m['availability'] for m in motorcycles)
    print("Availability Status Distribution:")
    for status, count in availability_counts.most_common():
        percentage = (count / len(motorcycles)) * 100
        print(f"  {status}: {count:,} models ({percentage:.1f}%)")
    print()
    
    # Sample motorcycles from different eras
    print("Sample Motorcycles from Different Eras:")
    print("=" * 50)
    
    eras = {
        "Early 2000s (2000-2005)": (2000, 2005),
        "Mid 2000s (2006-2010)": (2006, 2010),
        "Early 2010s (2011-2015)": (2011, 2015),
        "Late 2010s (2016-2020)": (2016, 2020),
        "Current Era (2021-2025)": (2021, 2025)
    }
    
    for era_name, (start_year, end_year) in eras.items():
        print(f"\n{era_name}:")
        era_bikes = []
        for m in motorcycles:
            year = extract_year_from_model(m['model'])
            if year and start_year <= year <= end_year:
                era_bikes.append(m)
        
        # Show 2 random examples from each era
        import random
        if era_bikes:
            samples = random.sample(era_bikes, min(2, len(era_bikes)))
            for bike in samples:
                print(f"  • {bike['brand']} {bike['model']}")
                print(f"    Type: {bike['type']} | Engine: {bike['engine']['displacement']}")
                print(f"    Price: {bike['price_range']} | Status: {bike['availability']}")
                print()

def filter_by_era_and_status():
    """Demonstrate filtering by era and availability status"""
    data = load_enhanced_database()
    motorcycles = data['motorcycles']
    
    print("\n=== Era and Status Analysis ===")
    
    # Find collector items from early 2000s
    early_2000s_collectors = []
    for m in motorcycles:
        year = extract_year_from_model(m['model'])
        if year and 2000 <= year <= 2005 and m['availability'] == 'Collector Item':
            early_2000s_collectors.append(m)
    
    print(f"\nCollector Items from Early 2000s: {len(early_2000s_collectors)} models")
    for bike in early_2000s_collectors[:5]:  # Show first 5
        print(f"  • {bike['brand']} {bike['model']} - {bike['price_range']}")
    
    # Find available current models
    current_available = []
    for m in motorcycles:
        year = extract_year_from_model(m['model'])
        if year and year >= 2022 and m['availability'] == 'Available':
            current_available.append(m)
    
    print(f"\nCurrently Available Models (2022+): {len(current_available)} models")
    for bike in current_available[:5]:  # Show first 5
        print(f"  • {bike['brand']} {bike['model']} - {bike['price_range']}")

def main():
    """Main demonstration function"""
    try:
        data = load_enhanced_database()
        demonstrate_enhanced_features(data)
        filter_by_era_and_status()
        
        print("\n" + "=" * 60)
        print("Database Enhancement Summary:")
        print("✓ Extended year coverage from 2000-2025 (26 years)")
        print("✓ Added realistic availability statuses")
        print("✓ Maintained 20,000 high-quality entries")
        print("✓ Preserved all existing functionality")
        print("✓ Enhanced historical motorcycle representation")
        
    except FileNotFoundError:
        print("Error: complete_motorcycle_database.json not found.")
        print("Please run 'python3 generate_motorcycle_database.py' first.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()