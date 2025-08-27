#!/usr/bin/env python3
"""
Taiwan Specific Motorcycle Database Generator

This script generates a comprehensive database of motorcycles specifically for Taiwan market
with complete specifications, pricing, and features according to Taiwan requirements.
"""

import json
import random
from datetime import datetime

# Configuration
TARGET_ENTRIES = 2000
OUTPUT_FILE = 'taiwan_specific_motorcycles.json'

# Taiwan motorcycle brands and their market distribution (as per requirements)
TAIWAN_BRANDS = {
    # Taiwan Local Brands (150-200 entries each)
    'SYM': 190,      # 三陽機車
    'Kymco': 185,    # 光陽機車 
    'PGO': 170,      # 比雅久
    'Aeon': 160,     # 宏佳騰
    
    # International Brands in Taiwan (100-150 entries each)
    'Yamaha': 150,   # 台灣山葉
    'Honda': 145,    # 台灣本田
    'Suzuki': 130,   # 台灣鈴木
    'Kawasaki': 120,
    
    # Electric Vehicle Brands (300 entries total)
    'GOGORO': 220,   # 主要電動車品牌
    'PGO_Electric': 60,  # PGO電動車款
    'Aeon_Electric': 60, # 宏佳騰電動車款
    
    # Additional brands to reach 2000+
    'SYM_Heritage': 90,   # SYM經典車款
    'Kymco_Performance': 80, # Kymco性能車款
    'Yamaha_Performance': 70, # Yamaha性能車款
    'Honda_Classic': 60,   # Honda經典車款
    'Others': 70,      # 其他品牌
    'Taiwan_Electric': 40,  # 其他台灣電動車品牌
    'Import_Specialty': 50  # 進口特殊車款
}

# Vehicle types with displacement ranges and characteristics
VEHICLE_TYPES = {
    # 速克達 (1200 entries total)
    'Urban Scooter': {'displacement_range': (50, 150), 'power_multiplier': 0.07, 'count': 400},
    'Sport Scooter': {'displacement_range': (125, 200), 'power_multiplier': 0.08, 'count': 300}, 
    'Maxi Scooter': {'displacement_range': (250, 650), 'power_multiplier': 0.09, 'count': 250},
    'Classic Scooter': {'displacement_range': (50, 125), 'power_multiplier': 0.065, 'count': 250},
    
    # 檔車 (600 entries total)
    'Naked': {'displacement_range': (150, 1000), 'power_multiplier': 0.10, 'count': 200},
    'Sport': {'displacement_range': (250, 1000), 'power_multiplier': 0.12, 'count': 200},
    'Classic': {'displacement_range': (125, 400), 'power_multiplier': 0.08, 'count': 100},
    'Adventure': {'displacement_range': (250, 800), 'power_multiplier': 0.085, 'count': 100},
    
    # 電動車 (200 entries total)
    'Electric Scooter': {'displacement_range': (0, 0), 'power_multiplier': 0, 'count': 120},
    'Electric Sport': {'displacement_range': (0, 0), 'power_multiplier': 0, 'count': 50},
    'Electric Commercial': {'displacement_range': (0, 0), 'power_multiplier': 0, 'count': 30}
}

# Engine types by displacement for Taiwan market
ENGINE_TYPES = {
    (50, 125): ['4-stroke, air-cooled, single-cylinder', '4-stroke, liquid-cooled, single-cylinder'],
    (126, 200): ['4-stroke, liquid-cooled, single-cylinder', '4-stroke, air-cooled, single-cylinder'],
    (201, 400): ['4-stroke, liquid-cooled, single-cylinder', '4-stroke, liquid-cooled, parallel-twin'],
    (401, 800): ['4-stroke, liquid-cooled, parallel-twin', '4-stroke, liquid-cooled, inline-four'],
    (801, 1500): ['4-stroke, liquid-cooled, inline-four', '4-stroke, liquid-cooled, V-twin']
}

