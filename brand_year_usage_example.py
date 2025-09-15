#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage example for Taiwan Motorcycle Database (Brand/Year/Model Structure)
Demonstrates how to query and analyze the organized motorcycle data
"""

import json
from collections import defaultdict, Counter

def load_database():
    """Load the brand/year organized motorcycle database"""
    with open('taiwan_motorcycles_by_brand_year.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def get_brand_models_by_year(data, brand, year):
    """Get all models for a specific brand in a specific year"""
    try:
        return data['brands'][brand]['years'][str(year)]['models']
    except KeyError:
        return []

def get_all_models_by_brand(data, brand):
    """Get all models for a specific brand across all years"""
    models = []
    if brand in data['brands']:
        for year_data in data['brands'][brand]['years'].values():
            models.extend(year_data['models'])
    return models

def get_models_by_year(data, year):
    """Get all models from all brands in a specific year"""
    models = []
    for brand_data in data['brands'].values():
        if str(year) in brand_data['years']:
            models.extend(brand_data['years'][str(year)]['models'])
    return models

def get_available_models(data):
    """Get all currently available models across all brands and years"""
    available_models = []
    for brand_name, brand_data in data['brands'].items():
        for year, year_data in brand_data['years'].items():
            for model in year_data['models']:
                if model['availability'] == 'Available':
                    model_copy = model.copy()
                    model_copy['brand'] = brand_name
                    available_models.append(model_copy)
    return available_models

def get_electric_models(data):
    """Get all electric motorcycle models"""
    electric_models = []
    for brand_name, brand_data in data['brands'].items():
        for year, year_data in brand_data['years'].items():
            for model in year_data['models']:
                if (model['engine'].get('displacement') == 'Electric Motor' or 
                    model['type'] == 'Electric'):
                    model_copy = model.copy()
                    model_copy['brand'] = brand_name
                    electric_models.append(model_copy)
    return electric_models

def get_price_range_models(data, min_price, max_price):
    """Get models within a specific price range (in NT$)"""
    models_in_range = []
    for brand_name, brand_data in data['brands'].items():
        for year, year_data in brand_data['years'].items():
            for model in year_data['models']:
                price_str = model['price_range']
                # Extract minimum price from range string like "NT$ 48,895 - 69,850"
                try:
                    price_parts = price_str.split(' - ')
                    min_model_price = int(price_parts[0].replace('NT$ ', '').replace(',', ''))
                    max_model_price = int(price_parts[1].replace(',', ''))
                    
                    if min_model_price >= min_price and max_model_price <= max_price:
                        model_copy = model.copy()
                        model_copy['brand'] = brand_name
                        models_in_range.append(model_copy)
                except (ValueError, IndexError):
                    continue
    return models_in_range

def analyze_brand_statistics(data):
    """Analyze statistics for each brand"""
    stats = {}
    for brand_name, brand_data in data['brands'].items():
        total_models = 0
        displacement_counter = Counter()
        type_counter = Counter()
        availability_counter = Counter()
        
        for year, year_data in brand_data['years'].items():
            total_models += len(year_data['models'])
            for model in year_data['models']:
                displacement_counter[model['engine']['displacement']] += 1
                type_counter[model['type']] += 1
                availability_counter[model['availability']] += 1
        
        stats[brand_name] = {
            'total_models': total_models,
            'country_of_origin': brand_data['country_of_origin'],
            'most_common_displacement': displacement_counter.most_common(1)[0] if displacement_counter else None,
            'most_common_type': type_counter.most_common(1)[0] if type_counter else None,
            'availability_breakdown': dict(availability_counter)
        }
    
    return stats

def main():
    """Demonstrate usage of the brand/year organized motorcycle database"""
    print("Taiwan Motorcycle Database - Usage Examples")
    print("=" * 50)
    
    # Load database
    data = load_database()
    print(f"Database loaded: {data['title']}")
    print(f"Years covered: {data['years_covered']}")
    print(f"Brands included: {len(data['brands'])}")
    print()
    
    # Example 1: Get all Yamaha models in 2024
    print("Example 1: Yamaha models in 2024")
    yamaha_2024 = get_brand_models_by_year(data, 'Yamaha', 2024)
    print(f"Found {len(yamaha_2024)} Yamaha models in 2024:")
    for model in yamaha_2024[:3]:  # Show first 3
        print(f"  - {model['model']} ({model['engine']['displacement']}, {model['type']})")
    print()
    
    # Example 2: Get all Honda models across all years
    print("Example 2: Honda models (all years)")
    honda_all = get_all_models_by_brand(data, 'Honda')
    print(f"Found {len(honda_all)} Honda models total")
    print()
    
    # Example 3: Get all available models
    print("Example 3: Currently available models")
    available = get_available_models(data)
    print(f"Found {len(available)} currently available models")
    
    # Group by brand
    available_by_brand = defaultdict(int)
    for model in available:
        available_by_brand[model['brand']] += 1
    
    print("Available models by brand:")
    for brand, count in sorted(available_by_brand.items()):
        print(f"  - {brand}: {count} models")
    print()
    
    # Example 4: Electric motorcycles
    print("Example 4: Electric motorcycles")
    electric = get_electric_models(data)
    print(f"Found {len(electric)} electric models:")
    for model in electric[:5]:  # Show first 5
        print(f"  - {model['brand']} {model['model']} ({model['year']})")
    print()
    
    # Example 5: Budget motorcycles (under NT$ 100,000)
    print("Example 5: Budget motorcycles (under NT$ 100,000)")
    budget = get_price_range_models(data, 0, 100000)
    print(f"Found {len(budget)} budget-friendly models:")
    for model in budget[:5]:  # Show first 5
        print(f"  - {model['brand']} {model['model']} - {model['price_range']}")
    print()
    
    # Example 6: Brand statistics
    print("Example 6: Brand statistics")
    stats = analyze_brand_statistics(data)
    
    print("Brand overview:")
    for brand, stat in stats.items():
        print(f"\n{brand} ({stat['country_of_origin']}):")
        print(f"  Total models: {stat['total_models']}")
        if stat['most_common_displacement']:
            print(f"  Most common displacement: {stat['most_common_displacement'][0]} ({stat['most_common_displacement'][1]} models)")
        if stat['most_common_type']:
            print(f"  Most common type: {stat['most_common_type'][0]} ({stat['most_common_type'][1]} models)")
        print(f"  Availability: {stat['availability_breakdown']}")
    
    # Example 7: Year-over-year comparison
    print("\nExample 7: Model count by year")
    year_counts = {}
    for year in range(2015, 2025):
        year_models = get_models_by_year(data, year)
        year_counts[year] = len(year_models)
    
    print("Models introduced by year:")
    for year, count in year_counts.items():
        print(f"  {year}: {count} models")
    
    print(f"\nTotal unique models in database: {sum(year_counts.values())}")

if __name__ == "__main__":
    main()