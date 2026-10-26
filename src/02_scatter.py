"""Scatter plots from real datasets: penguins, cars, and restaurant tips."""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Configure a default clean seaborn style
sns.set_theme(style="white")


def annotate_pearson(ax, x, y, label="Pearson r"):
    r = np.corrcoef(x, y)[0, 1]
    ax.annotate(
        f"{label} = {r:.2f}",
        xy=(0.03, 0.92),
        xycoords="axes fraction",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#BBBBBB"),
    )


def penguins_flipper_mass():
    penguins = sns.load_dataset("penguins").dropna()
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.scatterplot(
        data=penguins,
        x="flipper_length_mm",
        y="body_mass_g",
        hue="species",
        palette="deep",
        s=70,
        alpha=0.75,
        edgecolor="white",
        linewidth=0.6,
        ax=ax,
    )
    sns.regplot(
        data=penguins,
        x="flipper_length_mm",
        y="body_mass_g",
        scatter=False,
        color="#C73E1D",
        line_kws={"ls": "--", "lw": 2},
        ax=ax,
    )
    annotate_pearson(ax, penguins["flipper_length_mm"], penguins["body_mass_g"])
    ax.set_title("Penguins: bigger flippers mean heavier bodies")
    ax.set_xlabel("Flipper length (mm)")
    ax.set_ylabel("Body mass (g)")
    ax.legend(title="Species", loc="lower right")
    sns.despine(fig)
    plt.savefig("scatter_penguins_flipper_mass.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def mpg_weight_fuel():
    mpg = sns.load_dataset("mpg").dropna(subset=["horsepower"])
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.scatterplot(
        data=mpg,
        x="weight",
        y="mpg",
        hue="origin",
        size="cylinders",
        sizes=(30, 180),
        palette="muted",
        alpha=0.75,
        edgecolor="white",
        linewidth=0.6,
        ax=ax,
    )
    annotate_pearson(ax, mpg["weight"], mpg["mpg"], label="r")
    ax.set_title("Heavier cars burn more fuel: weight vs mpg by origin")
    ax.set_xlabel("Vehicle weight (lb)")
    ax.set_ylabel("Miles per gallon (mpg)")
    ax.legend(title="Origin / cylinders", loc="upper right", fontsize=10)
    sns.despine(fig)
    plt.savefig("scatter_mpg_weight_fuel.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def tips_bill_tip():
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip",
        hue="time",
        style="smoker",
        palette="colorblind",
        s=65,
        alpha=0.8,
        edgecolor="white",
        linewidth=0.6,
        ax=ax,
    )
    annotate_pearson(ax, tips["total_bill"], tips["tip"])
    ax.set_title("Tipping scales with the bill, dinner or lunch")
    ax.set_xlabel("Total bill ($)")
    ax.set_ylabel("Tip ($)")
    ax.legend(title="Meal time / smoker", loc="upper left", fontsize=10)
    sns.despine(fig)
    plt.savefig("scatter_tips_bill_tip.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def main():
    penguins_flipper_mass()
    mpg_weight_fuel()
    tips_bill_tip()


if __name__ == "__main__":
    main()