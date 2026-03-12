import streamlit as st
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from ml_model import predict_threat

st.set_page_config(page_title="Silent Threat AI", layout="centered")



st.title("🛡 Silent Threat AI – Defence Surveillance System")
st.caption("Real-time Behavioural Anomaly Detection")


st_autorefresh(interval=2000, limit=None, key="refresh")


if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

if "history" not in st.session_state:
    st.session_state.history = []


zone = st.selectbox(
    "📍 Surveillance Zone",
    ["Border Post", "Military Base", "Ammunition Depot"]
)


if st.button("Simulate Activity"):
    st.session_state.last_activity = time.time()
    st.success("Activity registered")


time_diff = int(time.time() - st.session_state.last_activity)


if time_diff < 5:
    level = "GREEN"
    reason = "Normal activity detected"
    confidence = 20
elif time_diff < 15:
    level = "YELLOW"
    reason = "Suspicious inactivity detected"
    confidence = 60
else:
    level = "RED"
    reason = "Silent threat detected due to inactivity"
    confidence = 95

st.markdown("---")

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


if level == "RED":
    st.error("🚨 Immediate Action Required: Notify Command Center")
elif level == "YELLOW":
    st.warning("⚠️ Monitoring closely for escalation")
else:
    st.success("✅ Area Secure")

log_entry = f"{datetime.now().strftime('%H:%M:%S')} — {zone} — {level} — {confidence}%"
if not st.session_state.history or st.session_state.history[-1] != log_entry:
    st.session_state.history.append(log_entry)

st.markdown("---")
st.subheader("📜 Alert History (Latest 5)")

for entry in st.session_state.history[-5:][::-1]:
    st.write(entry)


with st.expander("🧠 How Silent Threat AI Works"):
    st.write("""
    • Monitors inactivity patterns instead of motion  
    • Detects behavioural anomalies over time  
    • Assigns risk levels (GREEN / YELLOW / RED)  
    • Provides explainable confidence scores  
    • Logs alerts for forensic analysis  
    """)
