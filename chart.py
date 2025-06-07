import matplotlib.pyplot as plt
import numpy as np
import os
import uuid

def generate_chart(scores, categories):
    N = len(scores)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    scores += scores[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, scores, color='#f4e4cf', alpha=0.5)
    ax.plot(angles, scores, color='#df8f43', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9, fontweight='bold', color='#2b2b2b')
    ax.set_title("SYNC Life Balance Snapshot", size=14, weight='bold', y=1.08)

    ax.spines["polar"].set_visible(True)
    ax.grid(color='#cccccc', linestyle='--', linewidth=0.5)

    filename = f"{uuid.uuid4().hex}.png"
    path = os.path.join("/tmp", filename)
    plt.savefig(path, bbox_inches='tight', dpi=150)
    plt.close()
    return path
