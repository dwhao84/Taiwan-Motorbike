# Taiwan Motorcycle Database

## Overview
This repository contains a comprehensive motorcycle database for Taiwan, featuring 331 motorcycle entries from 6 major brands popular in the Taiwan market. The database includes both traditional gasoline motorcycles and modern electric vehicles.

## Data Source: TaiwanMotor.json

The main data file `TaiwanMotor.json` contains curated motorcycle information with the following structure:

### Database Structure
Each motorcycle entry follows this simple but comprehensive structure:
```json
{
  "brand": "Yamaha",
  "model": "FORCE 155（1DK）",
  "year": null,
  "generation": null
}
```

### Brand Coverage
The database covers 6 major motorcycle brands in Taiwan:

- **KYMCO (光陽)**: 121 models (36.6%) - The largest Taiwanese motorcycle manufacturer
- **Suzuki**: 74 models (22.4%) - Popular Japanese brand with strong presence in Taiwan
- **PGO (摩特動力)**: 52 models (15.7%) - Taiwanese manufacturer known for scooters
- **Yamaha**: 50 models (15.1%) - Japanese brand popular for sport bikes and scooters
- **Aeon (宏佳騰)**: 18 models (5.4%) - Taiwanese manufacturer with focus on electric vehicles
- **Gogoro**: 16 models (4.8%) - Leading Taiwanese electric scooter brand

**Total: 331 motorcycle entries**

### Model Categories

The database includes various types of motorcycles popular in Taiwan:

#### Traditional Gasoline Motorcycles
- **Scooters**: Most popular category in Taiwan (KYMCO Racing 150, Yamaha SMAX 155)
- **Sport Bikes**: Performance motorcycles (Yamaha YZF-R15, Suzuki GSX-R150)
- **Naked Bikes**: Versatile motorcycles (Yamaha MT series, Suzuki GSX-S series)
- **Adventure Bikes**: Touring motorcycles (Suzuki V-Strom series)
- **Classic/Retro**: Traditional styled bikes (Aeon MY150 Retro ABS)

#### Electric Motorcycles
- **Gogoro Series**: 1 Series, 2 Series, 3 Series, VIVA, SuperSport, CrossOver
- **Aeon Electric**: Ai-1 Sport series, EV.C1, eReady series

#### Engine Displacements
- **50cc-100cc**: Entry-level scooters and motorcycles
- **125cc-150cc**: Most popular segment in Taiwan
- **200cc-300cc**: Mid-range motorcycles
- **400cc+**: Large displacement bikes and adventure motorcycles

## Usage Examples

### Loading the Database
```python
import json

# Load the Taiwan motorcycle database
with open('TaiwanMotor.json', 'r', encoding='utf-8') as f:
    motorcycles = json.load(f)

print(f"Total motorcycles: {len(motorcycles)}")
```

### Data Validation
Validate the database integrity:
```bash
python3 validate_database.py

### Filtering by Brand
```python
# Get all KYMCO motorcycles
kymco_bikes = [bike for bike in motorcycles if bike['brand'] == 'KYMCO']
print(f"KYMCO models: {len(kymco_bikes)}")

# Get all electric motorcycles (Gogoro)
electric_bikes = [bike for bike in motorcycles if bike['brand'] == 'Gogoro']
print(f"Electric models: {len(electric_bikes)}")
```

### Analyzing Brand Distribution
```python
from collections import Counter

# Count motorcycles by brand
brand_counts = Counter(bike['brand'] for bike in motorcycles)

print("Brand distribution:")
for brand, count in brand_counts.most_common():
    print(f"{brand}: {count} models")
```

### Searching for Specific Models
```python
# Find models containing specific keywords
def search_models(keyword):
    return [bike for bike in motorcycles 
            if keyword.lower() in bike['model'].lower()]

# Search examples
racing_models = search_models('racing')
abs_models = search_models('abs')
electric_models = search_models('electric')
```

### Model Name Analysis
```python
# Find models with Chinese names
chinese_models = [bike for bike in motorcycles 
                 if any('\u4e00' <= char <= '\u9fff' for char in bike['model'])]

print(f"Models with Chinese names: {len(chinese_models)}")
```

## Notable Models in the Database

### Popular Scooters
- **KYMCO Racing S 150**: Performance scooter with ABS
- **Yamaha FORCE 155**: Popular sport scooter
- **PGO Tigra series**: Various displacement options (125cc-250cc)

### Electric Vehicles
- **Gogoro 2 Series**: Best-selling electric scooter in Taiwan
- **Gogoro VIVA**: Entry-level electric scooter
- **Aeon Ai-1 Sport**: Electric scooter with smart features

### Sport Motorcycles
- **Yamaha YZF-R15**: Entry-level sport bike
- **Suzuki GSX-R series**: Performance sport bikes
- **Yamaha MT series**: Naked sport motorcycles

### Adventure/Touring
- **Suzuki V-Strom series**: Adventure motorcycles (650cc-1050cc)
- **KYMCO AK550**: Maxi scooter for long-distance riding

## Data Characteristics

### Naming Conventions
- **Bilingual Models**: Many models include both English and Chinese names
- **Technical Specifications**: Engine codes and technical details (e.g., "5ML", "1DK")
- **Variants**: Multiple variants of popular models (ABS, TCS versions)

### Market Coverage
- **Entry Level**: 50cc-125cc scooters for urban commuting
- **Mid-Range**: 150cc-250cc motorcycles for versatile use
- **Premium**: 300cc+ motorcycles and electric vehicles
- **Specialty**: Adventure, sport, and touring motorcycles

## Data Analysis & Statistics

### Language Distribution
- **English names only**: 202 models (61.0%)
- **Chinese names only**: 21 models (6.3%)
- **Mixed language**: 108 models (32.6%)

### Popular Features & Keywords
- **ABS (Anti-lock Braking System)**: 24 models
- **125cc engines**: 81 models (most popular displacement)
- **150cc engines**: 41 models (second most popular)
- **Racing variants**: 6 models
- **Max/SMAX series**: 10 models

### Electric Vehicle Coverage
- **Total electric models**: 25 (7.5% of database)
- **Gogoro**: 16 models (complete product line)
- **Aeon electric**: 9 models (Ai series, EV.C1, eReady)

## Usage Example Script

Run the included analysis script to explore the database:
```bash
python3 analyze_database.py
```

This script provides:
- Brand distribution analysis
- Sample models by manufacturer
- Language analysis (Chinese vs English names)
- Electric vehicle identification
- Popular keyword analysis

## File Information
- **File**: TaiwanMotor.json
- **Format**: JSON array of motorcycle objects
- **Encoding**: UTF-8 (supports Chinese characters)
- **Size**: ~29KB
- **Entries**: 331 motorcycles

## Development and Contribution
This database represents a comprehensive collection of motorcycles available in the Taiwan market. The data includes:
- Major Taiwanese brands (KYMCO, PGO, Aeon)
- Popular Japanese brands (Yamaha, Suzuki)
- Leading electric vehicle manufacturer (Gogoro)

## License
This data is provided for educational and research purposes. Perfect for:
- Market research on Taiwan motorcycle industry
- Academic studies on transportation in Taiwan
- Development of motorcycle-related applications
- Analysis of electric vehicle adoption in Asia