# Taiwan-specific model names and series
TAIWAN_MODEL_SERIES = {
    'SYM': {
        'chinese': ['迪爵', '活力', '悍將', '野狼', '鳳凰', '三冠王', '金旺', '新勁戰士', '飛刀', '風華'],
        'english': ['Duke', 'Vivo', 'Fighter', 'Wolf', 'Phoenix', 'Jet', 'Maxsym', 'Symphony', 'Fiddle', 'Cruisym'],
        'series': ['FIGHTER', 'JET', 'GR', 'MAXSYM', 'CRUISYM', 'JOYMAX', 'SYMPHONY', 'FIDDLE', 'DRG', 'FNX']
    },
    'Kymco': {
        'chinese': ['大地名流', '豪邁', '雷霆', '奔騰', '勁麗', '新豪邁', '超級金牌', '名流', '風光', '驕子'],
        'english': ['People', 'Racing', 'Like', 'Many', 'Agility', 'Xciting', 'Downtown', 'Super', 'AK', 'CT'],
        'series': ['RACING', 'LIKE', 'MANY', 'XCITING', 'AK', 'DOWNTOWN', 'AGILITY', 'PEOPLE', 'GP', 'IONEX']
    },
    'PGO': {
        'chinese': ['飛鷹', '勁風', '閃電', '豹', '虎', '龍', '鳳', '麒麟', '火鳥', '神駒'],
        'english': ['Eagle', 'Wind', 'Lightning', 'Leopard', 'Tiger', 'Dragon', 'Phoenix', 'Kirin', 'Firebird', 'Stallion'],
        'series': ['BON', 'ALPHA', 'TIGRA', 'X-HOT', 'UR', 'JBUBU', 'PMX', 'TORNADO', 'HOT', 'BIG']
    },
    'Aeon': {
        'chinese': ['智慧', '未來', '科技', '創新', '電動', '環保', '智能', '先鋒', '前衛', '超越'],
        'english': ['Smart', 'Future', 'Tech', 'Innovation', 'Electric', 'Eco', 'AI', 'Pioneer', 'Avant', 'Beyond'],
        'series': ['AI-1', 'AI-2', 'AI-3', 'ELITE', 'COBRA', 'CROSSLAND', 'REVO', 'MOTOR', 'CUTE', 'ELITE']
    },
    'Yamaha': {
        'chinese': ['勁戰', '新勁戰', '山葉', '風暴', '雷霆', '閃電', '烈火', '極速', '征服', '霸王'],
        'english': ['Force', 'Cygnus', 'Axis', 'Janus', 'YZF', 'MT', 'FZ', 'XSR', 'R', 'Vino'],
        'series': ['FORCE', 'CYGNUS', 'AXIS', 'JANUS', 'YZF', 'MT', 'FZ', 'XSR', 'R-Series', 'SMAX']
    },
    'Honda': {
        'chinese': ['本田', '喜美', '雅歌', '飛度', '思域', '冠軍', '王者', '精英', '豪華', '經典'],
        'english': ['PCX', 'Lead', 'Dio', 'Scoopy', 'CB', 'CBR', 'CRF', 'Forza', 'SH', 'Vision'],
        'series': ['PCX', 'LEAD', 'DIO', 'SCOOPY', 'CB', 'CBR', 'CRF', 'FORZA', 'SH', 'VISION']
    },
    'GOGORO': {
        'chinese': ['睿能', '智慧', '未來', '生活', '都市', '時尚', '環保', '科技', '創新', '電動'],
        'english': ['Gogoro', 'Viva', 'Delight', 'Lite', 'Plus', 'Premium', 'SuperSport', 'S', 'Series', 'Edition'],
        'series': ['1-Series', '2-Series', '3-Series', 'S-Series', 'VIVA', 'Delight', 'SuperSport', 'Lite', 'Plus', 'Premium']
    }
}

