import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

# Read data from CSV
df = pd.read_csv("data.csv")

# Use the latest submission (last row)
latest = df.iloc[-1]

# Extract categories and values
categories = []
values = []

for column in df.columns:
    match = re.match(r'\d+\.\s*(.*?)\s*How', column)
    if match:
        category = match.group(1).strip()
        categories.append(category)
        values.append(latest[column])

# Complete the loop for radar chart
values += values[:1]
categories += categories[:1]

# Number of variables
N = len(categories)

# Calculate angle for each axis
angles = [n / float(N) * 2 * np.pi for n in range(N)]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Draw the outline
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.set_rlabel_position(0)
ax.set_ylim(0, 10)
ax.set_yticks(range(1, 11))
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10)

# Plot the values
ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, alpha=0.3)

# Save chart
plt.savefig("life_balance_chart.png")
