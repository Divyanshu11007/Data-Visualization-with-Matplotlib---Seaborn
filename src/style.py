"""Shared plotting style: custom color palettes and consistent figure formatting."""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Fallback to current working directory if running in a notebook/interactive kernel
if "__file__" in globals():
    ROOT = Path(__file__).resolve().parents[1]
else:
    ROOT = Path.cwd()

CHARTS = ROOT / "charts"
CHARTS.mkdir(exist_ok=True)

PROJECT_PALETTE = ["#0B3B5C", "#2E86AB", "#F18F01", "#C73E1D", "#6B8F71", "#815AC0"]
SEX_COLORS = {"male": "#0B3B5C", "female": "#C73E1D"}
SMOKER_COLORS = {"Yes": "#C73E1D", "No": "#2E86AB"}
TIME_COLORS = {"Lunch": "#2E86AB", "Dinner": "#F18F01"}
ORIGIN_COLORS = {"japan": "#0B3B5C", "europe": "#F18F01", "usa": "#C73E1D"}
PENGUIN_COLORS = {"Adelie": "#0B3B5C", "Gentoo": "#F18F01", "Chinstrap": "#2E86AB"}
PALETTE_DICTS = {
    "sex": SEX_COLORS,
    "smoker": SMOKER_COLORS,
    "time": TIME_COLORS,
    "origin": ORIGIN_COLORS,
    "species": PENGUIN_COLORS,
}

SEQUENTIAL_CMAP = mpl.colors.LinearSegmentedColormap.from_list(
    "project_seq", ["#F5F1E8", "#F18F01", "#0B3B5C"]
)
DIVERGING_CMAP = mpl.colors.LinearSegmentedColormap.from_list(
    "project_div", ["#C73E1D", "#F5F1E8", "#0B3B5C"]
)


def set_style():
    sns.set_theme(context="talk", style="whitegrid", palette=PROJECT_PALETTE)
    mpl.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "axes.titlesize": 17,
            "axes.titleweight": "bold",
            "axes.titlepad": 14,
            "axes.labelsize": 13,
            "axes.edgecolor": "#BBBBBB",
            "grid.color": "#E6E2DA",
            "grid.linewidth": 0.8,
            "legend.frameon": False,
            "savefig.dpi": 150,
            "savefig.bbox": "tight",
        }
    )


def save(fig, name):
    path = CHARTS / name
    fig.savefig(path)
    plt.close(fig)
    return path