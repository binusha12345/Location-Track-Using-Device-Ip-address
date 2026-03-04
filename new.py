import requests
import folium
from folium.plugins import Fullscreen, Geocoder

def get_my_location():
    try:
        # 1. IP එක මගින් දත්ත ලබා ගැනීම
        response = requests.get('http://ip-api.com/json/')
        data = response.json()
        
        if data.get('status') == 'success':
            lat = data.get('lat')
            lng = data.get('lon')
            city = data.get('city')
            isp = data.get('isp')
            
            print(f"✅ Detected: {city} | ISP: {isp}")

            # 2. සිතියම සෑදීම
            my_map = folium.Map(location=[lat, lng], zoom_start=12)

            # 3. Google Satellite View එකතු කිරීම
            folium.TileLayer(
                tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                attr='Google',
                name='Google Satellite',
                overlay=False,
                control=True
            ).add_to(my_map)
            
            folium.TileLayer('openstreetmap', name='Normal View').add_to(my_map)

            # 4. Marker එකක් තැබීම
            folium.Marker(
                [lat, lng], 
                popup=f"City: {city}<br>ISP: {isp}",
                tooltip="Click for details",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(my_map)

            # 5. Fullscreen button එකතු කිරීම
            Fullscreen().add_to(my_map)

            # 6. සෙවුම් යන්ත්‍රය (Search Bar) - මෙහිදී Geocoder භාවිතා කර ඇත
            # මෙය භාවිතා කර ඔබට සූරියවැව (Sooriyawewa) ලෙස search කළ හැක
            Geocoder().add_to(my_map)

            # Layer Control එකතු කිරීම (Satellite/Normal මාරු කිරීමට)
            folium.LayerControl().add_to(my_map)

            # 7. සිතියම Save කිරීම
            my_map.save("final_location_map.html")
            print("🚀 Map saved as final_location_map.html")
            
        else:
            print("❌ Error: API could not detect your location.")
            
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

get_my_location()