"""Correlation matrices and heatmaps from real datasets: diamonds, flights, Titanic."""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Configure a default clean seaborn style
sns.set_theme(style="white")


def diamonds_correlation():
    diamonds = sns.load_dataset("diamonds")
    corr = diamonds.select_dtypes("number").corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(9.5, 7))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        annot_kws={"size": 11, "fontweight": "bold"},
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.8,
        linecolor="white",
        cbar_kws={"shrink": 0.8, "label": "Pearson correlation"},
        ax=ax,
    )
    ax.set_title("Diamonds: carat and dimensions drive the price")
    ax.tick_params(axis="x", rotation=30)
    sns.despine(fig)
    plt.savefig("corr_diamonds_heatmap.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def flights_month_year_heatmap():
    flights = sns.load_dataset("flights")
    pivot = flights.pivot(index="month", columns="year", values="passengers")

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.heatmap(
        pivot,
        cmap="rocket_r",
        annot=True,
        fmt="d",
        annot_kws={"size": 8},
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": "Passengers"},
        ax=ax,
    )
    ax.set_title("Air travel grew every year and every summer")
    ax.set_xlabel("Year")
    ax.set_ylabel("")
    ax.tick_params(axis="y", rotation=0)
    sns.despine(fig)
    plt.savefig("heatmap_flights_month_year.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def titanic_correlation():
    titanic = sns.load_dataset("titanic")
    cols = ["survived", "pclass", "age", "sibsp", "parch", "fare"]
    corr = titanic[cols].corr()

    fig, ax = plt.subplots(figsize=(8.5, 7))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        annot_kws={"size": 11, "fontweight": "bold"},
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.8,
        linecolor="white",
        cbar_kws={"shrink": 0.8, "label": "Pearson correlation"},
        ax=ax,
    )
    ax.set_title("Titanic: class and fare matter, family size does not")
    ax.tick_params(axis="x", rotation=30)
    ax.tick_params(axis="y", rotation=0)
    sns.despine(fig)
    plt.savefig("corr_titanic_heatmap.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def main():
    diamonds_correlation()
    flights_month_year_heatmap()
    titanic_correlation()


if __name__ == "__main__":
    main()