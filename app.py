import streamlit as st
import time
from datetime import datetime

st.set_page_config(
    page_title="Silent Threat AI",
    layout="wide"
)

# ------------------ STATE ------------------
if "last_activity" not in st.session_state:
    st.session_state.last_activity = time.time()

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------ FUNCTIONS ------------------
def get_threat_level(last_time):
    diff = int(time.time() - last_time)

    if diff < 5:
        return "GREEN", "Normal activity detected"
    elif diff < 12:
        return "YELLOW", "Suspicious inactivity detected"
    else:
        return "RED", "Silent threat detected"

def log_event(level):
    st.session_state.history.append(
        f"{datetime.now().strftime('%H:%M:%S')} — {level}"
    )

# ------------------ UI ------------------
st.title("🛡 Silent Threat AI – Defence Surveillance System")
st.caption("Real-time Behavioural Anomaly Detection")

level, reason = get_threat_level(st.session_state.last_activity)

# ------------------ COLORS ------------------
if level == "GREEN":
    st.success(f"🟢 Threat Level: {level}\n\nReason: {reason}")
elif level == "YELLOW":
    st.warning(f"🟡 Threat Level: {level}\n\nReason: {reason}")
else:
    st.error(f"🔴 Threat Level: {level}\n\nReason: {reason}")

st.write(f"Last activity detected: **{int(time.time() - st.session_state.last_activity)} seconds ago**")

# ------------------ BUTTON ------------------
if st.button("Simulate Activity"):
    st.session_state.last_activity = time.time()
    log_event(level)
    st.success("Activity registered")

# ------------------ HISTORY ------------------
st.divider()
st.subheader("📜 Alert History")

if st.session_state.history:
    for h in reversed(st.session_state.history):
        st.write(h)
else:
    st.info("No alerts yet")