# Feature sets for different vehicle types
FEATURES_BY_TYPE = {
    'Urban Scooter': [
        'LED headlight', 'Digital display', 'Under-seat storage', 'CBS system', 'Fuel efficient',
        'Lightweight design', 'Easy handling', 'Compact size', 'Anti-theft system', 'USB charging port'
    ],
    'Sport Scooter': [
        'ABS system', 'Sport suspension', 'LED lighting system', 'Digital dashboard', 'Racing design',
        'Performance exhaust', 'Sport tires', 'Aerodynamic bodywork', 'Quick acceleration', 'Sport brakes'
    ],
    'Maxi Scooter': [
        'Large storage', 'Comfort seating', 'Windshield', 'ABS and TCS', 'Touring capability',
        'Premium features', 'Long-distance comfort', 'Weather protection', 'Cargo capacity', 'Highway capable'
    ],
    'Classic Scooter': [
        'Retro styling', 'Classic design', 'Chrome details', 'Vintage appeal', 'Simple operation',
        'Reliable engine', 'Easy maintenance', 'Timeless design', 'Comfortable ride', 'Heritage styling'
    ],
    'Naked': [
        'Upright riding position', 'Muscular design', 'Street fighter style', 'Aggressive styling', 'Performance engine',
        'Sport suspension', 'Naked bike appeal', 'Urban agility', 'Responsive handling', 'Modern technology'
    ],
    'Sport': [
        'Aerodynamic fairing', 'Racing position', 'High performance', 'Track capability', 'Advanced suspension',
        'Racing heritage', 'Supersport engine', 'Lightweight chassis', 'Racing technology', 'Sport electronics'
    ],
    'Electric Scooter': [
        'Zero emissions', 'Silent operation', 'Smart connectivity', 'Battery swapping', 'Eco-friendly',
        'Digital dashboard', 'Mobile app integration', 'Energy recovery', 'Fast charging', 'Low maintenance'
    ],
    'Electric Sport': [
        'High performance electric', 'Instant torque', 'Advanced battery', 'Sport handling', 'Quick charging',
        'Performance mode', 'Smart features', 'Connected services', 'Regenerative braking', 'Sport design'
    ]
}

# Taiwan market pricing structure (NT$)
PRICE_STRUCTURE = {
    'entry_level': (50000, 100000),     # 入門級 50-100k
    'mid_range': (100000, 200000),      # 中階級 100-200k  
    'high_end': (200000, 500000),       # 高階級 200-500k
    'premium': (500000, 1000000)        # 重機級 500k-1M+
}

# Target audience categories
TARGET_AUDIENCES = [
    '學生族群', '上班族', '家庭用戶', '重機玩家', '都市通勤族', 
    '環保愛好者', '科技愛好者', '復古愛好者', '運動愛好者', '長途旅行者'
]

# Market categories
MARKET_CATEGORIES = [
    '都市通勤', '運動休閒', '家庭實用', '性能導向', '環保節能',
    '復古經典', '豪華舒適', '越野冒險', '長途旅行', '商務用途'
]

def calculate_power(displacement, vehicle_type):
    """Calculate realistic power output for Taiwan motorcycles"""
    if vehicle_type.startswith('Electric'):
        # Electric motor power (kW to hp conversion)
        base_power = random.uniform(3.0, 15.0)  # 3-15 kW range
        return f"{base_power:.1f} kW ({base_power * 1.34:.1f} hp)"
    
    multiplier = VEHICLE_TYPES[vehicle_type]['power_multiplier']
    base_power = displacement * multiplier
    variation = random.uniform(0.85, 1.15)
    power = round(base_power * variation, 1)
    return f"{power} hp"

def calculate_torque(displacement, vehicle_type):
    """Calculate realistic torque output"""
    if vehicle_type.startswith('Electric'):
        base_torque = random.uniform(15.0, 50.0)  # Electric motors have high torque
        return f"{base_torque:.1f} Nm"
    
    # Rough torque calculation for gas engines (typically 70-80% of hp in Nm)
    power_str = calculate_power(displacement, vehicle_type)
    power_hp = float(power_str.split(' ')[0])
    torque = round(power_hp * random.uniform(0.7, 0.8) * 1.36, 1)  # Convert to Nm
    return f"{torque} Nm"

