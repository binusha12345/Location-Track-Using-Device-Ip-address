<div align="center">

# 🌍 Location Track — Using Device IP Address

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x"/>
  <img src="https://img.shields.io/badge/Folium-0.17+-green?style=for-the-badge&logo=folium&logoColor=white" alt="Folium"/>
  <img src="https://img.shields.io/badge/OpenStreetMap-API-orange?style=for-the-badge&logo=openstreetmap&logoColor=white" alt="OpenStreetMap"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Active"/>
</p>

<p align="center">
  <b>📍 Instantly detect your current location using your IP address & visualize it on an interactive map!</b>
</p>

---

</div>

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧭 **Auto Location Detection** | Fetches your public IP & pinpoints your city coordinates |
| 🗺️ **Dual Map Views** | Switch between **Normal Street View** & **Google Satellite View** |
| 📍 **Custom Marker** | Red marker with popup showing your **City** & **ISP** info |
| 🔍 **Built-in Search** | Use the search box to find & navigate to any location |
| 🖥️ **Fullscreen Mode** | One-click fullscreen for immersive map experience |
| 📂 **Saves as HTML** | Generates a portable `final_location_map.html` file |
| ⚡ **Fast & Lightweight** | Single script — no complex setup required |

---

## 🚀 How It Works

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Your IP     │────▶│  ip-api.com API  │────▶│  Latitude/Long.  │
└─────────────┘     └──────────────────┘     └────────┬─────────┘
                                                       │
                                                       ▼
┌─────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Save HTML   │◀────│  Folium Map      │◀────│  Custom Marker   │
│  (Portable)  │     │  + Tile Layers   │     │  + Popup Info    │
└─────────────┘     └──────────────────┘     └──────────────────┘
```

---

## 📦 Installation

### ✅ Prerequisites

Make sure you have **Python 3.x** installed on your system.

```bash
# Check your Python version
python --version
```

### 📥 Install Required Packages

```bash
pip install requests folium
```

| Package | Purpose |
|---------|---------|
| `requests` 🌐 | Makes HTTP request to IP geolocation API |
| `folium` 🗺️ | Creates interactive Leaflet-based maps |

---

## ▶️ Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/binusha12345/Location-Track-Using-Device-Ip-address.git
cd Location-Track-Using-Device-Ip-address
```

### 2️⃣ Install Dependencies

```bash
pip install requests folium
```

### 3️⃣ Run the Script

```bash
python new.py
```

### 4️⃣ Open the Map

Open the generated `final_location_map.html` file in your browser:

```bash
# Windows
start final_location_map.html

# macOS
open final_location_map.html

# Linux
xdg-open final_location_map.html
```

---

## 🖼️ Screenshots

<div align="center">
  <table>
    <tr>
      <td align="center">
        <b>🗺️ Normal Street View</b>
      </td>
      <td align="center">
        <b>🛰️ Google Satellite View</b>
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png" alt="Street View" width="300"/>
      </td>
      <td>
        <img src="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png" alt="Satellite View" width="300"/>
      </td>
    </tr>
  </table>
  <p><i>💡 <b>Tip:</b> Use the layer control button (top-right corner) to switch between views!</i></p>
</div>

---

## 🧪 Code Walkthrough

Here's the core logic of the script:

```python
# 1️⃣ Get location data from IP
response = requests.get('http://ip-api.com/json/')
data = response.json()

# 2️⃣ Extract coordinates
lat = data['lat']
lng = data['lon']
city = data['city']
isp = data['isp']

# 3️⃣ Create interactive map
my_map = folium.Map(location=[lat, lng], zoom_start=12)

# 4️⃣ Add Google Satellite tile layer
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr='Google',
    name='Google Satellite'
).add_to(my_map)

# 5️⃣ Place a marker with popup
folium.Marker(
    [lat, lng],
    popup=f"City: {city}<br>ISP: {isp}",
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(my_map)

# 6️⃣ Save to HTML
my_map.save("final_location_map.html")
```

---

## 📋 Dependencies

| Dependency | Version | Description |
|------------|---------|-------------|
| 🐍 `Python` | 3.x+ | Core runtime |
| 🌐 `requests` | Latest | HTTP library for API calls |
| 🗺️ `folium` | 0.17+ | Map visualization library |

---

## 🌐 API Reference

This project uses the free **[ip-api.com](http://ip-api.com/json/)** API:

| Endpoint | Method | Response Format |
|----------|--------|-----------------|
| `http://ip-api.com/json/` | `GET` | JSON |

### Sample Response

```json
{
  "status": "success",
  "country": "Sri Lanka",
  "city": "Colombo",
  "lat": 6.9271,
  "lon": 79.8612,
  "isp": "Sri Lanka Telecom",
  "org": "SLT Broadband",
  "query": "123.231.xxx.xxx"
}
```

> ⚠️ **Note:** Free API has a limit of **45 requests per minute**. For most personal use this is more than enough.

---

## 🤝 Contributing

Contributions are always welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a new branch (`git checkout -b feature/awesome-feature`)
3. 💾 Commit your changes (`git commit -m 'Add awesome feature'`)
4. 📤 Push to the branch (`git push origin feature/awesome-feature`)
5. 🔁 Open a Pull Request

---

## 📄 License

<div align="center">

**MIT License** 🎯

Copyright © 2026 [Binusha](https://github.com/binusha12345)

*Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:*

*The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.*

</div>

---

<div align="center">

### ⭐ **Show some love!**  

If you find this project useful, **star** the repository on GitHub!  

[![GitHub stars](https://img.shields.io/github/stars/binusha12345/Location-Track-Using-Device-Ip-address?style=social)](https://github.com/binusha12345/Location-Track-Using-Device-Ip-address)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/binusha12345">Binusha</a>
</p>

</div>