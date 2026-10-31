# Review notes

Collected from writer reports, to be resolved in the review pass.

## Taxonomy suggestions

- **01 (W2):** in `02-infinity-and-cardinality`, ordinals would read more naturally before cardinal numbers (cardinals currently define size by bijection classes and point forward to the "least ordinal" definition).

- **07 (W8):** candidate leaves: higher homotopy groups and fibrations; cohomology, cup products and Poincaré duality; CW complexes; vector bundles and characteristic classes; Morse theory; four-manifolds; topological data analysis (in 14). Knot theory could later split into classical and quantum invariants.
- **11 (W12):** candidate leaves: Poisson processes and continuous-time Markov chains; large deviations; stable laws and heavy tails; nonparametric statistics and the bootstrap; time series; causal inference (exists only in the medicine tree).

## Claims to verify

### Layer 01 (W2)

- **Countable sets:** Galileo 1638; Dedekind 1888 (definition of infinite); Cantor 1874 (algebraic numbers countable); back-and-forth method uncredited; Feferman–Levy model undated.
- **Diagonal argument:** Cantor 1891 versus 1874; Lawvere 1969; Turing 1936; Gödel 1931; hierarchy theorems as diagonal arguments; Cantor's letters to Dedekind 1899; Yanofsky 2003 (no venue).
- **Cardinal numbers:** Hartogs 1915; Tarski κ·κ = κ equivalent to AC; Cantor to Dedekind 1877 quote; König's theorem gives 2^ℵ₀ ≠ ℵ_ω; perfect set property for Borel sets; Lévy–Solovay 1967; PFA implies 2^ℵ₀ = ℵ₂; Gödel 1938/1940; Cohen 1963.
- **Ordinals:** Burali-Forti 1897; von Neumann 1923; Goodstein sequence from 3; Goodstein 1944; Kirby–Paris 1982; Gentzen 1936; Borel hierarchy closes at ω₁ without choice.
- **Paradoxes:** Russell 1901, letter to Frege June 1902; Berry phrase word count; Ramsey's split; NBG conservative over ZFC; Grothendieck universe ⇔ inaccessible; Boolos 1971 iterative conception.
- **ZF:** Zermelo 1908; Fraenkel and Skolem 1922; von Neumann foundation 1920s; |V₅| = 65,536; V_(ω+ω) models all but replacement; Martin 1975; Friedman 1971; Shelah 1974; Skolem's paradox 1922.
- **Axiom of choice:** Zermelo 1904; Zorn 1935; Hausdorff 1914; Kuratowski 1922; Blass 1984; Kelley 1950; Hodges 1979; Vitali 1905; Banach–Tarski 1924, five pieces minimal (Robinson 1947); Banach 1923 solvable groups; ZFC conservative over ZF for arithmetic; Diaconescu 1975; Blair 1977; Solovay 1970; sequential continuity needs countable choice.
- **Type theory:** Russell 1908; *Principia* 1910–1913; Church 1940; Lean `Classical.em` from choice; Girard's paradox undated; ETCS 1964; Automath 1967; Mizar Tarski–Grothendieck; Gonthier 2005; Feit–Thompson 2012; Coq renamed Rocq.
- **Quotients:** Novikov and Boone 1950s.
- **Books:** Artin *Algebra* 2nd edition 2011 or 2010; check all other edition years.

### Layer 02 (W3)

- **Constructing the numbers:** Peano and Dedekind starting at 1; Benacerraf 1965; Paris–Harrington 1977; Dedekind's 1872 √2·√3 = √6 claim; Cantor 1872 with Heine and Méray; Cantor 1874, 1891; Bombelli 1572; Gauss 1799 thesis and four proofs; Lindemann–Weierstrass general form 1885 and its statement; Roth 1955; Baker 1966; Apéry 1978; Nesterenko 1996; Frobenius 1877; Hurwitz 1898; Graves and Cayley octonions; Degen's eight-square identity; Kervaire and Bott–Milnor 1958; Ostrowski 1916; Hensel 1897; Cayley–Dickson sign convention.
- **Elementary number theory:** Lamé 1844 and 1847; Bachet and Bézout; Gauss 1801 unique factorisation; Fermat 1640; Euler 1763; Zhang 2013 (70,000,000); Polymath 246 (2014); Helfgott 2013; Alford–Granville–Pomerance 1994; AKS 2002/2004; Artin's conjecture 1927, Hooley 1967 under GRH; Legendre 1798; "more than two hundred proofs" of reciprocity; Artin reciprocity 1927 and Hilbert's ninth problem; Brahmagupta, Bhāskara II, Fermat c. 1637, Lagrange 1770; Selmer 1951; Jones–Sato–Wada–Wiens 1976; Davis–Putnam–Robinson 1961.
- **Books:** Knuth vol. 2 3rd edition 1997; Tao *Analysis I* 2006; Fine and Rosenberger 1997; Matiyasevich 1993; Davis 1973; Koblitz 2nd edition 1994; Cox 2nd edition 2013; Lemmermeyer 2000; Shoup 2nd edition 2009; Crandall and Pomerance 2nd edition 2005.

