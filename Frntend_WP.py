import streamlit as st
from streamlit_lottie import st_lottie
import json
import pickle
import time

# ---------------------------
# Helper to load Lottie files
# ---------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# ---------------------------
# Page Configuration & Styling
# ---------------------------
st.set_page_config(page_title="Weather Prediction", layout="centered")



# ---------------------
# Title (Bold + Normal)
# ---------------------
st.markdown('<h1 style="text-align: center; color: #ffffff;">Weather Forecast using Pollution Data</h1>', unsafe_allow_html=True)


# ---------------------
# Lottie Animations
# ---------------------
col1, col2 = st.columns(2)
with col1:
    st.header("What is Air Pollution?")
    st.write(
        "Air pollution is the contamination of air by harmful substances including gases, dust, and smoke. "
        "It affects human health, the environment, and the planet's climate."
    )
with col2:
    lottie_pollution = load_lottiefile("E:/Akira/Project!!/Loading.json")
    st_lottie(lottie_pollution, height=300)

# --------------------------
# Causes of Air Pollution
# --------------------------
with st.expander("🌪️ Causes of Air Pollution"):
    st.write("""
    - Vehicle emissions
    - Industrial discharges
    - Burning of fossil fuels
    - Agricultural activities
    - Indoor pollution (chemicals, poor ventilation)
    """)

# --------------------------
# Effects of Air Pollution
# --------------------------
with st.expander("⚠️ Effects on Health & Environment"):
    lottie_effect = load_lottiefile("E:/Akira/Project!!/Air.json")
    st_lottie(lottie_effect, height=250)
    st.write("""
    - Respiratory and heart problems
    - Global warming and climate change
    - Acid rain and ecosystem damage
    """)

# --------------------------
# Precautions and Prevention
# --------------------------
with st.expander("🛡️ How to Prevent?"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        - Use public transport
        - Plant more trees
        - Use clean energy
        - Avoid burning waste
        - Regular vehicle maintenance
        """)
    with col2:
        lottie_precautions = load_lottiefile("E:/Akira/Project!!/Precau.json")
        st_lottie(lottie_precautions, height=250)

# ---------------------
# Weather Prediction UI
# ---------------------
st.markdown("---")
st.subheader("📊 Predict Weather-Related Metric")

# Load ML model
with open("E:/Akira/Project!!/ModelRegr.pkl", "rb") as file3:
    regressor = pickle.load(file3)

# Inputs
a = st.number_input("SO2 (μg/m³):")
b = st.number_input("CO (mg/m³):")
c = st.number_input("NO (μg/m³):")
d = st.number_input("NO2 (μg/m³):")
e = st.number_input("NOx (μg/m³):")
f = st.number_input("NH3 (μg/m³):")
g = st.number_input("O3 (μg/m³):")
h = st.number_input("Wind Speed (m/s):")
i = st.number_input("Wind Direction (°):")
j = st.number_input("Relative Humidity (%):")
k = st.number_input("Solar Radiation (W/m²):")
l = st.number_input("Temperature (°C):")

# Predict Button
if st.button("Predict"):
    with st.spinner("⏳ Loading prediction..."):
        time.sleep(5)  # simulate processing delay
        input_data = [[a, b, c, d, e, f, g, h, i, j, k, l]]
        prediction = regressor.predict(input_data)
    st.success(f"🌤️ Predicted Value: {prediction[0]:.2f}")
