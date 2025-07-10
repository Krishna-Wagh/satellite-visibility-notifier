from n2yo_api import get_satellite_passes
from email_sender import send_email
from geocode import get_coordinates
from datetime import datetime

# Satellite list
SATELLITES = {
    "ISS (ZARYA)": 25544,
    "Hubble Space Telescope": 20580,
    "NOAA 19": 33591,
    "Starlink-1500": 44238,
    "Envisat": 27386,
    "Terra": 25994,
    "Tiangong (Chinese Station)": 48274,
    "Iridium 33": 24946,
    "GPS BIIR-2 (USA-47)": 22700,
    "METEOR M2": 40069
}

def main():
    print("🌍 Welcome to Satellite Visibility Notifier!\n")

    # Get user city and convert to coordinates
    city = input("Enter your city or location (e.g., Mumbai): ").strip()
    lat, lon = get_coordinates(city)
    if not lat or not lon:
        print("❌ Unable to get coordinates. Please try again with a valid city.")
        return

    # Ask for number of days
    try:
        days = int(input("Enter number of days to check (e.g., 1–5): "))
        if days < 1 or days > 10:
            print("⚠️ Please enter a number between 1 and 10.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return

    # Satellite selection
    print("\nAvailable Satellites:")
    for i, name in enumerate(SATELLITES, 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Choose a satellite (1–10): "))
        sat_name = list(SATELLITES.keys())[choice - 1]
        sat_id = SATELLITES[sat_name]
    except (ValueError, IndexError):
        print("❌ Invalid selection.")
        return

    print(f"\n📡 Fetching visible passes for {sat_name} over {city} (next {days} days)...")

    # Fetch satellite passes
    passes = get_satellite_passes(sat_id, lat, lon, days)
    passes = [p for p in passes if p is not None]

    if not passes:
        print("❌ No visible passes found.")
        return

    # Format output
    content = f"🛰️ {sat_name} Visible Passes over {city}:\n\n"
    for i, p in enumerate(passes[:5]):
        try:
            rise_time = datetime.utcfromtimestamp(p['startUTC']).strftime('%Y-%m-%d %H:%M:%S UTC')
            max_elev = p['maxEl']
            duration = p['duration']
            brightness = p.get('mag', 'N/A')

            content += f"Pass {i+1}:\n"
            content += f"  Start Time : {rise_time}\n"
            content += f"  Duration   : {duration} seconds\n"
            content += f"  Max Elev.  : {max_elev}°\n"
            content += f"  Brightness : {brightness}\n"
            content += "  ---\n"
        except Exception as e:
            print(f"⚠️ Skipped a pass due to data error: {e}")
            continue

    print("\n📋 Summary:\n" + content)

    # Email option
    notify = input("📧 Do you want this sent to your email? (yes/no): ").lower()
    if notify == "yes":
        email = input("Enter your email address: ").strip()
        success = send_email(email, f"{sat_name} Passes over {city}", content)
        if success:
            print("✅ Email sent successfully.")
        else:
            print("❌ Email sending failed.")

if __name__ == "__main__":
    main()
