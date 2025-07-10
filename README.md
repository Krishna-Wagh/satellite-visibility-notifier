# 🛰️ Satellite Visibility Notifier

A Python project that tells you when popular satellites like the **ISS**, **Starlink**, or **Hubble** will be visible over your city in the coming days.  
It uses the [N2YO Satellite Tracking API](https://www.n2yo.com/api/) and [OpenCage Geocoding API](https://opencagedata.com/) to fetch real-time satellite pass data and can optionally send the report to your email.

---
 
## 📸 Sample Output

```
🌍 Welcome to Satellite Visibility Notifier!

Enter your city or location (e.g., Mumbai): New York
Enter number of days to check (e.g., 1–5): 3

Available Satellites:
1. ISS (ZARYA)
2. Hubble Space Telescope
...

Choose a satellite (1–10): 1

📡 Fetching visible passes for ISS (ZARYA) over New York...

🛰️ ISS (ZARYA) Visible Passes over New York:

Pass 1:
  Start Time : 2025-07-04 01:24:00 UTC
  Duration   : 385 seconds
  Max Elev.  : 67°
  Brightness : -2.7
  ---
```

---

## 🚀 Features

- 🌆 Enter any city and get exact latitude/longitude
- 🛰️ Select from well-known satellites (ISS, Starlink, Hubble, etc.)
- 📅 Choose how many days ahead to check (up to 10)
- 📬 Optional email report via Gmail
- ✅ Clean, modular, beginner-friendly code

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Krishna-Wagh/satellite-visibility-notifier.git
cd satellite-visibility-notifier
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Set up `.env` file with your API keys

Create a file named `.env` in the root folder with the following content:

```
N2YO_API_KEY=your_n2yo_api_key
OPENCAGE_API_KEY=your_opencage_api_key
EMAIL=your_gmail_address@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

> ⚠️ Use a **Gmail App Password** instead of your real Gmail password.  
> Generate one here: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)

### 4. Run the script

```bash
python main.py
```

---

## 🛠 Customize for Yourself

| What You Want to Change      | How to Do It                        | File       |
|-----------------------------|-------------------------------------|------------|
| Add or remove satellites    | Edit the `SATELLITES` dictionary   | `main.py`  |
| Change number of passes     | Edit slicing logic (e.g. `passes[:5]`) | `main.py`  |
| Change email content/style  | Modify the `content` string         | `main.py`  |
| Replace geocoder service    | Update the `get_coordinates()` logic | `geocode.py` |

---

## 📁 File Structure

```
satellite-visibility-notifier/
├── main.py              # Main logic
├── n2yo_api.py          # Fetch satellite passes
├── geocode.py           # Convert city to lat/lon
├── email_sender.py      # Email reporting
├── requirements.txt     # Python dependencies
├── .env                 # Your secrets (not tracked)
└── README.md            # You're reading it!
```

---

## 💡 Ideas for Future Features

- 🌐 Web version using Streamlit or Flask
- 📊 Pass duration visualization
- 📲 Telegram/Discord bot version
- 📅 Downloadable calendar of upcoming passes

---

## 🙌 Credits

- [N2YO API](https://www.n2yo.com/api/)
- [OpenCage Geocoder](https://opencagedata.com/)
- Built by [Krishna Wagh](https://github.com/Krishna-Wagh)

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and share.

MIT License  
© 2025 Krishna Wagh
