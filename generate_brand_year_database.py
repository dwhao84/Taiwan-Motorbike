#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Taiwan Motorcycle Database organized by Brand → Year → Models
For the past 10 years (2015-2024) of Taiwan motorcycle market
"""

import json
import random
from datetime import datetime

def generate_brand_year_database():
    """Generate comprehensive motorcycle database organized by brand/year/model structure"""
    
    # Brand definitions with their characteristics
    brands_info = {
        "Yamaha": {
            "country": "Japan",
            "popular_categories": ["Sport Scooter", "Sport Bike", "Classic Scooter"],
            "price_premium": 1.1,
            "popular_models": ["Vino", "Jog", "勁戰", "Force", "SMAX", "YZF-R", "MT", "TMAX"]
        },
        "Honda": {
            "country": "Japan", 
            "popular_categories": ["Sport Scooter", "Naked Bike", "Classic Scooter"],
            "price_premium": 1.15,
            "popular_models": ["PCX", "Vario", "CB", "CBR", "Forza", "Lead", "Click"]
        },
        "SYM": {
            "country": "Taiwan",
            "popular_categories": ["Sport Scooter", "Maxi Scooter", "Urban Scooter"],
            "price_premium": 0.85,
            "popular_models": ["迪爵", "活力", "DRG", "Jet", "MAXSYM", "Woo", "JET SL+", "CLBCU"]
        },
        "Kymco": {
            "country": "Taiwan",
            "popular_categories": ["Sport Scooter", "Maxi Scooter", "Electric"],
            "price_premium": 0.9,
            "popular_models": ["大地名流", "GP", "Racing S", "AK", "iONEX", "新豪邁", "Many", "VJR"]
        },
        "PGO": {
            "country": "Taiwan",
            "popular_categories": ["Sport Scooter", "Electric", "Urban Scooter"],
            "price_premium": 0.8,
            "popular_models": ["Ur1", "J-bubu", "Tigra", "BON", "Alpha Max"]
        },
        "Suzuki": {
            "country": "Japan",
            "popular_categories": ["Sport Bike", "Naked Bike", "Adventure"],
            "price_premium": 1.05,
            "popular_models": ["GSX", "V-Strom", "SV", "Katana", "Address", "Burgman"]
        },
        "Vespa": {
            "country": "Italy",
            "popular_categories": ["Classic Scooter", "Premium Scooter"],
            "price_premium": 1.8,
            "popular_models": ["Primavera", "Sprint", "GTS", "LX", "S"]
        },
        "CPI": {
            "country": "Taiwan",
            "popular_categories": ["Sport Scooter", "Urban Scooter"],
            "price_premium": 0.7,
            "popular_models": ["GTR", "Formula", "Hussar", "Aragon"]
        },
        "Hartford": {
            "country": "Taiwan", 
            "popular_categories": ["Cruiser", "Touring"],
            "price_premium": 0.75,
            "popular_models": ["VR", "HD", "Touring"]
        },
        "Kawasaki": {
            "country": "Japan",
            "popular_categories": ["Sport Bike", "Naked Bike", "Adventure"],
            "price_premium": 1.2,
            "popular_models": ["Ninja", "Z", "Versys", "W", "ER"]
        }
    }
    
    # Engine configurations by displacement range
    engine_configs = {
        50: {"power_range": (3, 5), "type": "4-stroke, air-cooled", "fuel_type": "Gasoline"},
        110: {"power_range": (6, 8), "type": "4-stroke, air-cooled", "fuel_type": "Gasoline"},
        125: {"power_range": (8, 12), "type": "4-stroke, air-cooled", "fuel_type": "Gasoline"},
        150: {"power_range": (11, 15), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        158: {"power_range": (13, 16), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        200: {"power_range": (15, 22), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        250: {"power_range": (20, 30), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        300: {"power_range": (28, 35), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        400: {"power_range": (35, 50), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        500: {"power_range": (45, 65), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        650: {"power_range": (55, 80), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"},
        1000: {"power_range": (100, 150), "type": "4-stroke, liquid-cooled", "fuel_type": "Gasoline"}
    }
    
    # Base pricing by displacement (NT$)
    base_pricing = {
        50: (35000, 50000),
        110: (50000, 70000),
        125: (65000, 90000),
        150: (85000, 120000),
        158: (90000, 130000),
        200: (120000, 160000),
        250: (160000, 220000),
        300: (180000, 250000),
        400: (220000, 320000),
        500: (300000, 450000),
        650: (400000, 600000),
        1000: (600000, 1200000)
    }
    
    # Common features by category
    features_by_category = {
        "Sport Scooter": ["LED lighting", "Digital display", "Under-seat storage", "Disc brakes", "Telescopic forks"],
        "Classic Scooter": ["Retro styling", "Chrome accents", "Comfortable seating", "Easy maintenance"],
        "Sport Bike": ["Racing-inspired design", "6-speed transmission", "ABS", "Slipper clutch", "USD forks"],
        "Naked Bike": ["Upright riding position", "LED lighting", "Digital display", "Easy handling"],
        "Maxi Scooter": ["Large storage space", "Windscreen", "Comfortable touring", "Automatic CVT"],
        "Electric": ["Zero emissions", "Silent operation", "Quick charging", "Digital connectivity", "Regenerative braking"],
        "Urban Scooter": ["Fuel efficient", "Compact design", "Easy parking", "Affordable maintenance"],
        "Premium Scooter": ["Premium materials", "Advanced features", "Luxury styling", "High build quality"],
        "Cruiser": ["Low seat height", "Forward controls", "Classic styling", "Comfortable cruising"],
        "Touring": ["Large fuel tank", "Comfortable seating", "Wind protection", "Storage capacity"],
        "Adventure": ["Off-road capability", "Long travel suspension", "Rugged design", "Large fuel tank"]
    }
    
    # Generate the database structure
    database = {
        "title": "Taiwan Motorcycle Database - Brand/Year/Model Structure",
        "description": "Comprehensive motorcycle database organized by brand, year, and model for Taiwan market (2015-2024)",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "structure": "Brand → Year → Models",
        "years_covered": "2015-2024 (10 years)",
        "brands": {}
    }
    
    # Generate data for each brand
    for brand_name, brand_info in brands_info.items():
        database["brands"][brand_name] = {
            "country_of_origin": brand_info["country"],
            "years": {}
        }
        
        # Generate data for each year (2015-2024)
        for year in range(2015, 2025):
            database["brands"][brand_name]["years"][str(year)] = {
                "models": []
            }
            
            # Determine number of models for this brand/year (varies by brand popularity)
            if brand_name in ["Yamaha", "Honda", "SYM", "Kymco"]:
                num_models = random.randint(8, 15)  # Major brands
            elif brand_name in ["Suzuki", "Kawasaki"]:
                num_models = random.randint(5, 10)  # International brands
            else:
                num_models = random.randint(3, 8)   # Smaller brands
            
            # Generate models for this year
            used_model_names = set()
            for _ in range(num_models):
                model_name = generate_model_name(brand_info["popular_models"], used_model_names, year)
                used_model_names.add(model_name)
                
                # Determine displacement and category
                displacement = random.choice([50, 110, 125, 150, 158, 200, 250, 300, 400, 500, 650, 1000])
                category = random.choice(brand_info["popular_categories"])
                
                # Special handling for electric models
                if category == "Electric":
                    engine_spec = {
                        "displacement": "Electric Motor",
                        "type": "Electric motor with lithium battery",
                        "power": f"{random.randint(3, 15)} hp equivalent",
                        "battery_capacity": f"{random.randint(20, 80)} Ah",
                        "range": f"{random.randint(80, 200)} km"
                    }
                    price_range = (80000, 150000)
                else:
                    engine_config = engine_configs[displacement]
                    power = random.randint(engine_config["power_range"][0], engine_config["power_range"][1])
                    engine_spec = {
                        "displacement": f"{displacement}cc",
                        "type": engine_config["type"],
                        "power": f"{power} hp"
                    }
                    price_range = base_pricing[displacement]
                
                # Calculate price with brand premium
                base_min, base_max = price_range
                premium = brand_info["price_premium"]
                final_min = int(base_min * premium)
                final_max = int(base_max * premium)
                
                # Add year-based pricing adjustment (newer = more expensive)
                year_factor = 1 + ((year - 2015) * 0.03)  # 3% increase per year
                final_min = int(final_min * year_factor)
                final_max = int(final_max * year_factor)
                
                # Generate features
                base_features = features_by_category.get(category, ["Standard features"])
                features = random.sample(base_features, min(len(base_features), random.randint(3, 6)))
                
                # Determine availability based on year
                if year >= 2022:
                    availability = "Available"
                elif year >= 2019:
                    availability = random.choice(["Available", "Limited Availability"])
                elif year >= 2016:
                    availability = random.choice(["Limited Availability", "Discontinued"])
                else:
                    availability = random.choice(["Discontinued", "Used Market Only"])
                
                # Create model entry
                model = {
                    "model": model_name,
                    "year": year,
                    "type": category,
                    "engine": engine_spec,
                    "features": features,
                    "price_range": f"NT$ {final_min:,} - {final_max:,}",
                    "availability": availability,
                    "market_segment": determine_market_segment(displacement if category != "Electric" else 125)
                }
                
                database["brands"][brand_name]["years"][str(year)]["models"].append(model)
    
    return database

def generate_model_name(popular_models, used_names, year):
    """Generate a unique model name for the given year"""
    base_name = random.choice(popular_models)
    
    # Add variations
    variations = ["", " ABS", " DX", " Sport", " Touring", " Limited", " SE", " Pro", " Plus", " Max"]
    displacement_suffixes = ["50", "110", "125", "150", "158", "200", "250", "300", "400", "500"]
    
    # Try different combinations until we get a unique name
    attempts = 0
    while attempts < 20:
        if random.random() < 0.6:  # 60% chance to add displacement
            suffix = random.choice(displacement_suffixes)
            name = f"{base_name} {suffix}"
        else:
            name = base_name
        
        if random.random() < 0.3:  # 30% chance to add variation
            variation = random.choice(variations)
            name += variation
        
        # Add year for newer models sometimes
        if year >= 2020 and random.random() < 0.2:
            name += f" ({year})"
        
        if name not in used_names:
            return name
            
        attempts += 1
    
    # Fallback: use base name with year
    return f"{base_name} {year}"

def determine_market_segment(displacement):
    """Determine market segment based on displacement"""
    if displacement <= 50:
        return "Entry Level"
    elif displacement <= 125:
        return "Urban Commuter" 
    elif displacement <= 200:
        return "Sport/Touring"
    elif displacement <= 400:
        return "Mid-Range Sport"
    else:
        return "Premium/Touring"

def main():
    """Generate and save the brand/year organized motorcycle database"""
    print("Generating Taiwan Motorcycle Database (Brand/Year/Model Structure)...")
    
    # Generate the database
    database = generate_brand_year_database()
    
    # Calculate statistics
    total_models = 0
    for brand_name, brand_data in database["brands"].items():
        brand_total = 0
        for year, year_data in brand_data["years"].items():
            brand_total += len(year_data["models"])
        total_models += brand_total
        print(f"{brand_name}: {brand_total} models")
    
    print(f"\nTotal models generated: {total_models}")
    
    # Save to JSON file
    output_file = "taiwan_motorcycles_by_brand_year.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)
    
    print(f"\nDatabase saved to: {output_file}")
    print("Structure: Brand → Year (2015-2024) → Models")

if __name__ == "__main__":
    main()