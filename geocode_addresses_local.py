# geocode_addresses_local.py
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import time

# CONFIGURATION
INPUT_FILE = "addresses.csv"  # Update to your file name
ADDRESS_COLUMN = "full_address"
OUTPUT_FILE = "geocoded_addresses.csv"

# Load address data
df = pd.read_csv(INPUT_FILE)

# Set up geolocator and rate limiter
geolocator = Nominatim(user_agent="district6-campaign")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1.5)

# Geocode addresses
df['location'] = df[ADDRESS_COLUMN].apply(geocode)
df['latitude'] = df['location'].apply(lambda loc: loc.latitude if loc else None)
df['longitude'] = df['location'].apply(lambda loc: loc.longitude if loc else None)

# Save output
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Geocoding complete. Output saved to {OUTPUT_FILE}")
