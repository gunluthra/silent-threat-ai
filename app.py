import streamlit as st
import time
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Silent Threat AI", layout="centered")

st.title("🛡 Silent Threat AI – Defence Surveillance System")
st.caption("Real-time Behavioural Anomaly Detection")
st_autorefresh(interval=2000, limit=None, key="refresh")
zone = st.selectbox(
    "📍 Surveillance Zone",
    ["Border Post", "Military Base", "Ammunition Depot"]
)

if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

if st.button("Simulate Activity"):
    st.session_state.last_activity = time.time()
    st.success("Activity registered")

time_diff = int(time.time() - st.session_state.last_activity)

if time_diff < 5:
    st.success("🟢 Threat Level: GREEN")
    st.write("Reason: Normal activity detected")
elif time_diff < 15:
    st.warning("🟡 Threat Level: YELLOW")
    st.write("Reason: Suspicious inactivity detected")
else:
    st.error("🔴 Threat Level: RED")
    st.write("Reason: Silent threat detected due to inactivity")

st.write(f"⏱️ Last activity detected: {time_diff} seconds ago")
if time_diff < 5:
    confidence = 20
elif time_diff < 15:
    confidence = 60
else:
    confidence = 95

st.progress(confidence)
st.caption(f"🤖 AI Threat Confidence: {confidence}%")