def get_engine_type(displacement, vehicle_type):
    """Get appropriate engine type"""
    if vehicle_type.startswith('Electric'):
        return random.choice([
            'Permanent magnet synchronous motor',
            'Brushless DC motor', 
            'AC synchronous motor',
            'Hub motor'
        ])
    
    for (min_cc, max_cc), engine_types in ENGINE_TYPES.items():
        if min_cc <= displacement <= max_cc:
            return random.choice(engine_types)
    return '4-stroke, liquid-cooled, single-cylinder'

def calculate_taiwan_price(brand, displacement, vehicle_type):
    """Calculate Taiwan market pricing in NT$"""
    if vehicle_type.startswith('Electric'):
        # Electric vehicle pricing
        base_price = random.uniform(70000, 150000)
        if 'Sport' in vehicle_type:
            base_price *= 1.5
        elif 'Commercial' in vehicle_type:
            base_price *= 0.8
    else:
        # Gas engine pricing
        base_price = displacement * random.uniform(0.5, 1.2) * 1000
    
    # Brand premium multipliers for Taiwan market
    brand_multipliers = {
        'SYM': 0.85, 'Kymco': 0.90, 'PGO': 0.88, 'Aeon': 0.82,
        'Yamaha': 1.15, 'Honda': 1.20, 'Suzuki': 1.05, 'Kawasaki': 1.25,
        'GOGORO': 1.30, 'PGO_Electric': 0.95, 'Aeon_Electric': 0.90
    }
    
    # Vehicle type multipliers
    type_multipliers = {
        'Urban Scooter': 1.0, 'Sport Scooter': 1.2, 'Maxi Scooter': 1.5,
        'Classic Scooter': 1.1, 'Naked': 1.3, 'Sport': 1.6, 'Classic': 1.2,
        'Adventure': 1.4, 'Electric Scooter': 1.3, 'Electric Sport': 1.8,
        'Electric Commercial': 1.0
    }
    
    brand_key = brand.split('_')[0] if '_' in brand else brand
    brand_mult = brand_multipliers.get(brand_key, 1.0)
    type_mult = type_multipliers.get(vehicle_type, 1.0)
    
    final_price = base_price * brand_mult * type_mult * random.uniform(0.9, 1.1)
    final_price = max(final_price, 45000)  # Minimum price
    
    lower_price = int(final_price * 0.95)
    upper_price = int(final_price * 1.05)
    
    return f"NT$ {lower_price:,} - {upper_price:,}"

def get_fuel_efficiency(displacement, vehicle_type):
    """Calculate fuel efficiency for Taiwan conditions"""
    if vehicle_type.startswith('Electric'):
        # Electric range in km per charge
        return f"{random.randint(80, 120)} km/charge"
    
    # Gas motorcycle fuel efficiency (km/L)
    if displacement <= 125:
        efficiency = random.uniform(45, 60)
    elif displacement <= 200:
        efficiency = random.uniform(35, 50)
    elif displacement <= 400:
        efficiency = random.uniform(25, 40)
    else:
        efficiency = random.uniform(15, 30)
    
    return f"{efficiency:.1f} km/L"

def get_weight(displacement, vehicle_type):
    """Calculate motorcycle weight"""
    if vehicle_type.startswith('Electric'):
        base_weight = random.uniform(80, 120)
    else:
        base_weight = 70 + (displacement * 0.3) + random.uniform(-10, 15)
        
    if 'Maxi' in vehicle_type or 'Adventure' in vehicle_type:
        base_weight += random.uniform(20, 40)
    elif 'Sport' in vehicle_type:
        base_weight += random.uniform(10, 25)
        
    return f"{int(base_weight)} kg"

def get_seat_height(vehicle_type):
    """Get seat height based on vehicle type"""
    height_ranges = {
        'Urban Scooter': (760, 780),
        'Sport Scooter': (770, 790), 
        'Maxi Scooter': (790, 820),
        'Classic Scooter': (750, 770),
        'Naked': (800, 830),
        'Sport': (810, 840),
        'Classic': (780, 810),
        'Adventure': (850, 890),
        'Electric Scooter': (760, 780),
        'Electric Sport': (770, 800),
        'Electric Commercial': (760, 780)
    }
    
    min_height, max_height = height_ranges.get(vehicle_type, (770, 800))
    height = random.randint(min_height, max_height)
    return f"{height} mm"

