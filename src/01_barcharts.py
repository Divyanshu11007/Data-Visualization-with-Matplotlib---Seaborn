"""Bar charts from real datasets: Titanic survival, mpg by origin, tips by day."""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Configure a default clean seaborn style
sns.set_theme(style="white")


def survival_by_class_sex():
    titanic = sns.load_dataset("titanic")
    rates = (
        titanic.groupby(["class", "sex"], observed=True)["survived"]
        .mean()
        .reset_index()
    )
    rates["survived"] *= 100

    fig, ax = plt.subplots(figsize=(9.5, 5.5))
    sns.barplot(
        data=rates,
        x="class",
        y="survived",
        hue="sex",
        hue_order=["male", "female"],
        palette={"male": "#1f77b4", "female": "#ff7f0e"},  # Standard color palette fallback
        edgecolor="white",
        ax=ax,
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="%.0f%%", padding=2, fontsize=11, fontweight="bold")
    ax.set_title("Titanic: women and 1st-class passengers had the best odds")
    ax.set_xlabel("Ticket class")
    ax.set_ylabel("Survival rate (%)")
    ax.set_ylim(0, 115)
    ax.legend(title="Sex")
    sns.despine(fig)
    plt.savefig("bar_titanic_survival_class_sex.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def avg_mpg_by_origin():
    mpg = sns.load_dataset("mpg").dropna(subset=["horsepower"])
    avg = mpg.groupby("origin")["mpg"].mean().sort_values().reset_index()
    
    # Built-in palette map based on origin
    origin_colors = {"usa": "#1f77b4", "japan": "#2ca02c", "europe": "#d62728"}
    colors = [origin_colors.get(o, "#7f7f7f") for o in avg["origin"]]

    fig, ax = plt.subplots(figsize=(8.5, 5))
    sns.barplot(
        data=avg,
        y="origin",
        x="mpg",
        hue="origin",
        palette=colors,
        edgecolor="white",
        legend=False,
        ax=ax,
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="%.1f mpg", padding=4, fontsize=11, fontweight="bold")
    ax.set_title("Average fuel economy by car origin (1970s models)")
    ax.set_xlabel("Miles per gallon (mpg)")
    ax.set_ylabel("")
    ax.set_xlim(0, avg["mpg"].max() * 1.18)
    sns.despine(fig)
    plt.savefig("bar_avg_mpg_by_origin.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def tips_revenue_by_day():
    tips = sns.load_dataset("tips")
    daily = (
        tips.groupby("day", observed=True)["total_bill"]
        .sum()
        .reindex(["Thur", "Fri", "Sat", "Sun"])
        .reset_index()
    )
    daily["total_bill"] = daily["total_bill"] / 1000

    fig, ax = plt.subplots(figsize=(8.5, 5))
    sns.barplot(
        data=daily,
        x="day",
        y="total_bill",
        hue="day",
        palette="deep",
        edgecolor="white",
        legend=False,
        ax=ax,
    )
    for container in ax.containers:
        ax.bar_label(container, fmt="$%.2fk", padding=2, fontsize=11, fontweight="bold")
    ax.set_title("Restaurant revenue peaks on the weekend")
    ax.set_xlabel("Day of the week")
    ax.set_ylabel("Total bill revenue ($k)")
    ax.set_ylim(0, daily["total_bill"].max() * 1.15)
    sns.despine(fig)
    plt.savefig("bar_tips_revenue_by_day.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def main():
    np.random.seed(42)
    survival_by_class_sex()
    avg_mpg_by_origin()
    tips_revenue_by_day()


if __name__ == "__main__":
    main()