# Review notes

Collected from writer reports, to be resolved in the review pass.

## Taxonomy suggestions

- **01 (W2):** in `02-infinity-and-cardinality`, ordinals would read more naturally before cardinal numbers (cardinals currently define size by bijection classes and point forward to the "least ordinal" definition).

- **07 (W8):** candidate leaves: higher homotopy groups and fibrations; cohomology, cup products and Poincaré duality; CW complexes; vector bundles and characteristic classes; Morse theory; four-manifolds; topological data analysis (in 14). Knot theory could later split into classical and quantum invariants.
- **11 (W12):** candidate leaves: Poisson processes and continuous-time Markov chains; large deviations; stable laws and heavy tails; nonparametric statistics and the bootstrap; time series; causal inference (exists only in the medicine tree).

- **05 (W6):** optional leaves: commutative and Noetherian rings (localisation, prime spectrum) as a bridge to 12; group extensions and cohomology.

- **14 (W15):** candidate leaves: FFT and spectral methods; combinatorial and integer optimisation; quadrature; computational complexity (P versus NP) in 13 or 14; quantum computation has no home in the math tree (CS leaf linked instead).

- **08 (W9):** candidate leaves: symplectic geometry; fibre bundles, connections and characteristic classes (gauge theory); geometric group theory.

- **13 (W14):** candidate leaves: Turing degrees and relative computability; topos theory; stability, classification theory and o-minimality (a fifth model-theory leaf).
- **04 (W5):** candidate leaves: principal component analysis (in 11 or 14); symmetric and Clifford algebras; classical matrix groups.

- **03 (W4):** candidate leaves: random graphs (G(n, p), thresholds, giant component); designs, Latin squares and finite geometries; algebraic and spectral graph theory with expanders; matroids; combinatorial optimisation; algebraic combinatorics (symmetric functions, Young tableaux).

- **09 (W10):** candidate leaves: compact operators and Fredholm theory (09/03); wavelets and time-frequency analysis (09/04); elliptic functions (09/02); Hardy spaces, singular integrals, operator algebras; the general spectral theorem (now split between 09 and 14). Cross-link ergodic theorems (10) from 09/01.

- **06 (W7):** number `04-metric-spaces` before `03-calculus-of-several-variables`, since 03 builds on 04; move `estimates-and-inequalities` earlier in area 01; add a leaf on power series and analytic functions.

- **10 (W11):** layer 07 has no Jordan curve theorem leaf (Poincaré–Bendixson would link to it); complex dynamics (Julia and Mandelbrot sets, Douady–Hubbard) has no home, candidate leaf in 10/04 or 09.

- **14–15 (W16):** 14/05 decision theory (expected utility, Markov decision processes) and mechanism design/auctions; 14/06 optimal transport and kernel methods; 14/04 inverse problems and tomography; statistical mechanics and quantum information have no home; 15 might add "mathematics and the sciences".

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

### Layer 05 (W6)

- **Groups:** Burnside's lemma known to Frobenius; McKay 1959 (Cauchy); Wielandt's Sylow proof; Jordan 1870, Hölder 1889; Burnside pᵃqᵇ 1904.
- **Finite simple groups:** Feit–Thompson 1963, 255 pages, Coq 2012; 16 Lie-type families, 26 sporadics, Tits group; Monster order ≈ 8 × 10⁵³, Griess 1982; Aschbacher–Smith 2004; Gorenstein–Lyons–Solomon since 1994; "nearly 50 billion" groups of order 1024; Conway–Norton 1979, Borcherds 1992.
- **Presentations:** Novikov 1955, Boone; Dehn 1911; Higman 1961; Adian–Rabin; Markov on 4-manifolds.
- **Rings and fields:** Lamé 1847; Kummer and 23; ℤ[(1+√−19)/2] PID not Euclidean; Hilbert basis 1890; Steinitz 1910; Wedderburn 1905; AES polynomial x⁸ + x⁴ + x³ + x + 1.
- **Galois theory:** Shafarevich (solvable groups over ℚ); inverse Galois problem and sixth Fermat prime open; Cardano 1545; Ruffini 1799; Abel 1824; Hermite 1858, 1873; Wantzel 1837; Lindemann 1882; Gauss 1796/1801; 641 × 6700417; Frobenius 1896.
- **Books:** Cox–Little–O'Shea 4th 2015; Lidl–Niederreiter 1994; Serre 1977; James–Liebeck 2nd 2001; Artin 2nd 2011; Cox 2nd 2012; Stewart 4th 2015; Ireland–Rosen 2nd 1990; Stewart–Tall 3rd 2002; Lyndon–Schupp 1977; Stillwell 2nd 1993.

