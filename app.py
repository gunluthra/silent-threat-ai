import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Silent Threat AI",
    layout="centered"
)

st.title("🛡 Silent Threat AI – Defence Surveillance System")
st.caption("Behaviour-based Threat Detection")

# Session state to track last activity
if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

# Calculate inactivity time
inactive_time = int(time.time() - st.session_state.last_activity)

# Threat logic
if inactive_time < 5:
    threat = "GREEN"
    message = "Normal activity detected"
elif inactive_time < 15:
    threat = "YELLOW"
    message = "Suspicious delay in activity"
else:
    threat = "RED"
    message = "Silent threat detected due to inactivity"

# Display result
st.subheader(f"Threat Level: {threat}")
st.write(message)
st.write(f"Last activity detected: {inactive_time} seconds ago")

# Button to simulate activity
if st.button("Simulate Activity"):
    st.session_state.last_activity = time.time()
    st.success("Activity registered")
