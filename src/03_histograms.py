"""Histograms with KDE overlays from real datasets: penguins, cars, tips."""

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns

# Configure a default clean seaborn style
sns.set_theme(style="white")


def penguin_body_mass():
    penguins = sns.load_dataset("penguins").dropna()
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.histplot(
        data=penguins,
        x="body_mass_g",
        hue="species",
        multiple="stack",
        bins=28,
        palette="deep",
        edgecolor="white",
        alpha=0.9,
        ax=ax,
    )
    ax.axvline(penguins["body_mass_g"].mean(), color="#555555", ls="--", lw=1.4)
    ax.annotate(
        f'Overall mean: {penguins["body_mass_g"].mean():,.0f} g',
        xy=(0.03, 0.88),
        xycoords="axes fraction",
        fontsize=12,
        fontweight="bold",
        ha="left",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#BBBBBB"),
    )
    ax.set_title("Penguin body mass: Gentoo is the heavyweight")
    ax.set_xlabel("Body mass (g)")
    ax.set_ylabel("Number of penguins")
    
    # Generate custom handles dynamically matching the default 'deep' palette
    unique_species = penguins["species"].unique()
    colors = sns.color_palette("deep", len(unique_species))
    handles = [mpatches.Patch(facecolor=colors[i], label=species) for i, species in enumerate(unique_species)]
    ax.legend(handles=handles, title="Species")
    
    sns.despine(fig)
    plt.savefig("hist_penguin_body_mass.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def mpg_distribution():
    mpg = sns.load_dataset("mpg").dropna(subset=["horsepower"])
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.histplot(
        data=mpg,
        x="mpg",
        hue="origin",
        element="step",
        fill=False,
        stat="density",
        common_norm=False,
        bins=30,
        palette="muted",
        linewidth=2.2,
        ax=ax,
    )
    ax.axvline(mpg["mpg"].mean(), color="#C73E1D", ls="--", lw=2)
    ax.annotate(
        f'Fleet mean: {mpg["mpg"].mean():.1f} mpg',
        xy=(0.80, 0.88),
        xycoords="axes fraction",
        fontsize=12,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#BBBBBB"),
    )
    ax.set_title("Fuel economy is right-skewed: most cars cluster near 20 mpg")
    ax.set_xlabel("Miles per gallon (mpg)")
    ax.set_ylabel("Density")
    sns.despine(fig)
    plt.savefig("hist_mpg_distribution.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def tips_total_bill_kde():
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(9.5, 6))
    sns.histplot(
        data=tips,
        x="total_bill",
        bins=25,
        stat="density",
        color="#2E86AB",
        alpha=0.55,
        edgecolor="white",
        ax=ax,
    )
    sns.kdeplot(data=tips, x="total_bill", color="#C73E1D", lw=2.5, ax=ax)
    for pos, name in zip(
        tips["total_bill"].quantile([0.25, 0.5, 0.75]), ["Q1", "Median", "Q3"]
    ):
        ax.axvline(pos, color="#555555", ls="--", lw=1.2)
        ax.text(
            pos,
            ax.get_ylim()[1] * 0.95,
            name,
            ha="center",
            fontsize=11,
            fontweight="bold",
            color="#444444",
        )
    ax.set_title("Most restaurant bills land between $13 and $25")
    ax.set_xlabel("Total bill ($)")
    ax.set_ylabel("Density")
    sns.despine(fig)
    plt.savefig("hist_tips_total_bill_kde.png", bbox_inches="tight", dpi=120)
    plt.close(fig)


def main():
    penguin_body_mass()
    mpg_distribution()
    tips_total_bill_kde()


if __name__ == "__main__":
    main()