### Layer 14, parts 01–03 (W15)

- **Numerical analysis:** Wilkinson c. 1960; Householder 1958; Hestenes–Stiefel 1952; Francis/Kublanovskaya c. 1961; Runge 1895, 1901; Kutta 1901; Dormand–Prince 1980; Dahlquist 1963; Crank–Nicolson 1947; Lax–Richtmyer 1956; Courant 1943; Faber 1914; Bernstein 1912; Schoenberg 1946; Cayley 1879; Shamir 1979; Metropolis 1953; Hastings 1970; Dyer–Frieze–Kannan 1991; Bárány–Füredi; Hubbard–Schleicher–Sutherland 2001; Dongarra–Sullivan 2000; Lebesgue-constant asymptotics; growth factors "only partly understood".
- **Optimisation:** Bland 1977; Klee–Minty 1972; Santos 2010/2012 (43 dimensions, 86 facets); Spielman–Teng 2001; Khachiyan 1979; Karmarkar 1984; Farkas 1902; Kantorovich 1939; Slater 1950; Karush 1939; Kuhn–Tucker 1951; Goemans–Williamson 1995 (0.878); Nesterov–Nemirovski 1994; Nesterov 1983; Nemirovski–Yudin 1983; Polyak 1964; Lasso 1996; Markowitz 1952; Adam 2015; Rockafellar 1993 paraphrase; heavy ball failure; strict saddles avoided almost surely.
- **Information, codes, cryptography:** Kullback–Leibler 1951; Huffman 1952; Lempel–Ziv 1977/78; rate–distortion 1959; Tietäväinen, Zinoviev–Leontiev 1973; Singleton 1964; Gilbert 1952; Varshamov 1957; Tsfasman–Vlăduţ–Zink 1982; Berlekamp 1968; Berlekamp–McEliece–van Tilborg 1978; Guruswami–Sudan 1999; Gallager 1960/63; turbo 1993; Arıkan 2009; Shoup 1997; Cocks 1973, declassified 1997; Koblitz–Miller 1985; RSA-250 2020; Grover 1996; Regev 2005; SIKE 2022; McEliece 1978; LDPC and polar both in 5G; 256-bit curve ≈ 3,072-bit RSA; Kelly criterion as capacity.
- **Open as of 2026:** polynomial pivot rule; polynomial Hirsch; strongly polynomial LP; Gilbert–Varshamov tightness; relay and broadcast capacity; one-way functions; RSA versus factoring; Shor at cryptographic size.

### Layer 00 (W1)

- **Logic and proof theory:** Post 1921; Church and Turing 1936; Gentzen 1934–35; Jaśkowski 1934; Gentzen 1936; Szabo 1969; J. A. Robinson 1965; Haken 1985; Cook–Reckhow 1979; Henkin 1949; Rosser 1936; Lindström 1969; compactness of logic as compactness of the space of complete theories.
- **Model theory:** A. Robinson 1961; de Bruijn–Erdős 1951.
- **Foundations:** Gödel 1938; Cohen 1963; Kirby–Paris 1982; Frege 1893, 1903; Russell 1902; CH "debated as of 2026".
- **Geometry:** Hilbert's "tables, chairs and beer mugs"; Pasch 1882; Saccheri 1733; Lobachevsky 1829; Bolyai 1832; Beltrami 1868.
- **Computation and formal proof:** Appel–Haken 1976; Kempe 1879; Heawood 1890; Gonthier 2005; Hales 1998, Flyspeck 2014; Heule–Kullmann–Marek 2016 (7824/7825, about 200 TB).
- **Number theory and analysis:** Euler's sum-of-powers conjecture; Lander–Parkin 1966; Elkies 1988; Weierstrass 1872; Erdős 1947; Littlewood 1914; Fermat's descent for x⁴ + y⁴ = z²; Gelfond–Schneider 1934.
- **Constructive logic:** Heyting 1930; Kolmogorov 1932; Kripke 1965; Gödel and Gentzen 1933; Curry 1934; Howard 1969/1980; Bishop 1967; Brouwer's continuity principle.
- **Books:** Velleman 3rd 2019; Hammack 3rd 2018; Graham–Knuth–Patashnik 2nd 1994; Alon–Spencer 4th 2016; Greenberg 4th 2008; Kunen 1980; van Dalen 5th 2013; Wadler 2015; Heath 1908; Hartshorne 2000; Gelbaum–Olmsted 1964; Steen–Seebach 1970.

