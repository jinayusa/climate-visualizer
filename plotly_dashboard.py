import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load merged dataset
df = pd.read_csv('data/merged_global_climate.csv')

# Line chart – Temperature Anomaly
fig1 = px.line(df, x='Year', y='TempAnomaly',
               title='🌡️ Global Temperature Anomalies (1960–2020)',
               labels={'TempAnomaly': 'Temperature Deviation (°C)'},
               template='plotly_white')

# Line chart – Avg CO2 emissions
fig2 = px.line(df, x='Year', y='CO2',
               title='🛢️ Global Average CO₂ Emissions Per Capita',
               labels={'CO2': 'CO₂ (metric tons)'},
               template='plotly_white')

# Correlation – Dual axis plot
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=df['Year'], y=df['TempAnomaly'], name='Temperature Anomaly (°C)', yaxis='y1'))
fig3.add_trace(go.Scatter(x=df['Year'], y=df['CO2'], name='Avg CO₂ Emissions', yaxis='y2'))

fig3.update_layout(
    title="📈 Correlation Between CO₂ and Global Temperature",
    xaxis=dict(title="Year"),
    yaxis=dict(title="Temp Anomaly (°C)", side='left'),
    yaxis2=dict(title="CO₂ Emissions", overlaying='y', side='right'),
    template='plotly_white'
)

# Show plots
fig1.show()
fig2.show()
fig3.show()
