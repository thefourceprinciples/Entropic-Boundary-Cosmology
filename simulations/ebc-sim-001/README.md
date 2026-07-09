# EBC-SIM-001 — Bright/Dark Entropic Clock

A first runnable toy simulator for Entropic Boundary Cosmology.

## Purpose

EBC-SIM-001 demonstrates a bounded toy universe with:

- a bright sector `B`
- a dark sector `D`
- a tunable boundary `∂`
- boundary flux `Phi_∂`
- internal entropic time `tau_E`
- Fource and Darkness Functional diagnostics

## Claim boundary

This is a **classical toy model**. It is not a quantitative BEC simulation and does not validate EBC as physical cosmology.

## Core clock law

```text
d tau_E / d lambda = Phi_∂ / Phi_0
```

In the reference implementation:

```text
Phi_∂ = boundary_crossings / N_particles
```

## Run the Python reference

```bash
python simulations/ebc-sim-001/python/ebc_sim_001_barrier_sweep.py
```

## Run the browser demo

Open:

```text
simulations/ebc-sim-001/web/index.html
```

## Metrics

- `tau_E` — internal entropic time
- `lapse` — entropic clock rate
- `flux` — boundary crossing rate
- `coherence` — bright-sector coherence proxy
- `fource` — framework-specific robustness score
- `darkness_functional` — return-path integrity proxy