### Layer 08 (W9)

- **Classical geometry:** Pasch 1882; Hilbert's completeness axiom in later editions; Dehn's semi-Euclidean planes; Tarski decidability; Saccheri 1733; Beltrami 1868; Hilbert 1901; Thurston's trichotomy for knot complements; Bruck–Ryser 1949; Lam–Thiel–Swiercz 1989; order 12 open; Fedorov and Schoenflies 1891, 230 versus 219; Bieberbach; Berger 1966; Shechtman 1982; hat and spectre 2023; Sharpe 1997; Greenberg 1974; Thurston 1997.
- **Differential geometry:** Umlaufsatz; Fenchel; Fáry–Milnor; Gauss 1827; Chern 1944; Atiyah–Singer 1963; de Rham 1931; Hopf–Rinow 1931; Nash 1956; Perelman 2002–2003.
- **Convex and discrete:** McMullen 1970; Santos 2010; polynomial Hirsch open; Dehn 1900; Gauss 1831; Lagrange hexagonal lattice; Hales 1998/2005, Flyspeck 2014; Cohn–Elkies 2003; Viazovska 2016/2017, dimension 24, Fields 2022; optimal density known only in 1, 2, 3, 8, 24; LLL 1982; ML-KEM 2024; Thompson 1983; Conway–Sloane 1988.
- **Lie theory:** Cartan closed-subgroup theorem; diag(−2, −½) not an exponential in SL(2, ℝ) (trace argument; looks right); universal cover of SL(2, ℝ) has no faithful finite-dimensional representation; Killing 1888–1890; Cartan 1894; Langlands dual via reversed Dynkin arrows; Kac–Moody; Cartan 1913; Weyl 1925–1926; Peter–Weyl 1927; Wigner 1939; non-compact simple groups have no non-trivial finite-dimensional unitary representations; eightfold way.
- **Books:** Chevalley 1946; Stillwell 2008; Hall 2003; Humphreys 1972; Fulton–Harris 1991; Hawkins 2000; Bröcker–tom Dieck 1985; Sternberg 1994; Weyl 1928 (German original).

### Layer 13 (W14)

- **Category theory:** Freyd non-concretisability (c. 1970); Grothendieck universe ⇔ inaccessible; Kan 1958; Tôhoku 1957; Verdier 1960s; Hilbert syzygy 1890; Poincaré homology sphere π₁ of order 120; Quillen 1967; *Pursuing Stacks* 1983; Boardman–Vogt 1973; Curry, Howard 1969/1980, Lambek; Griffin 1990; Hofmann–Streicher 1994; Awodey–Warren, Voevodsky; simplicial model uses inaccessibles; cubical authors; Licata–Shulman 2013; mathlib and uniqueness of identity proofs; Riehl–Verity 2022; Lawvere–Tierney and forcing; Lawvere 1969.
- **Computability and incompleteness:** Ackermann 1928; Kleene 1936; Turing 1936/1937; Specker 1949; computable reals a real closed field; Rice 1953; totality Π₂-complete; Hilbert–Ackermann 1928; Löwenheim 1915; DPR 1961; Matiyasevich 1970; JSWW 1976; Hilbert's tenth by degree (4 undecidable, 2 decidable via Siegel 1972, 3 open); Dehn 1911; Novikov 1955, Boone; Adian–Rabin; Markov 1958; Magnus 1932; BB(5) = 47,176,870 (2024); Yedidia–Aaronson 2016 (7,918 states, later under 800); Rosser 1936; Feferman 1960; Q has 7 axioms; Gentzen 1935, 1936, 1943; Statman, Orevkov 1979; ordinals ω^ω (PRA), Γ₀ (ATR₀); Big Five table; Friedman 1975; Harrington and Friedman conservativity; Goodstein 1944 values; Kirby–Paris 1982; Paris–Harrington 1977.
- **Model theory:** Lindström 1969; Tennenbaum 1959; A. Robinson 1961, 1966; Morley 1965; ω + (ω* + ω)·η; Tarski 1948, 1951; Macintyre–Wilkie 1996; Wilkie 1996; Collins 1975; Davenport–Heintz 1988; Fischer–Rabin 1974; Presburger 1929; J. Robinson 1949; Ax–Kochen, Ershov 1965; Szmielew 1955; Trakhtenbrot 1950; Hrushovski 1996.
- **Forcing and large cardinals:** Gödel 1938/1940; Cohen 1963; Rasiowa–Sikorski; Easton 1970; Suslin (Jech 1967, Tennenbaum 1968, Solovay–Tennenbaum 1971); Shelah 1974; Lévy–Solovay 1967; Foreman–Magidor–Shelah 1988; Woodin and "V = Ultimate L"; Chow 2009; Shoenfield Σ¹₂; Ulam 1930; Scott 1961; Kunen 1971; Martin 1970; Martin–Steel 1989; Solovay 1970, Shelah 1984; AD equiconsistent with infinitely many Woodins; Maddy 1988; Reinhardt open.

