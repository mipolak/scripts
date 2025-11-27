#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path

# GLOBAL: mapping JSON keys -> CSV header names (hardcoded, fixed order)
KEY_MAP = {
    "id": "user_id",
    "name_a": "name",
    "name_b": "surname",
    "address": "address",
    "country_code": "country code",
    "mail": "email_address",  # example of nested key list
    # add more keys if needed
}

def find_nested_key(obj, key, path=""):
    """Recursively search for key in nested JSON structures."""
    if isinstance(obj, dict):
        if key in obj:
            return obj[key], f"{path}.{key}" if path else key
        for k, v in obj.items():
            result, found_path = find_nested_key(v, key, f"{path}.{k}" if path else k)
            if result is not None:
                return result, found_path
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            result, found_path = find_nested_key(item, key, f"{path}[{i}]")
            if result is not None:
                return result, found_path
    return None, None

def collect_all_keys(obj, seen_keys=None):
    """Recursively collect all keys in nested JSON objects."""
    if seen_keys is None:
        seen_keys = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            seen_keys.add(k)
            collect_all_keys(v, seen_keys)
    elif isinstance(obj, list):
        for item in obj:
            collect_all_keys(item, seen_keys)
    return seen_keys

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise ValueError("JSON must be an object or a list of objects")
    return data

def preview_keys(json_path: Path):
    """Preview which keys from KEY_MAP exist in JSON, plus list other keys."""
    records = load_json(json_path)
    print("Key search preview:")
    print("-" * 40)
    for json_key, csv_header in KEY_MAP.items():
        found = False
        paths = []
        for i, obj in enumerate(records[:3]):  # inspect first 3 records
            val, path = find_nested_key(obj, json_key)
            if val is not None:
                found = True
                paths.append(f"record[{i}]/{path}")
                break
        status = "✓" if found else "✗"
        print(f"{csv_header:<20} {status}  {paths[0] if paths else 'MISSING'}")
    print()
    # Collect all keys present in first 3 records
    all_keys = set()
    for obj in records[:3]:
        keys = collect_all_keys(obj)
        all_keys.update(keys)
    # Remove keys already in KEY_MAP to list only others
    other_keys = sorted(all_keys - set(KEY_MAP.keys()))

    print("Available keys:")
    print("-" * 40)
    if other_keys:
        for k in other_keys:
            print(k)
    else:
        print("(no other keys found)")

def json_to_csv(json_path: Path, csv_path: Path, preview=False):
    if preview:
        preview_keys(json_path)
        return

    keys = list(KEY_MAP.keys())
    headers = list(KEY_MAP.values())
    records = load_json(json_path)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for obj in records:
            row = []
            for key in keys:
                val, _ = find_nested_key(obj, key)
                if val in ("", None):
                    row.append("NULL")
                else:
                    row.append(str(val))
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(
        description="JSON -> CSV converter with key search & preview"
    )
    parser.add_argument(
        "input_json",
        type=Path,
        help="Input JSON file (object or list of objects)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output CSV file (default: same name with .csv extension)",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Preview which keys exist in JSON (don't convert)",
    )

    args = parser.parse_args()

    json_path = args.input_json
    csv_path = args.output or json_path.with_suffix(".csv")

    if args.preview:
        json_to_csv(json_path, csv_path, preview=True)
    else:
        json_to_csv(json_path, csv_path)
        print(f"Converted {json_path} -> {csv_path}")

if __name__ == "__main__":
    main()
