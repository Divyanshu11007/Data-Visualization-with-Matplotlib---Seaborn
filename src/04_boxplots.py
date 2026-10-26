"""Box plots from real datasets: Titanic ages, tipping by day, penguin species."""

import matplotlib.pyplot as plt
import seaborn as sns

# Configure a default clean seaborn style
sns.set_theme(style="white")


def titanic_age_by_class():
    titanic = sns.load_dataset("titanic")
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.boxplot(
        data=titanic,
        x="class",
        y="age",
        hue="sex",
        hue_order=["male", "female"],
        palette="deep",
        width=0.6,
        fliersize=3.5,
        linewidth=1.4,
        gap=0.15,
        ax=ax,
    )
    ax.set_title("Titanic: 3rd class was the youngest on board")
    ax.set_xlabel("Ticket class")
    ax.set_ylabel("Passenger age (years)")
    ax.legend(title="Sex", loc="upper right")
    sns.despine(fig)
    plt.savefig("box_titanic_age_class_sex.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def tips_bill_by_day_smoker():
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.boxplot(
        data=tips,
        x="day",
        y="total_bill",
        hue="smoker",
        hue_order=["No", "Yes"],
        order=["Thur", "Fri", "Sat", "Sun"],
        palette="muted",
        width=0.65,
        fliersize=3.5,
        linewidth=1.4,
        gap=0.15,
        ax=ax,
    )
    ax.set_title("Both bills and smokers pile up on weekends")
    ax.set_xlabel("Day of the week")
    ax.set_ylabel("Total bill ($)")
    ax.legend(title="Smoker", loc="upper left")
    sns.despine(fig)
    plt.savefig("box_tips_day_smoker.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def penguin_mass_by_species():
    penguins = sns.load_dataset("penguins").dropna()
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.boxplot(
        data=penguins,
        x="species",
        y="body_mass_g",
        hue="species",
        palette="colorblind",
        width=0.55,
        linewidth=1.4,
        legend=False,
        ax=ax,
    )
    sns.stripplot(
        data=penguins,
        x="species",
        y="body_mass_g",
        color="#333333",
        size=4,
        alpha=0.45,
        jitter=0.12,
        ax=ax,
    )
    ax.set_title("Penguin mass by species, with every individual shown")
    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    sns.despine(fig)
    plt.savefig("box_penguin_mass_species.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def main():
    titanic_age_by_class()
    tips_bill_by_day_smoker()
    penguin_mass_by_species()


if __name__ == "__main__":
    main()