### Layer 04 (W5)

- **Dates:** Peano 1888 (vector space axioms); Hamel 1905; Blass 1984; Jordan 1870; Cayley 1858, Frobenius 1878; Perron 1907; Frobenius 1912; Sylvester 1852; Cramer 1750; Grassmann 1844; Gram 1883; Schmidt 1907; Eckart–Young 1936; Moore 1920; Penrose 1955; Pearson 1901; Hotelling 1933; Leslie 1945; Brin–Page 1998 (α ≈ 0.85); Strassen 1969; de Silva–Lim 2008; Eilenberg–Mac Lane 1945 and V → V∗∗; Lagrange 1770s, Gauss 1801; *Nine Chapters*.
- **Claims:** ω ≈ 2.37; algebraic dual of ℝ[x] has uncountable dimension; inverse costs about three times a solve; R₀ thresholds; QR convergence; 7-dimensional cross product; ℓ¹ not reflexive, Lᵖ reflexive for 1 < p < ∞.
- **Books:** Axler 4th 2024; Strang 6th 2023; Lax 2nd 2007; Landsberg 2012; Lang 2002; Seneta 2nd 1981; Serre 1973; Arnold 1974/1978; Meyer 2000; Langville–Meyer 2006; Horn–Johnson 1985; Trefethen–Bau 1997; Stewart 1993.

### Layer 03 (W4)

- **Recent results:** Campos–Griffiths–Morris–Sahasrabudhe 2023, R(k, k) ≤ (4 − ε)ᵏ; PFR over 𝔽₂ⁿ 2023 and its Lean formalisation; Kelley–Meka 2023 "same shape as Behrend" (check: the exponent differs, so soften to "the same general form").
- **Small Ramsey numbers:** "R(5, 5) between 43 and 48" is likely out of date: the coordinator believes the upper bound was lowered to 46 in 2024 (Angeltveit–McKay); verify and update. R(3,4) = 9, R(3,5) = 14, R(4,4) = 18, R(3,3,3) = 17; Erdős "aliens" anecdote.
- **Open as of 2026:** Turán tetrahedron 5/9; union-closed sets (Gilmer 2022 and later fractions); Erdős progression conjecture (Bloom–Sisask 2020); Erdős–Szemerédi sum–product; Skolem problem; ex(n, C₈) and K₄,₄ exponents.
- **Attributions:** Hall 1935; König 1931; Berge 1957; Kuratowski 1930; Guthrie 1852; Kempe 1879; Heawood 1890; Hardy–Ramanujan 1918; Erdős 1959; Moser–Tardos 2010; Pascal–Fermat 1654; Kolmogorov 1933; Mirsky 1971; Dilworth 1950; Sperner 1928; Kővári–Sós–Turán 1954; Erdős–Stone 1946; Gowers 1997, 2001; Kahn–Kalai 1993; Behrend 1946; Paris–Harrington 1977; Schur 1916; van der Waerden 1927; Hales–Jewett 1963; Ruzsa 1994; ex(n, C₄) ~ n^(3/2)/2; Klein bottle the only Heawood exception (6 colours).
- **Other:** Stanley's 200+ Catalan families; Latin rectangles via Hall; Plünnecke–Ruzsa statement.
- **Books:** Elaydi 3rd 2005; Stanley vol. 1 2nd 2012; Grinstead–Snell 2nd 1997; Benjamin–Quinn 2003; Conlon–Fox–Sudakov 2015; Füredi–Simonovits 2013; Babai–Frankl 1992; Anderson 1987; Zhao 2023; Tao 2008.

