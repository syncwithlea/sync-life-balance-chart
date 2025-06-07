import matplotlib.pyplot as plt
import numpy as np
import os

def create_radar_chart(categories, values, name="Life Balance", date=""):
    # Number of variables we're plotting.
    num_vars = len(categories)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    # Ensure the values loop back to the start
    values += values[:1]

    # Set up the radar chart
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Draw one axe per variable + add labels
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Set up axis labels and ticks
    ax.set_rlabel_position(0)
    ax.set_yticks(np.arange(1, 11, 1))
    ax.set_yticklabels([str(i) for i in range(1, 11)], color="grey", size=8)
    ax.set_ylim(0, 10)
    
    # Draw axis labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=10, fontweight='bold')

    # Plot data
    ax.plot(angles, values, color="mediumslateblue", linewidth=2, linestyle='solid')
    ax.fill(angles, values, color="mediumslateblue", alpha=0.25)

    # Add title
    title = f"{name}'s Life Balance\n{date}" if date else f"{name}'s Life Balance"
    plt.title(title, size=16, y=1.1, fontweight='bold')

    # Add a custom legend
    legend_text = ("Score Guide:\n"
                   "0–3: Needs Immediate Attention\n"
                   "4–6: Room for Improvement\n"
                   "7–10: Going Well")
    plt.annotate(
        legend_text,
        xy=(1.1, -0.2),
        xycoords='axes fraction',
        ha='left',
        va='center',
        fontsize=9,
        bbox=dict(boxstyle='round,pad=0.4', edgecolor='lightgray', facecolor='white', alpha=0.8)
    )

    # Save chart
    output_path = os.path.join(os.getcwd(), "life_balance_chart.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    return output_path
