import streamlit as st
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from ml_model import predict_threat
import pandas as pd
import numpy as np
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Silent Threat AI", layout="centered")

# ----------------------------------------------------
# TITLE
# ----------------------------------------------------
st.title("🛡 Silent Threat AI – Defence Surveillance System")
st.caption("Real-time Behavioural Anomaly Detection")

# Auto refresh (only once)
st_autorefresh(interval=4000, limit=None, key="refresh")

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------
if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------------------------------
# ZONE SELECTION
# ----------------------------------------------------
zone = st.selectbox(
    "📍 Surveillance Zone",
    ["Border Post", "Military Base", "Ammunition Depot"]
)

# ----------------------------------------------------
# ACTIVITY BUTTON
# ----------------------------------------------------
if st.button("Simulate Activity"):
    st.session_state.last_activity = time.time()
    st.success("Activity registered")

# ----------------------------------------------------
# TIME DIFFERENCE
# ----------------------------------------------------
time_diff = int(time.time() - st.session_state.last_activity)

# ----------------------------------------------------
# ML THREAT PREDICTION
# ----------------------------------------------------
level = predict_threat(time_diff)

if level == "GREEN":
    reason = "Normal activity detected"
    confidence = 20
elif level == "YELLOW":
    reason = "Suspicious inactivity detected"
    confidence = 60
else:
    reason = "Silent threat detected due to inactivity"
    confidence = 95

st.markdown("---")

# ----------------------------------------------------
# THREAT STATUS
# ----------------------------------------------------
if level == "GREEN":
    st.success(f"🟢 Threat Level: {level}")
elif level == "YELLOW":
    st.warning(f"🟡 Threat Level: {level}")
else:
    st.error(f"🔴 Threat Level: {level}")

st.write(f"**Reason:** {reason}")
st.write(f"⏱️ Last activity detected: {time_diff} seconds ago")

st.progress(confidence)
st.caption(f"🤖 AI Threat Confidence: {confidence}%")

# ----------------------------------------------------
# COMMAND CENTER PANEL
# ----------------------------------------------------
st.markdown("### 🛰 Command Center Status")

col1, col2, col3 = st.columns(3)

col1.metric("Threat Level", level)
col2.metric("Zone", zone)
col3.metric("Inactivity (sec)", time_diff)

st.markdown("---")

# ----------------------------------------------------
# MULTI FACTOR RISK SCORE
# ----------------------------------------------------
zone_risk = {
    "Border Post": 20,
    "Military Base": 40,
    "Ammunition Depot": 60
}

risk_score = confidence + zone_risk[zone] + (time_diff * 2)

st.metric("⚠️ Threat Risk Score", risk_score)

# ----------------------------------------------------
# COMMAND CENTER ALERT
# ----------------------------------------------------
if risk_score > 120:
    st.error("🚨 CRITICAL ALERT — Immediate response required")
elif risk_score > 80:
    st.warning("⚠️ Elevated threat detected")

# ----------------------------------------------------
# ESCALATION MESSAGE
# ----------------------------------------------------
if level == "RED":
    st.error("🚨 Immediate Action Required: Notify Command Center")
elif level == "YELLOW":
    st.warning("⚠️ Monitoring closely for escalation")
else:
    st.success("✅ Area Secure")

# ----------------------------------------------------
# ALERT HISTORY
# ----------------------------------------------------
log_entry = f"{datetime.now().strftime('%H:%M:%S')} — {zone} — {level} — {confidence}%"

if not st.session_state.history or st.session_state.history[-1] != log_entry:
    st.session_state.history.append(log_entry)

st.markdown("---")
st.subheader("📜 Alert History (Latest 5)")

for entry in st.session_state.history[-5:][::-1]:
    st.write(entry)

# ----------------------------------------------------
# THREAT ANALYSIS CHART
# ----------------------------------------------------
st.markdown("---")
st.subheader("📡 Threat Analysis")

radar_data = {
    "Inactivity": min(time_diff * 5, 100),
    "Zone Risk": zone_risk[zone],
    "AI Confidence": confidence,
    "System Escalation": risk_score % 100
}

radar_df = pd.DataFrame.from_dict(radar_data, orient="index", columns=["Score"])

st.bar_chart(radar_df)

# ----------------------------------------------------
# RISK TREND
# ----------------------------------------------------
if "risk_data" not in st.session_state:
    st.session_state.risk_data = []

st.session_state.risk_data.append(risk_score)

chart_data = pd.DataFrame(st.session_state.risk_data, columns=["Risk"])

st.subheader("📊 Live Risk Trend")
st.line_chart(chart_data)

# ----------------------------------------------------
# ZONE OVERVIEW
# ----------------------------------------------------
zone_status = {
    "Border Post": np.random.randint(20,100),
    "Military Base": np.random.randint(20,100),
    "Ammunition Depot": np.random.randint(20,100)
}

st.subheader("📍 Zone Threat Overview")
st.bar_chart(zone_status)

# ----------------------------------------------------
# AI EXPLANATION
# ----------------------------------------------------
with st.expander("🧠 AI Decision Explanation"):
    st.write(f"""
    Threat level **{level}** determined from:

    - Inactivity time: {time_diff} seconds
    - Defence zone risk weighting
    - Machine learning classification
    - Final calculated risk score: {risk_score}
    """)

# ----------------------------------------------------
# FUTURE EXPANSION
# ----------------------------------------------------
with st.expander("🚀 Future System Integration"):
    st.write("""
    Planned upgrades:

    - Real-time camera motion detection
    - Behaviour tracking from keyboard/mouse
    - NLP-based threat message detection
    - Drone surveillance integration
    - Predictive threat forecasting
    """)

# ----------------------------------------------------
# WEBCAM
# ----------------------------------------------------
st.markdown("---")
st.subheader("📷 Live Surveillance Camera")

webrtc_streamer(
    key="camera",
    media_stream_constraints={"video": True, "audio": False}
)

# ----------------------------------------------------
# SYSTEM EXPLANATION
# ----------------------------------------------------
with st.expander("🧠 How Silent Threat AI Works"):
    st.write("""
    • Monitors inactivity patterns instead of motion  
    • Detects behavioural anomalies over time  
    • Assigns risk levels (GREEN / YELLOW / RED)  
    • Uses machine learning for threat classification  
    • Calculates multi-factor defence risk score  
    • Provides explainable AI insights for decision makers  
    """)