### Layer 09 (W10)

- **Measure and integration:** Vitali 1905; Solovay 1970; Banach–Tarski 1924, five pieces; Lebesgue 1902; Riesz–Fischer 1907; Radon 1913; Nikodym 1930; von Neumann L² proof; Kolmogorov 1933; Hausdorff 1918; Hutchinson 1981; Mandelbrot 1975; Shishikura 1998; Cantor mass-distribution constant 2.
- **Complex analysis:** Riemann 1851 and Dirichlet principle; Poincaré ball versus bidisc; Koebe and Poincaré 1907; Riemann 1859; ∑z^(2ⁿ) radial behaviour.
- **Functional analysis:** Hahn and Banach late 1920s; Banach–Steinhaus 1927; Banach 1932; Banach–Mazurkiewicz 1931; Weierstrass 1872; Enflo 1973; Riesz and Fréchet 1907; Hahn–Banach without choice for separable spaces; Phillips (c₀ uncomplemented in ℓ^∞); Lᵖ (p ≠ 2) not Hilbertian; Lebesgue constants (4/π²)·log n.
- **Harmonic analysis:** Fourier 1822; Dirichlet 1829; du Bois-Reymond 1873; Fejér 1900; Gibbs about 9%; Kolmogorov 1923, 1926; Carleson 1966 (Luzin); Hunt 1968; Kahane–Katznelson; Dini–Lipschitz; Weyl 1916; Plancherel 1910; uncertainty constant 1/(16π²); Schwartz late 1940s, Fields 1950; multiplication impossibility 1950s; Malgrange–Ehrenpreis mid-1950s; Lewy 1957 statement (distributional form came later); Sobolev 1930s; Haar 1933; Pontryagin 1934, van Kampen 1935; Peter–Weyl 1927; Cooley–Tukey 1965, Gauss c. 1805; Roth 1953; Shor 1994; Tate 1950; MacWilliams via Walsh–Hadamard.
- **Books:** Ahlfors 3rd 1979; Needham 1997; Forster 1981; Brezis 2011; Lax 2002; Kreyszig 1978; Reed–Simon I 1972; Rudin FA 2nd 1991; Oxtoby 2nd 1980; Young 1988; Stein–Shakarchi 2003, 2003, 2005, 2011; Körner 1988; Katznelson 1968; Rudin 1962; Terras 1999; Strichartz 1994; Hörmander I 1983; Grubb 2009; Flajolet–Sedgewick 2009; Lieb–Loss 2nd 2001; Folland 2nd 1999; Rudin RCA 3rd 1987; Falconer 1990; Mandelbrot 1982; Tao 2011; Halmos 1950.

### Layer 06 (W7)

- Dates: Riemann 1854; Bolzano intermediate value theorem (IVT) 1817; Cauchy *Cours d'analyse* 1821 and its continuity claim; Weierstrass 1872 with 0 < a < 1, b odd, ab > 1 + 3π/2; Volterra 1881; Oresme 14th century; Fréchet 1906 thesis; Hausdorff named metric spaces 1914; Banach 1922; Green 1828; Hermite 1873; Lindemann 1882.
- Cantor's Cauchy-sequence construction of ℝ; Liouville and e^(−x²) having no elementary antiderivative.
- Open as of 2026: irrationality of γ and of π + e.
- Cauchy-complete non-Archimedean fields.
- Cauchy-product bound 2(n + 1)/(n + 2).
- x² + y²(1 − x)³: unique critical point, a strict local minimum, yet unbounded below.
- Peano's mixed-partials example (values −1 and 1).
- PageRank as a contraction in ℓ¹.
- Chapter numbers cited in Rudin and Spivak.
- Edition years: Körner 1988, Tao 2006, Hairer–Wanner 1996, Steele 2004, Stein–Shakarchi 2005, Hardy–Littlewood–Pólya 1934, Graham–Knuth–Patashnik 2nd 1994, Sutherland 2nd 2009, Ó Searcóid 2007, Kreyszig 1978, Granas–Dugundji 2003, Munkres 1991, Krantz–Parks 2002, Marsden–Tromba 6th 2012, Boyd–Vandenberghe 2004, Nocedal–Wright 2nd 2006, Schey 4th 2005; Knopp undated.

