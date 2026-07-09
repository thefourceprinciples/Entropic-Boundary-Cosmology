# Next Planks

## EBC-SIM-001 — Bright/Dark Entropic Clock

Status: initialized.

Purpose: demonstrate the EBC clock law with a classical toy universe.

```text
d tau_E / d lambda = Phi_∂ / Phi_0
```

## EBC-SIM-002 — Split-Step BEC-Inspired Field Layer

Next technical module.

Minimum deliverables:

1. `python/core/splitstep.py`
2. `python/core/potentials.py`
3. `python/ebc_gpe_1d_demo.py`
4. density heatmap for `|psi(x,t)|^2`
5. bright-sector coarse-grained entropy from masked density
6. same EBC metric interface: `S_B`, `Phi_E`, `tau_E`, `N_E`

Claim boundary: BEC-inspired mean-field dynamics, not a full many-body entanglement calculation.

## GLT-SIM-001 — Graphene Lattice Time Surface

A 2D hex-grid or KMC-inspired simulator for time-as-structure in graphene/crystal growth.

Fields:

- local birth time
- domain identity
- grain-boundary map
- defect density
- strain/constraint field
- coherence field
- Fource field

Core law:

```text
In 2D growth, time becomes visible when a moving boundary freezes invisible possibility into irreversible structure.
```

## Manuscript v0.2

Reviewer-hardening pass:

- sharper source citations
- figure placeholders
- formal definitions table
- rejection conditions
- expanded related-work section
- simulation reproducibility checklist
