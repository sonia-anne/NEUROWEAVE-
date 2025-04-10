
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="NEUROWEAVE | Hydrocephalus Nanotherapy", layout="wide")
st.title("💧 NEUROWEAVE | Nanodevice-Assisted Surgery for Hydrocephalus")

st.markdown("""
NEUROWEAVE is a curative platform for hydrocephalus using self-guided nanorobots that restore cerebrospinal fluid (CSF) flow, 
regenerate ependymal tissue, and eliminate the need for traditional shunt valves. 
Below is a simulation of ventricular pressure and CSF flow under different conditions.
""")

# Simulated data
days = list(range(0, 11))
csf_blocked = [25 + i*1.5 for i in days]
csf_valve = [25 - i*0.8 if i < 5 else 20 - (i-5)*0.3 for i in days]
csf_neuroweave = [25 - i*1.8 if i < 5 else 15 + 0.3*(i-5) for i in days]

fig = go.Figure()
fig.add_trace(go.Scatter(x=days, y=csf_blocked, mode='lines+markers',
                         name="Blocked (No Treatment)", line=dict(color="red", width=3)))
fig.add_trace(go.Scatter(x=days, y=csf_valve, mode='lines+markers',
                         name="Shunt Valve", line=dict(color="orange", width=3)))
fig.add_trace(go.Scatter(x=days, y=csf_neuroweave, mode='lines+markers',
                         name="NEUROWEAVE Nanobots", line=dict(color="blue", width=4)))

fig.update_layout(title="🧠 Intracranial Pressure / CSF Flow Over Time",
                  xaxis_title="Days",
                  yaxis_title="CSF Pressure (mmHg)",
                  height=600)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🔧 Key Components of NEUROWEAVE")
st.markdown("""
- **Self-guided nanobots** with magnetic propulsion and ependymal targeting.
- **BDNF + VEGF release** controlled by real-time AI.
- **Intravenous injection** with barrier-crossing polymer coating.
- **AR-assisted surgery** for real-time visualization and control.
- **Fail-safe self-destruction** in case of abnormal navigation or pH.
""")

st.subheader("📈 Projected Outcomes & Access")
col1, col2 = st.columns(2)
col1.metric("Infant Mortality Reduction", "↓ 84%", "Simulated")
col1.metric("Shunt Failure Reoperations", "↓ 91%", "vs. valves")
col2.metric("Tissue Regeneration", "↑ 78%", "in organoids")
col2.metric("Procedure Cost", "< $2,000", "per case (Global South)")

st.markdown("---")
st.caption("Created by Sonia Annette Echeverría Vera · Ecuador · 2025")
