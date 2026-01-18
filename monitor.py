import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="HealthPulse | Observability", layout="wide")

st.title("🛰️ HealthPulse: System Observability Dashboard")
st.markdown("### Real-time Monitoring for Intact Software Services")

# 1. Logic: Simulated System Check
def check_system_health():
    # In a real app, this would ping a URL or Database
    status = "Online" if random.random() > 0.1 else "Offline"
    response_time = random.randint(20, 500)
    return status, response_time

# 2. Application State
if 'logs' not in st.session_state:
    st.session_state.logs = []

if st.button('Run Manual System Check'):
    status, r_time = check_system_health()
    st.session_state.logs.append({"Service": "Core-Claims-Engine", "Status": status, "Latency": r_time})

# 3. Visualizing Observability
df = pd.DataFrame(st.session_state.logs)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("System Status Logs")
    if not df.empty:
        st.dataframe(df.tail(10), use_container_width=True)

with col2:
    st.subheader("Alerting Logic")
    if not df.empty:
        latest = df.iloc[-1]
        if latest['Status'] == "Offline":
            st.error(f"🚨 CRITICAL: {latest['Service']} is DOWN!")
        elif latest['Latency'] > 300:
            st.warning(f"⚠️ SLOW: {latest['Service']} high latency detected.")
        else:
            st.success(f"✅ {latest['Service']} is Healthy")
