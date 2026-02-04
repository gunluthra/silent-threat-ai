import streamlit as st
import time

st.set_page_config(page_title="Silent Threat AI", layout="centered")

st.title("🛡️ Silent Threat AI – Defence Surveillance System")
st.caption("Real-time Behavioural Anomaly Detection")

# Threat logic (simulation)
current_time = int(time.time()) % 30

if current_time < 10:
    risk = "GREEN"
    reason = "Normal activity detected"
    color = "green"
elif current_time < 20:
    risk = "YELLOW"
    reason = "Suspicious delay in activity"
    color = "orange"
else:
    risk = "RED"
    reason = "Silent threat detected due to inactivity"
    color = "red"

st.markdown(f"## 🟢 Threat Level: :{color}[{risk}]")
st.write(f"**Reason:** {reason}")
st.write(f"**Last activity detected:** {current_time} seconds ago")

# Alert history
st.markdown("### 📜 Alert History")
if "history" not in st.session_state:
    st.session_state.history = []

log = f"{time.strftime('%H:%M:%S')} – {risk}"
if not st.session_state.history or st.session_state.history[-1] != log:
    st.session_state.history.append(log)

st.session_state.history = st.session_state.history[-5:]

for item in reversed(st.session_state.history):
    st.write(item)