### Layer 07 (W8)

- **Point-set:** Kelley 1950 title; Tychonoff for Hausdorff factors ⇔ ultrafilter lemma; Urysohn c. 1925, posthumous; Steen–Seebach 1970; Munkres 2nd edition 2000; Kelley 1955; Armstrong 1983 (or 1979).
- **Algebraic topology:** π₃(S²) ≅ ℤ (Hopf); every finitely presented group is π₁ of a closed 4-manifold, homeomorphism problem undecidable (Markov 1958); Hawaiian earring has no universal cover; Nielsen–Schreier n(k−1)+1; branched covers and function fields; Massey 1967; Stillwell 2nd edition 1993; Fulton 1995; Munkres 1984.
- **Euler characteristic:** closed odd-dimensional manifolds have χ = 0; Lakatos 1976; Richeson 2008.
- **Fixed points:** PPAD-completeness phrasing; Lovász–Kneser via Borsuk–Ulam; Kakutani hypotheses; Matoušek 2003; Milnor 1965.
- **Manifolds:** Milnor 1956; Kervaire–Milnor 28; exotic ℝ⁴ (Freedman, Donaldson; Taubes uncountably many); unique smooth structures in dimension ≤ 3; smooth 4-dimensional Poincaré open; Whitney into ℝ²ⁿ; Lee 2nd edition 2013; Guillemin–Pollack 1974.
- **Surfaces:** Radó; T # ℝP² ≅ N₃; H₁(N_k) ≅ ℤᵏ⁻¹ ⊕ ℤ/2; uniformisation for non-orientable surfaces; Weeks 1985.
- **Knots:** Alexander 1928; Jones 1984; Alexander polynomials of trefoil and figure-eight; Conway knot Δ = 1; skein sign convention; Jones unknot problem open; Kronheimer–Mrowka 2011; Adams 1994; Rolfsen 1976; Lickorish 1997.
- **Three-manifolds:** Poincaré 1904; Smale 1961; Freedman 1982; Kneser–Milnor; JSJ; Thurston c. 1982; Hamilton 1982; Perelman 2002–2003; expositions c. 2006; Fields 2006, Millennium 2010; "only Millennium problem solved as of 2026"; Thurston 1997; Morgan–Tian 2007; O'Shea 2007.

### Layer 11 (W12)

- **Foundations and limit theorems:** Vitali 1905; Solovay 1970; Hilbert's sixth problem; Kolmogorov 1933 (English 1950) and Borel's paradox; Kesten 1980; percolation at criticality on ℤ³ open; Hewitt–Savage 1955; Etemadi 1981; Khinchin 1929; Bernoulli 1713; Birkhoff 1931; Markov 1906 and motive; Glivenko–Cantelli 1933; de Moivre 1733; Laplace 1812; Pólya 1920 naming; Lindeberg 1922; Feller 1935; Berry 1941; Esseen 1942; constant < 0.5; Donsker 1951; Lindeberg counterexample bound 1/(√2 − 1); Chernoff 1952; Hoeffding 1963; Azuma 1967; McDiarmid 1989; chromatic number concentration; Erdős–Kac 1940; Cramér 1936; Martin-Löf 1966; Pascal–Fermat 1654.
- **Processes and statistics:** Doeblin 1938; Bayer–Diaconis 1992; Pólya 1921; Metropolis 1953; Brown 1827; Bachelier 1900; Einstein 1905; Wiener 1923; Paley–Wiener–Zygmund 1933; Kakutani 1944; Itô 1944, 1951; Kac 1949; Black–Scholes–Merton 1973; Girsanov 1960; Fisher 1922; Stein 1956; James–Stein 1961; Rao 1945; Cramér 1946; Neyman–Scott 1948; uniform-maximum variance θ²/(n(n + 2)); Neyman–Pearson 1933; Wilks 1938; Student 1908; Benjamini–Hochberg 1995; ASA statement 2016; Bayes 1763; Laplace 1774; de Finetti 1931; Doob 1949; Diaconis–Freedman 1986; Geman and Geman 1984; Gelfand–Smith 1990; Gauss 1821–1823; Aitken 1935; Galton 1886; Hoerl–Kennard 1970; Tibshirani 1996.
- **Worked numbers:** 1000 coin tosses P(S ≥ 600) bounds; the 36% false-discovery example; Chebyshev versus Hoeffding sample sizes; 0.99³⁰ ≈ 0.74.
- **Books:** check all edition years listed in the Go deeper sections.

## Cross-layer follow-ups (coordinator, after review pass)
