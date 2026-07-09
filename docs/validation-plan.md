# Validation Plan

## v0.1 objective

Validate the toy metric layer, not a physical cosmology.

## Protocol 1 — Boundary sweep

Run the Python reference simulation while varying barrier opacity:

```text
kappa = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0
```

Expected qualitative result:

- transmissivity decreases as `kappa` increases
- boundary flux decreases as `kappa` increases
- entropic lapse decreases as `kappa` increases
- final `tau_E` decreases as `kappa` increases

## Protocol 2 — Sealed boundary

Force no boundary exchange.

Expected result:

```text
J_BD = 0
d tau_E / d lambda = 0
```

unless an entropy-proxy term is intentionally enabled.

## Protocol 3 — Darkness modes

Compare:

- fertile: returns preserve particle tokens
- corrupting: returns scramble particle tokens
- sealed: no exchange

Expected result:

- fertile mode has higher `D_F`
- corrupting mode has lower `D_F`
- sealed mode has near-zero exchange

## Protocol 4 — Sensitivity checks

Repeat with different seeds, particle counts, bin counts, and noise levels.

## Failure conditions

- `tau_E` decreases while `Phi_∂ >= 0`
- barrier opacity does not affect exchange
- Fource is indistinguishable from a simple entropy score
- Darkness Functional cannot be operationally measured as return-path integrity
