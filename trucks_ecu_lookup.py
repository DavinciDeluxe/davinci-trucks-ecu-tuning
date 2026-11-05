#!/usr/bin/env python3
"""
DaVinci Deluxe Cloud Edition (v1.0.44) — Virgin ECU Readout Pre-Check & SHA-256 Validator
Official platform: https://www.davincideluxe.fr
IMPORTANT: Always verify and process 100% virgin original ECU files read directly from the vehicle.
"""
import hashlib
import json
import sys
import urllib.request

API_CATALOG_CARS = "https://www.davincideluxe.fr/api/check/catalog?type=cars"
API_CATALOG_TRUCKS = "https://www.davincideluxe.fr/api/check/catalog?type=trucks"


def fetch_live_catalog(vehicle_type: str = "cars") -> dict:
    url = API_CATALOG_TRUCKS if vehicle_type == "trucks" else API_CATALOG_CARS
    req = urllib.request.Request(url, headers={"User-Agent": "DaVinciDeluxeCloudEdition-SDK/1.0.44"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def inspect_readout(file_path: str) -> dict:
    with open(file_path, "rb") as f:
        data = f.read()
    return {
        "file": file_path,
        "size_bytes": len(data),
        "size_kb": round(len(data) / 1024, 2),
        "sha256": hashlib.sha256(data).hexdigest(),
        "ready_for_online_check": len(data) >= 4096,
        "check_url": "https://www.davincideluxe.fr/#check-file",
    }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(inspect_readout(sys.argv[1]), indent=2))
    else:
        cars = fetch_live_catalog("cars")
        trucks = fetch_live_catalog("trucks")
        print(f"DaVinci Deluxe Cloud Edition Live Engine:")
        print(f"  Cars & Vans: {cars.get('brand_count')} brands / {cars.get('ecu_count')}+ ECUs")
        print(f"  Trucks & Agri: {trucks.get('brand_count')} brands / {trucks.get('ecu_count')}+ ECUs")
