import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

# Seiten-Konfiguration
st.set_page_config(
    page_title="Fancy Dashboard",
    page_icon="✨",
    layout="wide"
)

# Custom CSS für besseres Aussehen
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f0f2f6, #ffffff);
    }
    .main > div {
        padding: 2rem;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.9);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Hauptüberschrift mit Animation
st.title("✨ Interaktives Dashboard ✨")
st.markdown("---")

# Seitenleisten-Menü
with st.sidebar:
    st.header("Einstellungen")
    name = st.text_input("Dein Name")
    alter = st.slider("Alter", 0, 100, 25)
    lieblingsfarbe = st.color_picker("Wähle deine Lieblingsfarbe", "#00ff00")

# Layout mit Spalten
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Interaktives Diagramm")
    # Beispieldaten generieren
    dates = pd.date_range(start='2025-01-01', end='2025-04-28', freq='D')
    values = np.random.randn(len(dates)).cumsum()
    df = pd.DataFrame({'Datum': dates, 'Wert': values})
    
    # Plotly-Diagramm
    fig = px.line(df, x='Datum', y='Wert', 
                  title='Entwicklung über Zeit',
                  template='plotly_white')
    fig.update_traces(line_color=lieblingsfarbe)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🎯 Fortschrittsanzeige")
    progress = st.progress(0)
    
    if st.button("Starte Animation"):
        for i in range(100):
            progress.progress(i + 1)
            time.sleep(0.01)
        st.balloons()

# Metriken-Bereich
st.markdown("---")
m1, m2, m3 = st.columns(3)

with m1:
    st.metric(label="Temperatur", value="24 °C", delta="1.2 °C")

with m2:
    st.metric(label="Luftfeuchtigkeit", value="65%", delta="-5%")

with m3:
    st.metric(label="Luftqualität", value="Gut", delta="↗")

# Interaktive Karte
st.markdown("---")
st.subheader("🗺️ Interaktive Karte")
df_map = pd.DataFrame({
    'lat': [48.1351, 52.5200, 53.5511],
    'lon': [11.5820, 13.4050, 9.9937],
    'name': ['München', 'Berlin', 'Hamburg']
})
st.map(df_map)

# Footer
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: gray;'>
        Dashboard erstellt von {name if name else 'Anonymous'} | Aktuelle Zeit: {datetime.now().strftime('%H:%M:%S')}
    </div>
""", unsafe_allow_html=True)