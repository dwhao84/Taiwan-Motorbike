# Taiwan Motorcycle Database

## Overview
This repository contains comprehensive motorcycle data for Taiwan, featuring over 20,000 motorcycle entries from major brands popular in Taiwan.

## Files

### complete_motorcycle_database.json
A comprehensive database with 20,000 motorcycle entries including:
- **Brand**: Major motorcycle brands (Honda, Yamaha, Kymco, SYM, Suzuki, Kawasaki, Aeon, PGO, Sanyang, CFMOTO)
- **Model**: Specific model names with variants and years
- **Type**: Vehicle type (Sport, Scooter, Touring, Adventure, etc.)
- **Engine**: Complete engine specifications
  - Displacement (50cc - 1500cc)
  - Engine type (4-stroke liquid-cooled, air-cooled, etc.)
  - Power output (HP)
- **Features**: Key features and capabilities
- **Price Range**: Taiwan market pricing in NT$ (New Taiwan Dollar)
- **Availability**: Current availability status

### TaiwanMotor.json
Original smaller database with curated motorcycle data organized by categories.

### taiwan_specific_motorcycles.json
Focused database containing 33 specific motorcycle models popular in Taiwan, including:
- **SYM Models**: 全新迪爵125, JET SL+ 158, 迪爵125, Woo 115, 活力125, CLBCU 125, DRG 158, Jet 14 125, MAXSYM TL 500
- **Kymco Models**: 大地名流125/150, GP 125, 新豪邁125, Racing S 150, iONEX, AK 550
- **Yamaha Models**: Jog 125, 勁戰 (Force 155), SMAX 155, YZF-R3, MT-03
- **Honda Models**: PCX 150, Vino 125, CB300R
- **GOGORO**: Electric scooter series (2 Series, Viva Mix, 3 Series)
- **Other Electric**: PGO Ur1, 宏佳騰 Ai-1 Sport
- **Local Brands**: 光陽 Many 110, 三陽 FNX 125, 比雅久 Tigra 200
- **Sport Bikes**: Kawasaki Ninja 400
- Includes realistic Taiwan market pricing and specifications
- Features both Chinese and English model names for better accessibility
- Covers various categories: Urban/Sport Scooters, Electric Vehicles, Naked Bikes, Sport Bikes, Maxi Scooters

### generate_motorcycle_database.py
Python script that generates the comprehensive motorcycle database. Run this script to create or regenerate the `complete_motorcycle_database.json` file with 20,000 realistic motorcycle entries.

### example_usage.py
Example script demonstrating how to load and use the motorcycle database for various analysis and filtering tasks.

### taiwan_specific_usage.py
Example Python script for working with the Taiwan-specific motorcycle database. Demonstrates filtering and analysis of the curated Taiwan models.

### enhanced_database_demo.py
Demonstration script showcasing the enhanced database features including the extended 2000-2025 year coverage and realistic availability statuses.

## Database Structure

Each motorcycle entry follows this structure:
```json
{
  "brand": "Honda",
  "model": "PCX 150 (2023)",
  "type": "Sport Scooter",
  "engine": {
    "displacement": "150cc",
    "type": "4-stroke, liquid-cooled",
    "power": "13.2 hp"
  },
  "features": ["LED lighting", "Smart key", "Large storage space"],
  "price_range": "NT$ 110,000 - 120,000",
  "availability": "Available"
}
```

### Availability Status
The database includes realistic availability statuses based on model year:
- **Available**: Current models (2022-2025)
- **Limited Availability**: Recent models with limited stock (2018-2021)
- **Discontinued**: Models no longer in production (2010-2017)
- **Used Market Only**: Older models available only in used market (2005-2015)
- **Collector Item**: Classic/vintage models (2000-2009)

## Usage

### Running the Generator
To generate a fresh database with 20,000 motorcycle entries:
```bash
python3 generate_motorcycle_database.py
```

### Loading the Database
```python
import json

# Load the complete database
with open('complete_motorcycle_database.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

motorcycles = data['motorcycles']
print(f"Total entries: {len(motorcycles)}")

# Or load the Taiwan-specific database
with open('taiwan_specific_motorcycles.json', 'r', encoding='utf-8') as f:
    taiwan_data = json.load(f)

taiwan_motorcycles = taiwan_data['motorcycles']
print(f"Taiwan specific entries: {len(taiwan_motorcycles)}")
```

### Filtering Examples
```python
# Filter by brand
honda_bikes = [m for m in motorcycles if m['brand'] == 'Honda']

# Filter by displacement
small_bikes = [m for m in motorcycles if '125cc' in m['engine']['displacement']]

# Filter by type
scooters = [m for m in motorcycles if 'Scooter' in m['type']]
```

### Running Examples
To see database analysis and usage examples:
```bash
# For the comprehensive database
python3 example_usage.py

# For the Taiwan-specific database
python3 taiwan_specific_usage.py
```

### Taiwan-Specific Database
The `taiwan_specific_motorcycles.json` contains curated data for 33 specific popular Taiwan motorcycle models:
- **33 Popular Models**: Including SYM, Kymco, Yamaha, Honda, GOGORO, and local brands
- **Chinese Names**: Original Chinese model names with English translations
- **Taiwan Pricing**: Realistic Taiwan market pricing in NT$
- **Accurate Specs**: Real-world engine specifications and features
- **Diverse Categories**: Urban/Sport Scooters, Electric Vehicles, Sport Bikes, Naked Bikes, Maxi Scooters

Example usage:
```python
# Load Taiwan-specific database
with open('taiwan_specific_motorcycles.json', 'r', encoding='utf-8') as f:
    taiwan_data = json.load(f)

# Find all SYM models
sym_models = [m for m in taiwan_data['motorcycles'] if m['brand'] == 'SYM']
print(f"SYM models: {len(sym_models)}")

# Find budget motorcycles under NT$ 70,000
budget_bikes = [m for m in taiwan_data['motorcycles'] 
                if int(m['price_range'].split('NT$ ')[1].split(' -')[0].replace(',', '')) < 70000]

# Find electric motorcycles
electric_bikes = [m for m in taiwan_data['motorcycles'] 
                  if m['engine']['displacement'] == 'Electric Motor'] 
                if int(m['price_range'].split(' - ')[0].replace('NT$ ', '').replace(',', '')) <= 70000]
```

## Data Generation

The comprehensive database was generated using `generate_motorcycle_database.py` which creates realistic motorcycle data by:
- Combining real brand names with logical model variations
- Using appropriate engine displacements for different vehicle types
- Calculating realistic power outputs based on displacement
- Generating Taiwan market pricing with brand premiums
- Including model years from 2000-2025 (26 years of comprehensive data)
- Adding realistic feature sets and variants
- Implementing availability status based on model year (Available, Discontinued, Limited Availability, Used Market Only, Collector Item)

## Brand Coverage

- **Honda**: 2,980 entries
- **Yamaha**: 3,023 entries  
- **Kymco**: 2,519 entries
- **SYM**: 2,531 entries
- **Suzuki**: 2,290 entries
- **Kawasaki**: 1,909 entries
- **Aeon**: 1,250 entries
- **Sanyang**: 1,300 entries
- **CFMOTO**: 1,142 entries
- **PGO**: 1,056 entries

## License
This data is provided for educational and research purposes.