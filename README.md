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

### generate_motorcycle_database.py
Python script that generates the comprehensive motorcycle database. Run this script to create or regenerate the `complete_motorcycle_database.json` file with 20,000 realistic motorcycle entries.

### example_usage.py
Example script demonstrating how to load and use the motorcycle database for various analysis and filtering tasks.

## Database Structure

Each motorcycle entry follows this structure:
```json
{
  "brand": "Honda",
  "model": "PCX 150",
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
python3 example_usage.py
```

## Data Generation

The comprehensive database was generated using `generate_motorcycle_database.py` which creates realistic motorcycle data by:
- Combining real brand names with logical model variations
- Using appropriate engine displacements for different vehicle types
- Calculating realistic power outputs based on displacement
- Generating Taiwan market pricing with brand premiums
- Including model years from 2020-2024
- Adding realistic feature sets and variants

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