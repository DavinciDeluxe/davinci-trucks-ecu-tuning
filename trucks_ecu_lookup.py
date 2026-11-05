#!/usr/bin/env python3
"""DaVinci Deluxe Cloud Edition (v1.0.44) — Virgin ECU Readout Pre-Check & Live Multi-Domain Catalog"""
import hashlib, json, sys, urllib.request

OFFICIAL_DOMAINS = [
    "https://www.davincideluxe.fr", "https://www.davincideluxe.org",
    "https://www.davincideluxe.app", "https://www.davincideluxe.software",
    "https://www.davincideluxe.es", "https://www.davincideluxe.de",
    "https://www.davincideluxe.it", "https://www.aesoftech.eu"
]

def inspect_virgin_file(path: str) -> dict:
    raw = open(path, "rb").read()
    return {
        "file": path,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "official_check_url": "https://www.davincideluxe.fr/#check-file"
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(inspect_virgin_file(sys.argv[1]), indent=2))
    else:
        print("Official DaVinci Deluxe Cloud Edition Domains:", ", ".join(OFFICIAL_DOMAINS))