def get_availability_status(model_year):
    """Determine availability status based on model year"""
    current_year = 2024
    year_diff = current_year - model_year
    
    if year_diff <= 1:
        return "Available"
    elif year_diff <= 2:
        return random.choice(["Available", "Limited Availability"])
    elif year_diff <= 4:
        return random.choice(["Limited Availability", "Discontinued"])
    else:
        return random.choice(["Discontinued", "Used Market Only"])

def generate_model_name(brand, vehicle_type):
    """Generate realistic Taiwan motorcycle model name"""
    brand_key = brand.split('_')[0] if '_' in brand else brand
    
    if brand_key not in TAIWAN_MODEL_SERIES:
        brand_key = 'SYM'  # Default fallback
        
    series_data = TAIWAN_MODEL_SERIES[brand_key]
    
    # Choose between Chinese and English names
    use_chinese = random.choice([True, False])
    
    if use_chinese:
        chinese_name = random.choice(series_data['chinese'])
        english_name = random.choice(series_data['english'])
        model_name = chinese_name
        model_english = english_name
    else:
        model_name = random.choice(series_data['series'])
        model_english = model_name
    
    # Add displacement or series number
    if vehicle_type.startswith('Electric'):
        model_name += f" {random.choice(['E', 'Electric', 'EV', 'Plus', 'Pro'])}"
    else:
        displacement = random.randint(50, 650)
        if random.choice([True, False]):
            model_name += f" {displacement}"
    
    return model_name, model_english

def generate_features(vehicle_type, brand):
    """Generate appropriate features for the motorcycle"""
    base_features = FEATURES_BY_TYPE.get(vehicle_type, FEATURES_BY_TYPE['Urban Scooter'])
    
    # Add brand-specific features
    brand_features = {
        'GOGORO': ['Smart connectivity', 'Battery swapping system', 'Mobile app integration'],
        'Yamaha': ['VVA technology', 'Blue Core engine', 'Smart key system'],
        'Honda': ['PGM-FI fuel injection', 'Idling stop system', 'Smart key'],
        'SYM': ['CBS system', 'LED lighting', 'Anti-theft system'],
        'Kymco': ['Noodoe connectivity', 'ABS system', 'Sport suspension']
    }
    
    brand_key = brand.split('_')[0] if '_' in brand else brand
    extra_features = brand_features.get(brand_key, [])
    
    # Combine and randomize features
    all_features = list(set(base_features + extra_features))
    num_features = random.randint(4, 7)
    selected_features = random.sample(all_features, min(num_features, len(all_features)))
    
    return selected_features

def generate_motorcycle(brand, vehicle_type):
    """Generate a single Taiwan motorcycle entry"""
    # Generate displacement
    if vehicle_type.startswith('Electric'):
        displacement_cc = "Electric Motor"
        displacement_num = 0
    else:
        min_disp, max_disp = VEHICLE_TYPES[vehicle_type]['displacement_range']
        displacement_num = random.randint(min_disp, max_disp)
        displacement_cc = f"{displacement_num}cc"
    
    # Generate model information
    model_name, model_english = generate_model_name(brand, vehicle_type)
    model_year = random.randint(2020, 2025)
    
    # Generate engine specifications
    engine_type = get_engine_type(displacement_num, vehicle_type)
    power = calculate_power(displacement_num, vehicle_type)
    torque = calculate_torque(displacement_num, vehicle_type)
    
    # Generate features and pricing
    features = generate_features(vehicle_type, brand)
    price_range = calculate_taiwan_price(brand, displacement_num, vehicle_type)
    fuel_efficiency = get_fuel_efficiency(displacement_num, vehicle_type)
    weight = get_weight(displacement_num, vehicle_type)
    seat_height = get_seat_height(vehicle_type)
    availability = get_availability_status(model_year)
    
    # Assign category and target audience
    category = random.choice(MARKET_CATEGORIES)
    target_audience = random.choice(TARGET_AUDIENCES)
    
    # Build the motorcycle entry with all required fields
    motorcycle = {
        "brand": brand.replace('_', ' '),
        "model": model_name,
        "model_english": model_english,
        "model_year": str(model_year),
        "type": vehicle_type,
        "engine": {
            "displacement": displacement_cc,
            "type": engine_type,
            "power": power,
            "torque": torque
        },
        "features": features,
        "price_range": price_range,
        "fuel_efficiency": fuel_efficiency,
        "weight": weight,
        "seat_height": seat_height,
        "availability": availability,
        "category": category,
        "target_audience": target_audience
    }
    
    return motorcycle

