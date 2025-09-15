# Taiwan Motorcycle Database

## Overview
This repository contains comprehensive motorcycle data for Taiwan, organized by brand, year, and model structure covering 10 years (2015-2024) of Taiwan's motorcycle market.

## Files

### taiwan_motorcycles_by_brand_year.json
**NEW:** Comprehensive database with 832+ motorcycle entries organized by Brand → Year → Models structure, covering:
- **Brands**: Yamaha, Honda, SYM, Kymco, PGO, Suzuki, Vespa, CPI, Hartford, Kawasaki
- **Years**: 2015-2024 (past 10 years of Taiwan motorcycle market)
- **Models**: Detailed specifications including:
  - Model name and year
  - Vehicle type (Sport Scooter, Sport Bike, Electric, etc.)
  - Engine specifications (displacement, power, type)
  - Features and capabilities
  - Taiwan market pricing in NT$ (New Taiwan Dollar)
  - Current availability status
  - Market segment classification

### TaiwanMotor.json
Original database with curated motorcycle data organized by categories.

### generate_brand_year_database.py
Python script that generates the comprehensive brand/year/model organized motorcycle database. Run this script to create or regenerate the `taiwan_motorcycles_by_brand_year.json` file with 800+ realistic motorcycle entries covering 10 years of Taiwan market data.

### brand_year_usage_example.py
Example script demonstrating how to load and use the brand/year organized motorcycle database for various analysis and filtering tasks, including:
- Query models by brand and year
- Find available/electric/budget models
- Analyze brand statistics and market trends

## Database Structure

The new brand/year/model organized database follows this hierarchical structure:

```json
{
  "title": "Taiwan Motorcycle Database - Brand/Year/Model Structure",
  "description": "Comprehensive motorcycle database organized by brand, year, and model for Taiwan market (2015-2024)",
  "structure": "Brand → Year → Models",
  "years_covered": "2015-2024 (10 years)",
  "brands": {
    "Yamaha": {
      "country_of_origin": "Japan",
      "years": {
        "2024": {
          "models": [
            {
              "model": "Force 155 ABS",
              "year": 2024,
              "type": "Sport Scooter",
              "engine": {
                "displacement": "155cc",
                "type": "4-stroke, liquid-cooled",
                "power": "15 hp"
              },
              "features": ["LED lighting", "ABS", "Smart key", "Digital display"],
              "price_range": "NT$ 95,000 - 125,000",
              "availability": "Available",
              "market_segment": "Sport/Touring"
            }
          ]
        }
      }
    }
  }
}
```

### Availability Status
The database includes realistic availability statuses based on model year:
- **Available**: Current models (2022-2024)
- **Limited Availability**: Recent models with limited stock (2019-2021)
- **Discontinued**: Models no longer in production (2016-2018)
- **Used Market Only**: Older models available only in used market (2015)

## Usage

### Running the Generator
To generate a fresh brand/year organized database:
```bash
python3 generate_brand_year_database.py
```

### Loading the Database
```python
import json

# Load the brand/year organized database
with open('taiwan_motorcycles_by_brand_year.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Database: {data['title']}")
print(f"Brands: {list(data['brands'].keys())}")

# Get all Yamaha models in 2024
yamaha_2024 = data['brands']['Yamaha']['years']['2024']['models']
print(f"Yamaha 2024 models: {len(yamaha_2024)}")

# Get all Honda models across all years
honda_models = []
for year_data in data['brands']['Honda']['years'].values():
    honda_models.extend(year_data['models'])
print(f"Total Honda models: {len(honda_models)}")
```

### Query Examples
```python
# Find all available electric motorcycles
electric_available = []
for brand_name, brand_data in data['brands'].items():
    for year, year_data in brand_data['years'].items():
        for model in year_data['models']:
            if (model['availability'] == 'Available' and 
                model['engine'].get('displacement') == 'Electric Motor'):
                electric_available.append({
                    'brand': brand_name,
                    'model': model['model'],
                    'year': model['year']
                })

# Find budget models under NT$ 70,000
budget_bikes = []
for brand_name, brand_data in data['brands'].items():
    for year, year_data in brand_data['years'].items():
        for model in year_data['models']:
            price_str = model['price_range']
            min_price = int(price_str.split(' - ')[0].replace('NT$ ', '').replace(',', ''))
            if min_price <= 70000:
                budget_bikes.append({
                    'brand': brand_name,
                    'model': model['model'],
                    'price_range': model['price_range']
                })
```


### Running Examples  
To see database analysis and usage examples:
```bash
python3 brand_year_usage_example.py
```

## Data Generation

The brand/year organized database was generated using `generate_brand_year_database.py` which creates realistic motorcycle data by:
- Organizing by Brand → Year (2015-2024) → Models structure
- Including all 10 major Taiwan motorcycle brands
- Combining real brand characteristics with logical model variations
- Using appropriate engine displacements for different vehicle types
- Calculating realistic power outputs based on displacement
- Generating Taiwan market pricing with brand premiums and year-based adjustments
- Adding realistic feature sets for each motorcycle category
- Implementing availability status based on model year (Available, Discontinued, Limited Availability, Used Market Only)

## Brand Coverage

The database covers 10 major motorcycle brands in Taiwan:

- **Yamaha** (Japan): 124 models - Sport scooters, sport bikes, classic scooters
- **Honda** (Japan): 108 models - Premium scooters, naked bikes, sport bikes  
- **SYM** (Taiwan): 118 models - Local favorite, sport scooters, maxi scooters
- **Kymco** (Taiwan): 125 models - Leading Taiwan brand, strong electric lineup
- **Suzuki** (Japan): 84 models - Sport bikes, adventure bikes, naked bikes
- **Kawasaki** (Japan): 67 models - High-performance sport bikes, naked bikes
- **Vespa** (Italy): 58 models - Premium classic and modern scooters
- **PGO** (Taiwan): 59 models - Budget-friendly, electric innovation
- **CPI** (Taiwan): 53 models - Affordable sport scooters
- **Hartford** (Taiwan): 36 models - Cruisers and touring motorcycles

**Total: 832 models** spanning 10 years (2015-2024)

## License
This data is provided for educational and research purposes.