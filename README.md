# Computational Physics Summer Project

Working through Mark Newman's *Computational Physics* textbook, building up
numerical methods in Python.

## Done so far

- **Numerical integration** — Simpson's rule, implemented and verified against SciPy
- **Random numbers & random walks** — 2D random walk (Brownian motion) on a
  discrete grid, with reflecting boundaries and an animated visualisation
  using `matplotlib.animation`

## Next up

- Mean squared displacement analysis of the random walk (checking diffusive
  scaling)
- Self-avoiding random walk
- More numerical methods, building toward the 2D Ising model and Monte Carlo
  option pricing

## Requirements

```
numpy
matplotlib
scipy
```

## Structure

- `numerical-methods/` — integration, root-finding, etc.
- `random-numbers/` — random number generation, random walks, Brownian motion