# Information Visualization

> **Layer:** [14 Human and Visual Computing](../README.md) › [Human-computer interaction](README.md)
> **Builds on:** [Perception and cognition](perception-and-cognition.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Rasterization pipeline](../02-computer-graphics/rasterization-pipeline.md), [Unsupervised learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md)
> **Enables:** [Observability](../../12-software-engineering/04-operations/observability.md), [Usability evaluation](usability-evaluation.md), [Ethics and professional responsibility](../../15-computing-in-context/ethics-and-professional-responsibility.md)

## Essence

Information visualization turns data into pictures so that people can use their visual system, the highest-bandwidth channel into the brain, to see patterns, outliers and comparisons that would be invisible in a table. A chart is an **encoding**: each data attribute is mapped to a visual channel such as position, length, colour or shape, and the reader must decode it. Channels are not equal. Perception experiments show that people judge positions along a common scale far more accurately than angles, areas or colour shades, and that some features "pop out" without effort while others demand slow serial search. Good visualization is therefore an engineering discipline: match the most important attribute to the most accurate channel, remove marks that carry no data, choose colour scales that match the data's structure, and let interaction carry what one static view cannot.

## Core tenets

1. **Visualise because summaries hide structure.** Anscombe's quartet (1973) is four datasets with the same means, variances, correlation and regression line, yet one is linear, one curved, one has an outlier and one is a single extreme point. Summary statistics compress away exactly the structure a plot shows at a glance. Visualization is for exploring and checking data, not only for presenting conclusions.

2. **A chart maps data attributes to marks and channels.** Marks are geometric primitives (points, lines, areas); channels control their appearance (position, length, angle, area, colour hue, colour lightness, shape). Bertin (1967) first set out these visual variables; Mackinlay (1986) turned them into two design criteria. *Expressiveness*: the encoding shows all of the data and only the data, so an ordered attribute must not use an unordered channel such as hue. *Effectiveness*: the most important attributes get the most accurately perceived channels. The grammar of graphics (Wilkinson, 1999) behind tools such as ggplot2 and Vega-Lite makes this mapping the unit of specification.

3. **Channels have an effectiveness ranking.** Cleveland and McGill (1984) measured how accurately people compare quantities and found, from best to worst: position along a common scale; position along non-aligned scales; length, direction and angle; area; volume and curvature; shading and colour saturation. Heer and Bostock (2010) replicated the ranking with crowdsourced participants. This is why a bar chart beats a pie chart for comparing parts, and why bubble sizes are misjudged: perceived area grows more slowly than actual area. For categorical data the ranking changes: spatial grouping, hue and shape distinguish categories well.

4. **Preattentive features pop out; conjunctions do not.** A single red mark among blue ones, or one tilted line among upright ones, is found in a fixed time of roughly 200–250 ms regardless of how many distractors there are, because the visual system detects these features in parallel. A target defined by a *combination* (red *and* tilted among red upright and blue tilted marks) needs serial search, with time growing with the number of items (Treisman's feature integration theory). Use one preattentive channel to highlight what matters; mixing several highlights cancels the effect.

5. **Overview first, zoom and filter, then details on demand.** Shneiderman's "visual information-seeking mantra" (1996) describes how interactive visualization handles more data than one screen can show: start with an aggregated overview, let the user narrow to a region or subset, and reveal individual records only when asked. Linked views (selecting in one chart highlights the same items in another) and brushing extend this. Interaction is the answer to the gap between data volume and screen and attention limits.

6. **Maximise the share of ink that shows data.** Tufte's data-ink ratio (1983) asks what fraction of a graphic's ink encodes data; heavy gridlines, 3D effects, shadows and decoration ("chartjunk") add ink without information and can distort. Small multiples, a grid of the same chart for different subsets on shared axes, exploit the eye's skill at comparing aligned positions. Tufte's lie factor, the ratio of the size of an effect shown to the size in the data, should be near 1: a bar chart whose axis does not start at zero exaggerates differences because bars encode length.

7. **Colour scales must match the data type.** Use *sequential* scales (light to dark in one hue) for ordered magnitudes, *diverging* scales (two hues meeting at a neutral midpoint) for values around a meaningful centre, and *categorical* hues for unordered classes, of which people reliably tell apart only around eight to ten. Lightness carries order; hue does not. The rainbow colour map is a common mistake: its lightness rises and falls, creating false boundaries and hiding real ones. Perceptually uniform maps such as viridis (2015) change lightness monotonically and stay readable for the roughly 8% of men with red-green colour vision deficiency.

8. **Scale changes the problem.** Plotting a million points as dots produces overplotting: a solid blob in which density is invisible. Large data is aggregated (histograms, hexagonal binning, density shading) before it is drawn, and high-dimensional data is projected to two dimensions with methods such as Principal Component Analysis (PCA) or t-distributed Stochastic Neighbor Embedding (t-SNE), whose distortions must be remembered when reading the result.

## Key concepts

| Term | Meaning |
|---|---|
| Mark | Geometric primitive that represents an item or link (point, line, area) |
| Visual channel | Property of a mark that encodes an attribute (position, length, hue, ...) |
| Expressiveness | An encoding shows all of the data's structure and nothing extra |
| Effectiveness | Important attributes use the most accurately perceived channels |
| Preattentive feature | Visual property detected in parallel, in constant time |
| Data-ink ratio | Fraction of a graphic's ink that encodes data |
| Small multiples | Repeated charts on shared scales, one per subset |
| Sequential / diverging / categorical scale | Colour maps for ordered, centred and unordered data |
| Overplotting | Marks hiding one another so density and structure are lost |

## How it fits

- **Below:** Channel rankings and pop-out are applications of [perception and cognition](perception-and-cognition.md); honest summaries, uncertainty bands and error bars come from [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md); charts are drawn by the [rasterization pipeline](../02-computer-graphics/rasterization-pipeline.md); dimensionality reduction comes from [unsupervised learning](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md).
- **Above:** Operational dashboards in [observability](../../12-software-engineering/04-operations/observability.md), scientific figures, and machine-learning training curves are visualizations and inherit these rules. Misleading charts are an issue of [professional ethics](../../15-computing-in-context/ethics-and-professional-responsibility.md).
- **Siblings:** [Perception and cognition](perception-and-cognition.md) supplies the human limits; [interaction design principles](interaction-design-principles.md) govern the zoom, filter and brushing controls; [usability evaluation](usability-evaluation.md) tests whether readers actually extract the intended insight.

## Common misconceptions

- **"Pie charts are fine for comparing parts."** Angle and area are judged worse than position or length; a sorted bar chart is almost always easier to read.
- **"More colours make a chart clearer."** Hue cannot convey order, and beyond about eight to ten categories readers cannot match colours to a legend.
- **"Removing decoration is just style."** Extra ink competes for preattentive attention and can encode false differences; it changes what readers perceive.

## Go deeper

- Tamara Munzner, *Visualization Analysis and Design* (2014): marks, channels, expressiveness and effectiveness as a design framework.
- Edward Tufte, *The Visual Display of Quantitative Information* (1983): data-ink, chartjunk, small multiples and the lie factor.
- William Cleveland and Robert McGill, "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods" (1984): the channel-accuracy experiments.
- Ben Shneiderman, "The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations" (1996): the information-seeking mantra.