### Layer 12 (W13)

- 01–02 attributions: Kronecker stated Kronecker–Weber (proofs by Weber, Hilbert); Artin reciprocity 1927; class number one: Heegner 1952, Baker and Stark 1960s; Selmer 3x³ + 4y³ + 5z³ 1951; Jensen, infinitely many irregular primes; Chebyshev bounds c. 1850; Mertens 3–4–1 inequality; de la Vallée Poussin error term 1899; Littlewood sign changes 1914; Hardy 1914; Selberg 1942; Newman 1980; Bombieri–Vinogradov 1965; Vinogradov 1937; Chen announced 1966, published 1973.
- 01–02 claims: Helfgott preprints 2013, computer check with Platt; Polymath bounded gaps 246, parity problem blocks gap 2; Goldbach checked beyond 10¹⁸; RH checked for the first several trillion zeros; 61% heuristic for regular primes; Hardy–Littlewood assumed the Generalised Riemann Hypothesis (GRH) for ternary Goldbach; Euclid-style proofs work only for a² ≡ 1 mod q; Hilbert class field of ℚ(√−5) is ℚ(√−5, i).
- 03 dates: Hilbert basis theorem 1890, Nullstellensatz 1893, Buchberger 1965; Riemann's inequality 1850s, Roch 1860s; Weil's bound 1940s; EGA 1960–1967 with Dieudonné; FAC 1955; GAGA 1956; étale cohomology with Artin and Verdier.
- 04: Weil's extension of Mordell 1928; Hasse's bound 1930s; Hecke operators 1930s; Elkies rank ≥ 28 curve 2006; Gross–Zagier 1986, Kolyvagin 1989; Koblitz and Miller 1985; 256-bit curve ≈ 3072-bit RSA; Sato–Tate "Taylor and collaborators", no year; Frey mid-1980s, Hellegouarch first; Ribet 1986; Euler n = 3 1770; Wiles June 1993 Isaac Newton Institute, fix September 1994, Annals 1995; Khare–Wintenberger published 2009; Viazovska 2016, dimension 24 with collaborators; local Langlands GL(n) Harris–Taylor, Henniart c. 2000; Ngô 2008/2010, Fields 2010; geometric Langlands "proof announced in 2024 by Gaitsgory, Raskin and collaborators" (check refereeing status); "open as of 2026" list: general reciprocity/functoriality, BSD, RH, twin primes, binary Goldbach, Siegel zeros, Hilbert's 12th, boundedness of ranks.
- Writer verified by computation: 2(3, 5) on y² = x³ − 2; #E(𝔽₁₃) = 19; η(z)²η(11z)² coefficients; σ₇ identity; Jacobi four-square; j coefficients; τ values.

### Layer 10 (W11)

