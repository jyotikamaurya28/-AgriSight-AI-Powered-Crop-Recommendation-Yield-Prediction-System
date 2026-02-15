import streamlit as st
import pandas as pd
import joblib
import random
import sys
import os
import requests
from dotenv import load_dotenv
import streamlit.components.v1 as components

# --------------------------------------------------
#  BASE DIRECTORY ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# --------------------------------------------------
# LOAD ENV VARIABLES
# --------------------------------------------------
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="AgriSight", layout="wide")
st.title("🌾 AgriSight – Smart Crop & Risk Advisor")

st.markdown(
    "Enter your details to find the **best crop**, "
    "**success probability**, and get **smart farming advice**."
)

# --------------------------------------------------
# SAFE MODEL LOADING
# --------------------------------------------------
def load_models():
    try:
        crop_model_path = os.path.join(BASE_DIR, "models", "crop_recommendation_model.pkl")
        success_model_path = os.path.join(BASE_DIR, "models", "success_prediction_model.pkl")

        crop_model = joblib.load(crop_model_path)
        success_model = joblib.load(success_model_path)

        return crop_model, success_model

    except Exception as e:
        st.error("❌ Model files not found. Check 'models' folder in GitHub.")
        st.stop()

crop_model, success_model = load_models()

# --------------------------------------------------
# IMPORT LLM SAFELY
# --------------------------------------------------
try:
    from llm.llm_advice import get_advice
except:
    def get_advice(crop, date, district):
        return "AI advice module not configured."

# --------------------------------------------------
# DISTRICTS
# --------------------------------------------------
districts = [
    "Agra","Aligarh","Ambedkar Nagar","Amethi","Amroha","Auraiya",
    "Azamgarh","Baghpat","Bahraich","Ballia","Balrampur","Banda",
    "Barabanki","Bareilly","Basti","Bhadohi","Bijnor","Budaun",
    "Bulandshahr","Chandauli","Chitrakoot","Deoria","Etah","Etawah",
    "Faizabad","Farrukhabad","Fatehpur","Firozabad",
    "Gautam Buddha Nagar","Ghaziabad","Ghazipur","Gonda",
    "Gorakhpur","Hamirpur","Hapur","Hardoi","Hathras","Jalaun",
    "Jaunpur","Jhansi","Kannauj","Kanpur Dehat","Kanpur Nagar",
    "Kasganj","Kaushambi","Kushinagar","Lakhimpur Kheri",
    "Lalitpur","Lucknow","Maharajganj","Mahoba","Mainpuri",
    "Mathura","Mau","Meerut","Mirzapur","Moradabad",
    "Muzaffarnagar","Pilibhit","Pratapgarh","Rae Bareli",
    "Rampur","Saharanpur","Sambhal","Sant Kabir Nagar",
    "Shahjahanpur","Shamli","Shravasti","Siddharth Nagar",
    "Sitapur","Sonbhadra","Sultanpur","Unnao","Varanasi"
]

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    date = st.date_input("📅 Farming Start Date")

with col2:
    district = st.selectbox("🏞️ Select District", districts)

# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------
if st.button("🔍 Predict Crop & Risk"):

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
    crop = crop_model.predict(input_df)[0]

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

    st.subheader("🌱 Recommended Crop")
    st.success(crop.upper())

    st.subheader("📊 Success Probability")

    if success_prob > 0.7:
        st.success(f"✅ High Success Chance ({success_prob:.2f})")
    elif success_prob > 0.4:
        st.warning(f"⚠️ Moderate Success Chance ({success_prob:.2f})")
    else:
        st.error(f"❌ High Risk ({success_prob:.2f})")

    st.subheader("💡 Smart Farming Advice")

    with st.spinner("Generating advice..."):
        advice = get_advice(crop, date, district)

    st.info(advice)

# --------------------------------------------------
# WEATHER SECTION (SAFE)
# --------------------------------------------------
st.markdown("---")
st.header("🌦️ Weather Forecast")

if not API_KEY:
    st.warning("Weather API key not configured in Render.")
else:
    selected_district = st.selectbox("Select district for weather", districts)
    days = st.slider("Forecast Days", 1, 5, 3)

    if st.button("Get Weather"):
        try:
            url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={selected_district}&days={days}"
            res = requests.get(url)

            if res.status_code == 200:
                data = res.json()

                for day in data['forecast']['forecastday']:
                    st.write(f"📅 {day['date']}")
                    st.write(f"🌡️ Max Temp: {day['day']['maxtemp_c']}°C")
                    st.write(f"🌡️ Min Temp: {day['day']['mintemp_c']}°C")
                    st.write(f"☁️ Condition: {day['day']['condition']['text']}")
                    st.write("---")
            else:
                st.error("Failed to fetch weather data.")

        except:
            st.error("Weather API error.")

# --------------------------------------------------
# AGRIBOT
# --------------------------------------------------
st.markdown("---")
st.header("🤖 AgriBot Assistant")

components.html(
"""
<div id="bp-web-widget"></div>
<script src="https://cdn.botpress.cloud/webchat/v3.0/inject.js"></script>
<script src="https://files.bpcontent.cloud/2025/06/08/07/20250608074849-WSAX4Y9N.js"></script>
""",
height=500
)