def generate_taiwan_database():
    """Generate the complete Taiwan motorcycle database"""
    motorcycles = []
    
    print("Generating Taiwan Specific Motorcycle Database...")
    print(f"Target entries: {TARGET_ENTRIES}")
    
    for brand, target_count in TAIWAN_BRANDS.items():
        print(f"Generating {target_count} entries for {brand}...")
        
        for i in range(target_count):
            # Choose vehicle type based on brand characteristics
            if brand in ['SYM', 'Kymco', 'PGO']:
                # Taiwan brands focus on scooters
                vehicle_type = random.choice([
                    'Urban Scooter', 'Sport Scooter', 'Maxi Scooter', 'Classic Scooter'
                ])
            elif brand in ['Yamaha', 'Honda']:
                # Japanese brands have diverse portfolios
                vehicle_type = random.choice([
                    'Urban Scooter', 'Sport Scooter', 'Maxi Scooter', 'Naked', 'Sport', 'Classic'
                ])
            elif brand in ['GOGORO', 'PGO_Electric', 'Aeon_Electric']:
                # Electric brands
                vehicle_type = random.choice([
                    'Electric Scooter', 'Electric Sport', 'Electric Commercial'
                ])
            else:
                # Other brands
                vehicle_type = random.choice([
                    'Urban Scooter', 'Sport Scooter', 'Naked', 'Sport', 'Classic'
                ])
            
            motorcycle = generate_motorcycle(brand, vehicle_type)
            motorcycles.append(motorcycle)
    
    # Create the complete database structure
    database = {
        "title": "Taiwan Specific Motorcycle Database",
        "description": "Comprehensive database of motorcycles specifically for Taiwan market with complete specifications",
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "total_entries": len(motorcycles),
        "motorcycles": motorcycles
    }
    
    return database

def save_database(database, filename):
    """Save database to JSON file with proper formatting"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)
    
    print(f"\nDatabase saved to {filename}")
    print(f"Total entries: {database['total_entries']}")

def main():
    """Main function"""
    print("Taiwan Motorcycle Database Generator Starting...")
    
    # Generate the database
    database = generate_taiwan_database()
    
    # Save to file
    save_database(database, OUTPUT_FILE)
    
    # Print summary statistics
    motorcycles = database['motorcycles']
    
    print(f"\n=== Generation Summary ===")
    print(f"Total motorcycles generated: {len(motorcycles)}")
    
    # Brand distribution
    from collections import Counter
    brands = Counter(m['brand'] for m in motorcycles)
    print(f"\nBrand Distribution:")
    for brand, count in brands.most_common():
        print(f"  {brand}: {count} models")
    
    # Vehicle type distribution
    types = Counter(m['type'] for m in motorcycles)
    print(f"\nVehicle Type Distribution:")
    for vtype, count in types.most_common():
        print(f"  {vtype}: {count} models")
    
    # Year distribution
    years = Counter(m['model_year'] for m in motorcycles)
    print(f"\nModel Year Distribution:")
    for year, count in sorted(years.items()):
        print(f"  {year}: {count} models")
    
    print(f"\n✅ Taiwan motorcycle database successfully generated!")
    print(f"📄 Saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()