- Ordinary differential equations: Grobman 1959, Hartman 1960; Sturm and Liouville 1830s; Kakutani 1944.
- First-order: Kružkov 1970; Glimm 1965; multi-dimensional conservation-law systems "largely open as of 2026"; Crandall–Lions 1983.
- Heat: Tychonoff 1935 and growth class A·e^(a|x|²); Widder 1975; Ricci flow Hamilton 1982, Perelman 2002–2003.
- Wave: d'Alembert 1747; Courant–Friedrichs–Lewy (CFL) 1928; Kac 1966; Gordon–Webb–Wolpert 1992; Fritz John 4th 1982; Courant–Hilbert II 1962.
- Weak solutions: Lax–Milgram 1954; De Giorgi 1957, Nash 1958, De Giorgi counterexample 1968; Brezis 2011; Gilbarg–Trudinger 2nd 1983.
- Nonlinear: Hopf 1950, Cole 1951; Zabusky–Kruskal 1965; Gardner–Greene–Kruskal–Miura 1967; Lax 1968; Fujita 1966; Fefferman 2000, Navier–Stokes open as of 2026 (check 2025 computer-assisted blow-up work does not change the wording); Leray 1934; Caffarelli–Kohn–Nirenberg 1982; Escauriaza–Seregin–Šverák 2003; Tao 2016; Buckmaster–Vicol 2019; Turing 1952; Tao 2006; Drazin–Johnson 1989.
- Euler–Lagrange: Johann Bernoulli 1696; Euler and Lagrange 1740s–1750s; Gelfand–Fomin 1963; Feynman II ch. 19 (1964); Lanczos 1949; brachistochrone integral ∫√((1 + y′²)/y).
- Noether: 1918; Tavel translation 1971; invited to Göttingen 1915; Pauli 1926 and the four-dimensional hydrogen symmetry; swing as parametric pumping; Kosmann-Schwarzbach 2011; Olver 2nd 1993; Arnold 2nd 1989.
- Minimisers: Weierstrass 1870; Hilbert 1900; Ball–James 1987; Morrey 1952; Ball 1977; Ambrosetti–Rabinowitz 1973; Giusti 2003; Struwe 4th 2008.
- Iterated maps: May 1976; Feigenbaum 1978; Lanford 1982; Li–Yorke 1975; Sharkovskii 1964; Graczyk–Świątek and Lyubich 1997; Jakobson 1981; Douady–Hubbard 1982; parameters 3.5441 and 3.5644; Devaney 2nd 1989; de Melo–van Strien 1993.
- Bifurcations: Hopf 1942; Guckenheimer–Holmes 1983; Kuznetsov 3rd 2004; amplitude ≈ 2√μ for x″ − (μ − x²)x′ + x = 0.
- Chaos: Lorenz 1963; exponents ≈ 0.906, 0, −14.57; dimension ≈ 2.06; Hopf value 470/19; 0.506/0.506127 anecdote; 1972 butterfly talk; Banks et al. 1992; Poincaré 1890; Hénon 1976; Benedicks–Carleson 1991; classical Hénon attractor unproven as of 2026; Smale's 14th problem 1998; Tucker 2002; Gleick 1987.
- Ergodic: Zermelo 1896; Birkhoff 1931; von Neumann 1932; Weyl 1916; Kolmogorov 1958, Sinai 1959 settling von Neumann's question; Ornstein 1970; Szemerédi 1975; Furstenberg 1977; Furstenberg–Katznelson 1978; Green–Tao 2004/2008 "ideas from this approach"; Walters 1982; Furstenberg book 1981; Einsiedler–Ward 2011.
- Hamiltonian: Gromov 1985; Dirac 1925; Kovalevskaya 1888; Kolmogorov 1954, Arnold 1963, Moser 1962, τ > n − 1; Arnold diffusion 1964; Nekhoroshev 1977; Laskar 1989; Poincaré non-integrability wording; Moser 1973; *Les méthodes nouvelles* 1892–1899.
- Books: Teschl 2012; Axler et al. 2001; Mörters–Peres 2010; Coddington–Levinson 1955; Moler–Van Loan 2003; Perko 2001; Hirsch–Smale–Devaney 2013; Evans 2010; Lax 1973; Whitham 1974. Undated: Strogatz 2nd, Dacorogna, Lyapunov, Strauss.
- Style: "ODE" appears unexpanded inside Tucker's paper title in chaos Go deeper (acceptable as a title).

### Layers 14/04–06 and 15 (W16)

