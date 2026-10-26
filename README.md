# Data Visualization with Matplotlib & Seaborn

A hands-on data-visualization portfolio built with **Matplotlib** and **Seaborn**. Every chart
is generated from a **real dataset** bundled with Seaborn (`titanic`, `mpg`, `tips`,
`penguins`, `diamonds`, `flights`) and saved as a high-resolution PNG in `charts/`.

The goal: learn to tell compelling stories through visual data graphics — not just make plots.

## Chart gallery

| Script | Charts | Dataset | Story it tells |
|---|---|---|---|
| `01_barcharts.py` | Grouped bar, ranked bar, revenue bar | titanic, mpg, tips | Titanic survival by class & sex; Japanese cars led 70s fuel economy; weekend revenue peak |
| `02_scatter.py` | Scatter + regression, bubble scatter | penguins, mpg, tips | Flipper length predicts body mass; heavier cars burn more fuel; tips scale with bill |
| `03_histograms.py` | Stacked histogram, KDE overlay, step KDE | penguins, mpg, tips | Gentoo penguins are heaviest; mpg is right-skewed; most bills sit between $13–$25 |
| `04_boxplots.py` | Grouped box plots + strip overlay | titanic, tips, penguins | 3rd class was youngest; smokers & bigger bills on weekends; mass by species |
| `05_correlation_heatmaps.py` | Masked correlation heatmap, annotated pivot heatmap, full correlation matrix | diamonds, flights, titanic | Carat drives diamond price; air travel grows yearly & seasonally; class/fare matter for survival |

## Highlights

- **Custom color palettes** — a hand-tuned palette (`style.PROJECT_PALETTE`) used across
  every chart, plus dataset-specific semantic colors (sex, smoker, time, origin, species).
- **Custom colormaps** — `SEQUENTIAL_CMAP` and `DIVERGING_CMAP` built with
  `LinearSegmentedColormap` for the heatmaps.
- **Consistent formatting** — one shared `set_style()` (whitegrid theme, talk-size fonts,
  bold titles, tight bounding boxes, 150 dpi), labeled axes everywhere, Pearson-r
  annotations on scatter plots, bar-label callouts, and despined axes.

## Results (15 charts)

`charts/bar_titanic_survival_class_sex.png` · `charts/bar_avg_mpg_by_origin.png` ·
`charts/bar_tips_revenue_by_day.png` · `charts/scatter_penguins_flipper_mass.png` ·
`charts/scatter_mpg_weight_fuel.png` · `charts/scatter_tips_bill_tip.png` ·
`charts/hist_penguin_body_mass.png` · `charts/hist_mpg_distribution.png` ·
`charts/hist_tips_total_bill_kde.png` · `charts/box_titanic_age_class_sex.png` ·
`charts/box_tips_day_smoker.png` · `charts/box_penguin_mass_species.png` ·
`charts/corr_diamonds_heatmap.png` · `charts/heatmap_flights_month_year.png` ·
`charts/corr_titanic_heatmap.png`

## Requirements

- Python 3.10+
- Installing dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run any script from the repository root — each writes its PNGs into `charts/`:

```bash
python src/01_barcharts.py
python src/02_scatter.py
python src/03_histograms.py
python src/04_boxplots.py
python src/05_correlation_heatmaps.py
```

## Project structure

```
DV/
├── README.md
├── requirements.txt
├── src/
│   ├── style.py                    # custom palette + formatting helpers
│   ├── 01_barcharts.py
│   ├── 02_scatter.py
│   ├── 03_histograms.py
│   ├── 04_boxplots.py
│   └── 05_correlation_heatmaps.py
└── charts/                         # generated PNG charts (150 dpi)
```

## Key takeaways

1. **Annotation turns a chart into a story** — bar labels, mean lines, and Pearson-r
   boxes let the reader get the point in one glance.
2. **Correlation ≠ causation, but heatmaps point you where to look** — carat vs price
   (r ≈ 0.92 in diamonds) immediately flags the strongest relationship.
3. **Conditional views beat averages** — splitting bars/boxes by a second variable
   (e.g., survival by class *and* sex) reveals stories averages hide.
4. **Consistent styling builds trust** — one palette and one formatting pass across all
   charts make a report feel like one narrative instead of a grab bag.
