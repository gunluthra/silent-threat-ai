import streamlit as st
import time

st.set_page_config(page_title="Silent Threat AI", layout="centered")

st.title("🛡 Silent Threat AI – Defence Surveillance System")
st.caption("Real-time Behavioural Anomaly Detection")

# Model logic (AI brain)
if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

idle_time = int(time.time() - st.session_state.last_activity)

if idle_time < 5:
    threat = "GREEN"
    reason = "Normal activity detected"
elif idle_time < 15:
    threat = "YELLOW"
    reason = "Suspicious inactivity"
else:
    threat = "RED"
    reason = "Silent threat detected"

# UI display
st.subheader(f"🟢 Threat Level: {threat}")
st.write(f"**Reason:** {reason}")
st.write(f"**Last activity detected:** {idle_time} seconds ago")

# Simulate activity
if st.button("Simulate Activity"):
    st.session_state.last_activity = time.time()
    st.success("Activity registered")