- 14/04–05: Buckingham 1914; Nyquist 1932; Doyle 1978; Choquet-Bruhat 1952; Stone 1932; Lovelock's theorem as stated; Verhulst 1838; May 1976; Cox–Ross–Rubinstein 1979; Harrison–Pliska 1981; Dalang–Morton–Willinger 1990; Delbaen–Schachermayer 1994; PPAD-completeness 2006; Maynard Smith–Price 1973; Axelrod 1984; Duncan Black 1948; "about 9%" Condorcet-cycle probability; Vapnik–Chervonenkis (VC) theory c. 1971.
- 14/06: Gaussian concentration constant 2e^(−t²/2); Lévy isoperimetric attribution; Wigner 1955; Marchenko–Pastur 1967; BBP threshold 1 + √γ (2005); Montgomery 1973; Shannon 1949 and precursors; Candès restricted isometry property (RIP) constant √2 − 1 (2008); Candès–Recht 2009; CD-audio figures; compressed sensing in clinical MRI; Cybenko 1989; Hornik et al. 1989; Leshno et al. 1993 (hypotheses simplified); Barron 1993; Rumelhart–Hinton–Williams 1986; Jacot–Gabriel–Hongler 2018; Zhang et al. 2017; Belkin et al. 2019 (title from memory); landscape claims (deep linear networks, strict saddles) uncited and simplified.
- 15 history: YBC 7289 dates; Rhind c. 1550 BCE; Madhava 14th century; Liu Hui 263; al-Khwārizmī c. 820; Lobachevsky 1829, Bolyai 1832; Bourbaki from 1939.
- 15 philosophy: Benacerraf 1965, 1973; Bishop 1967; Gentzen 1936 (ε₀); Hamming 1980; Field 1980; Gödel 1940.
- 15 practice: Pólya conjecture 1919, counterexample 906,150,257 (1980); Odlyzko–te Riele 1985; Littlewood 1914; BBP formula 1995; Voevodsky errors; De Millo–Lipton–Perlis 1979; Thurston 1994; Polymath January 2009.
- 15 computers and proof: Appel–Haken "nearly two thousand" configurations; Robertson–Sanders–Seymour–Thomas 1997 (633); Gonthier 2005; Hales 1998/2005; Flyspeck 2014; Boolean Pythagorean triples 2016 (7,825; ≈200 TB); S(5) = 160 (2017); Lean 2013; Coq renamed Rocq 2025; Feit–Thompson formalised 2012; Liquid Tensor December 2020/June 2021/July 2022; PFR formalised in about three weeks; FunSearch December 2023; AlphaGeometry January 2024 (25 of 30); IMO silver July 2024; **least sure:** July 2025 IMO gold-medal reports (DeepMind, OpenAI).
- 15 open problems: Conrey 1989 (> 40%); Leray 1934; Caffarelli–Kohn–Nirenberg 1982; Bhargava positive proportion for BSD; Chen 1973; Goldbach to 4 × 10¹⁸ (12 says "beyond 10¹⁸": make consistent); Helfgott 2013 "widely accepted"; Collatz to ≈ 2⁶⁸; Tao 2019; Conway 1972; Masser–Oesterlé 1985; Mochizuki 2021; Scholze–Stix 2018.
- 15 learning and teaching: Skemp 1976; Tall–Vinner 1981; Sweller 1988; Kirschner–Sweller–Clark 2006; Roediger–Karpicke 2006; Shulman 1986; Ma 1999; TIMSS 1995; PISA 2000.
- 15 society: GPS "tens of microseconds per day"; Radon 1917; 1979 Nobel (CT); Sally Clark 1999/2003, "1 in 73 million"; Berkeley 1973 data, 1975 paper; Gaussian copula 2000; Kleinberg–Mullainathan–Raghavan 2016; Chouldechova 2017; Viazovska Fields 2022; Uhlenbeck Abel 2019; Cost of Knowledge 2012; arXiv 1991.

## Cross-layer follow-ups (coordinator, after review pass)

- Root README names layer 14 "Applied & Computational Mathematics"; the files use "and". Align the root README.

- 03 links assume planned files cover: Borsuk–Ulam in 07 `fixed-point-theorems.md` (W8 confirms it does); Ramsey's theorem in 13 `proof-theory-and-reverse-mathematics.md`; diagonal Ramsey bounds in 15 `open-problems.md`; VC dimension in 14 `statistical-learning-theory.md`. Check after all drafts land.

- (06, W7) The extrema leaf links to 04 `the-spectral-theorem.md`; completeness/contraction links to 04 `non-negative-matrices-and-perron-frobenius.md`. Both are body-only links; confirm the targets cover what 06 assumes.

- (12, W13) Planned targets to confirm once written: 13 `higher-categories-and-homotopy-type-theory` (from Langlands Enables), 13 `quantifier-elimination-and-decidable-theories` (from Nullstellensatz Enables), 14 `error-correcting-codes` (Goppa codes, from curves Enables), 14 `high-dimensional-geometry-and-random-matrices` (from zeta Enables).

- (10, W11) Confirm 06 `compactness-in-metric-spaces` covers Arzelà–Ascoli; 07 `topological-spaces-and-continuous-maps` defines homeomorphism (stability leaf); 09 distributions fits as Builds on of characteristics. 03 additive-combinatorics is linked from 10 body text only.

- (14–15, W16) Sibling-tree links from 15: README → medicine history-of-medicine; history-of-mathematics Enables → CS history-of-computing and medicine history-of-medicine; philosophy-of-mathematics Enables → medicine the-scientific-method-and-models (loose fit); open-problems Enables → CS p-np-and-np-completeness. Goldbach verification bound differs between 12 and 15.
