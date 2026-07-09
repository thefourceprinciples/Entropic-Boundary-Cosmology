import math

from ebc_sim_001_barrier_sweep import transmissivity, run, Config


def test_transmissivity_monotonic():
    values = [transmissivity(k) for k in [0.0, 0.2, 0.4, 0.8, 1.0]]
    assert values == sorted(values, reverse=True)


def test_tau_is_nonnegative():
    result = run(0.4, Config(particles=100, steps=50, seed=1))
    assert result.final_tau_e >= 0


def test_high_barrier_reduces_transmissivity():
    assert transmissivity(1.0) < transmissivity(0.0)
    assert math.isclose(transmissivity(0.0), 1.0)
