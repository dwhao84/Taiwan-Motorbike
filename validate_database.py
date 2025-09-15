#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taiwan Motorcycle Database Validator

This script validates the TaiwanMotor.json database to ensure:
- JSON format is valid
- All required fields are present
- Data consistency checks
"""

import json
import sys

def validate_json_format(filename):
    """Validate that the JSON file is properly formatted."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, data, None
    except json.JSONDecodeError as e:
        return False, None, f"JSON format error: {e}"
    except FileNotFoundError:
        return False, None, f"File not found: {filename}"
    except Exception as e:
        return False, None, f"Error reading file: {e}"

def validate_data_structure(motorcycles):
    """Validate the structure of motorcycle data."""
    errors = []
    required_fields = ['brand', 'model', 'year', 'generation']
    
    if not isinstance(motorcycles, list):
        errors.append("Data should be a list of motorcycle objects")
        return errors
    
    for i, bike in enumerate(motorcycles):
        if not isinstance(bike, dict):
            errors.append(f"Entry {i}: Should be a dictionary object")
            continue
            
        # Check required fields
        for field in required_fields:
            if field not in bike:
                errors.append(f"Entry {i}: Missing required field '{field}'")
        
        # Check data types
        if 'brand' in bike and not isinstance(bike['brand'], str):
            errors.append(f"Entry {i}: 'brand' should be a string")
        
        if 'model' in bike and not isinstance(bike['model'], str):
            errors.append(f"Entry {i}: 'model' should be a string")
        
        # Check for empty values
        if 'brand' in bike and not bike['brand'].strip():
            errors.append(f"Entry {i}: 'brand' cannot be empty")
        
        if 'model' in bike and not bike['model'].strip():
            errors.append(f"Entry {i}: 'model' cannot be empty")
    
    return errors

def validate_data_consistency(motorcycles):
    """Check for data consistency issues."""
    warnings = []
    
    # Check for duplicate entries
    seen_combinations = set()
    for i, bike in enumerate(motorcycles):
        if 'brand' in bike and 'model' in bike:
            combination = (bike['brand'], bike['model'])
            if combination in seen_combinations:
                warnings.append(f"Entry {i}: Duplicate combination '{bike['brand']} {bike['model']}'")
            seen_combinations.add(combination)
    
    # Check brand consistency
    brands = set()
    for bike in motorcycles:
        if 'brand' in bike:
            brands.add(bike['brand'])
    
    print(f"Found {len(brands)} unique brands: {', '.join(sorted(brands))}")
    
    return warnings

def generate_statistics(motorcycles):
    """Generate basic statistics about the database."""
    from collections import Counter
    
    print("\n=== Database Statistics ===")
    print(f"Total entries: {len(motorcycles)}")
    
    # Brand distribution
    brand_counts = Counter(bike.get('brand', 'Unknown') for bike in motorcycles)
    print(f"Brands: {len(brand_counts)}")
    
    for brand, count in brand_counts.most_common():
        percentage = (count / len(motorcycles)) * 100
        print(f"  {brand}: {count} models ({percentage:.1f}%)")
    
    # Year information
    years_with_data = sum(1 for bike in motorcycles if bike.get('year') is not None)
    print(f"\nEntries with year information: {years_with_data}")
    print(f"Entries without year information: {len(motorcycles) - years_with_data}")
    
    # Generation information
    gen_with_data = sum(1 for bike in motorcycles if bike.get('generation') is not None)
    print(f"Entries with generation information: {gen_with_data}")
    print(f"Entries without generation information: {len(motorcycles) - gen_with_data}")

def main():
    """Main validation function."""
    filename = 'TaiwanMotor.json'
    
    print("Taiwan Motorcycle Database Validator")
    print("=" * 50)
    
    # Validate JSON format
    print("1. Validating JSON format...")
    is_valid, data, error = validate_json_format(filename)
    
    if not is_valid:
        print(f"❌ FAILED: {error}")
        sys.exit(1)
    
    print("✅ JSON format is valid")
    
    # Validate data structure
    print("\n2. Validating data structure...")
    structure_errors = validate_data_structure(data)
    
    if structure_errors:
        print("❌ FAILED: Data structure issues found:")
        for error in structure_errors[:10]:  # Show first 10 errors
            print(f"  - {error}")
        if len(structure_errors) > 10:
            print(f"  ... and {len(structure_errors) - 10} more errors")
        sys.exit(1)
    
    print("✅ Data structure is valid")
    
    # Check data consistency
    print("\n3. Checking data consistency...")
    warnings = validate_data_consistency(data)
    
    if warnings:
        print("⚠️  WARNINGS: Consistency issues found:")
        for warning in warnings[:10]:  # Show first 10 warnings
            print(f"  - {warning}")
        if len(warnings) > 10:
            print(f"  ... and {len(warnings) - 10} more warnings")
    else:
        print("✅ No consistency issues found")
    
    # Generate statistics
    generate_statistics(data)
    
    print("\n" + "=" * 50)
    print("✅ Validation complete!")
    
    if structure_errors:
        print(f"❌ Found {len(structure_errors)} errors")
        return False
    elif warnings:
        print(f"⚠️  Found {len(warnings)} warnings")
        return True
    else:
        print("✅ Database is fully valid!")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)