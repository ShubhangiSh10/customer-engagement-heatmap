import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic realistic data
np.random.seed(42)
data = pd.DataFrame({
    "Purchase_Frequency": np.random.normal(50, 10, 100),
    "Avg_Order_Value": np.random.normal(300, 50, 100),
    "Days_Since_Last_Visit": np.random.normal(20, 5, 100),
    "Email_Click_Rate": np.random.normal(0.25, 0.05, 100),
    "App_Session_Per_Week": np.random.normal(5, 1.2, 100),
    "Support_Tickets": np.random.normal(2, 1.0, 100),
    "NPS_Score": np.random.normal(45, 10, 100),
})

# Compute correlation matrix
corr = data.corr()

# Style
sns.set_theme(style="whitegrid")
sns.set_context("talk")

# Create figure EXACTLY 512×512 px
plt.figure(figsize=(8, 8), dpi=64)

# Heatmap
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    square=True,
    linewidths=.5,
    cbar_kws={"shrink": .5}
)

plt.title("Customer Engagement Metrics – Correlation Matrix")

# Save exactly 512×512
plt.savefig("chart.png", dpi=64)
plt.close()
