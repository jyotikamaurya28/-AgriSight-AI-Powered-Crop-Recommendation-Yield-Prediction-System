import streamlit as st
import pandas as pd
import joblib
import random
import sys
import os
import requests
from dotenv import load_dotenv
import streamlit.components.v1 as components

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from llm.llm_advice import get_advice


# Load trained models
crop_model = joblib.load("models/crop_recommendation_model.pkl")
success_model = joblib.load("models/success_prediction_model.pkl")

# UI Title
st.set_page_config(page_title="AgriSight")
st.title("🌾 AgriSight – Smart Crop & Risk Advisor")
st.markdown("Enter your details to find the **best crop**, **risk level**, and get **smart farming tips**.")
districts = [
    "Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha", "Auraiya", "Azamgarh",
    "Baghpat", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly",
    "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr", "Chandauli", "Chitrakoot",
    "Deoria", "Etah", "Etawah", "Faizabad", "Farrukhabad", "Fatehpur", "Firozabad",
    "Gautam Buddha Nagar", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur",
    "Hapur", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj",
    "Kanpur Dehat", "Kanpur Nagar", "Kasganj", "Kaushambi", "Kushinagar",
    "Lakhimpur Kheri", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", "Mainpuri",
    "Mathura", "Mau", "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar",
    "Pilibhit", "Pratapgarh", "Rae Bareli", "Rampur", "Saharanpur", "Sambhal",
    "Sant Kabir Nagar", "Shahjahanpur", "Shamli", "Shravasti", "Siddharth Nagar",
    "Sitapur", "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"
]
# Inputs from farmer
col1, col2 = st.columns(2)
with col1:
    date = st.date_input("📅 Select your Farming Start Date")
with col2:
    district = st.selectbox("🏞️ Select Your District Name", options=districts)




# When farmer clicks "Predict"
if st.button("🔍 Predict Crop and Advice"):
    if not district:
        st.warning("Please enter your district.")
    else:
        # Simulate realistic input features (or replace with real data/API later)
        weather_soil = {
            "N": random.randint(20, 90),
            "P": random.randint(5, 40),
            "K": random.randint(5, 40),
            "temperature": round(random.uniform(22, 34), 2),
            "humidity": round(random.uniform(40, 80), 2),
            "ph": round(random.uniform(5.5, 7.5), 2),
            "rainfall": round(random.uniform(50, 200), 2),
        }

        input_df = pd.DataFrame([weather_soil])

        # Predict best crop
        crop = crop_model.predict(input_df)[0]

        # Predict success/failure
        success_input = pd.DataFrame([{
            "Area": random.randint(300, 800),
            "Production": random.randint(400, 1500),
            "Zn %": random.uniform(0.5, 1.5),
            "Fe%": random.uniform(1.0, 3.0),
            "Cu %": random.uniform(0.2, 0.8),
            "Mn %": random.uniform(0.5, 1.5),
            "B %": random.uniform(0.2, 0.8),
            "S %": random.uniform(1.0, 3.0)
        }])

        success_prob = success_model.predict_proba(success_input)[0][1]

        # Display predictions
        st.subheader("🌱 Recommended Crop")
        st.success(f"**{crop.upper()}**")

        st.subheader("📊 Success Prediction")
        if success_prob > 0.7:
            st.info(f"✅ Good chance of success ({success_prob:.2f})")
        elif success_prob > 0.4:
            st.warning(f"⚠️ Moderate chance of success ({success_prob:.2f})")
        else:
            st.error(f"❌ High risk of failure ({success_prob:.2f})")

        # AI Advice
        st.subheader("💡 Smart Farming Tips")
        with st.spinner("Getting expert tips..."):
            advice = get_advice(crop, date, district)
        st.info(advice)

# Load environment variables from .env file
load_dotenv()

# Access your weather API key
API_KEY = os.getenv("WEATHER_API_KEY")

# Your WeatherAPI Key
API_KEY = "6b8c248a30824ecf94962928250906"

# List of Uttar Pradesh Districts (you can expand this)
districts = [
    "Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha", "Auraiya", "Azamgarh",
    "Baghpat", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly",
    "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr", "Chandauli", "Chitrakoot",
    "Deoria", "Etah", "Etawah", "Faizabad", "Farrukhabad", "Fatehpur", "Firozabad",
    "Gautam Buddha Nagar", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur",
    "Hapur", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj",
    "Kanpur Dehat", "Kanpur Nagar", "Kasganj", "Kaushambi", "Kushinagar",
    "Lakhimpur Kheri", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", "Mainpuri",
    "Mathura", "Mau", "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar",
    "Pilibhit", "Pratapgarh", "Rae Bareli", "Rampur", "Saharanpur", "Sambhal",
    "Sant Kabir Nagar", "Shahjahanpur", "Shamli", "Shravasti", "Siddharth Nagar",
    "Sitapur", "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"
]


st.title("🌦️ District-wise Weather Forecast & Alerts (Uttar Pradesh)")
selected_district = st.selectbox("Select your district", sorted(districts))
days = st.slider("Forecast days", 1, 8, 3)

if st.button("Get Weather Forecast"):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={selected_district}&days={days}&alerts=yes"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        st.subheader(f"📍 Weather Forecast for {selected_district}")
        for day in data['forecast']['forecastday']:
            st.markdown(f"""
            **Date:** {day['date']}  
            🌡️ Max: {day['day']['maxtemp_c']}°C  
            🌡️ Min: {day['day']['mintemp_c']}°C  
            ☁️ Condition: {day['day']['condition']['text']}  
            💧 Rain: {day['day']['daily_chance_of_rain']}%  
            """)
        
        # Show alerts if available
        if data.get("alerts", {}).get("alert"):
            st.warning("🚨 Weather Alerts:")
            for alert in data["alerts"]["alert"]:
                st.markdown(f"**{alert['headline']}** - {alert['desc']}")
        else:
            st.success("✅ No weather alerts found.")
    else:
        st.error("Failed to fetch weather data. Check your API key or try again.")
st.title("🤖 AgriBot - Your Farming Assistant")


components.html(
"""
    <div id="bp-web-widget"></div>
    <script src="https://cdn.botpress.cloud/webchat/v3.0/inject.js"></script>
    <script src="https://files.bpcontent.cloud/2025/06/08/07/20250608074849-WSAX4Y9N.js"></script>
    """,height=600, width=600)
