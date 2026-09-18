import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Skills
# -----------------------------

labels = [
    "Python",
    "AI / Machine\nLearning",
    "Cloud /\nBig Data",
    "Data\nEngineering",
    "Power BI",
    "SQL"
]

values = [5, 4, 4, 5, 5, 5]

# Cerrar el polígono
values += values[:1]

N = len(labels)

angles = np.linspace(
    0,
    2 * np.pi,
    N,
    endpoint=False
).tolist()

angles += angles[:1]

# -----------------------------
# Figure
# -----------------------------

fig = plt.figure(figsize=(8, 8), facecolor="#111827")

ax = plt.subplot(
    111,
    polar=True,
    facecolor="#17152e"
)

# Primer eje arriba
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# -----------------------------
# Grid
# -----------------------------

ax.set_ylim(0, 5)

ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels([])

ax.grid(
    color="#6b5b95",
    alpha=0.35,
    linewidth=0.8
)

ax.spines["polar"].set_visible(False)

# -----------------------------
# Labels
# -----------------------------

ax.set_xticks(angles[:-1])

ax.set_xticklabels(
    labels,
    color="white",
    fontsize=11,
    fontweight="bold"
)

ax.tick_params(
    axis="x",
    pad=18
)

# -----------------------------
# Radar polygon
# -----------------------------

ax.plot(
    angles,
    values,
    linewidth=2.5,
    color="#c84cff"
)

ax.fill(
    angles,
    values,
    color="#7047eb",
    alpha=0.35
)

ax.scatter(
    angles[:-1],
    values[:-1],
    s=70,
    color="#ff4db8",
    edgecolors="#111827",
    linewidth=1.2,
    zorder=10
)

# -----------------------------
# Titles
# -----------------------------

fig.text(
    0.5,
    0.94,
    "Core Skills",
    ha="center",
    color="white",
    fontsize=20,
    fontweight="bold"
)

fig.text(
    0.5,
    0.905,
    "SELF-ASSESSED · 1 = LEARNING · 5 = ADVANCED",
    ha="center",
    color="#beb8d5",
    fontsize=9
)

fig.text(
    0.5,
    0.055,
    "github.com/gabo2912",
    ha="center",
    color="#88829f",
    fontsize=8
)

plt.subplots_adjust(
    top=0.82,
    bottom=0.15,
    left=0.15,
    right=0.85
)

plt.savefig(
    "assets/core-skills.png",
    dpi=300,
    bbox_inches="tight",
    facecolor=fig.get_facecolor()
)

plt.show()