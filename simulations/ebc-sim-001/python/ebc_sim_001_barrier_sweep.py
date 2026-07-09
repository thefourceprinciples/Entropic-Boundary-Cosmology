#!/usr/bin/env python3
"""
EBC-SIM-001 — Bright/Dark Entropic Clock
Reference barrier-sweep toy implementation.

Claim boundary: classical toy model only. This is not a quantitative BEC simulator.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
import csv
import math
import random
from pathlib import Path
from typing import List


@dataclass
class Config:
    particles: int = 600
    steps: int = 1200
    phi0: float = 0.05
    seed: int = 140


@dataclass
class Result:
    kappa: float
    transmissivity: float
    final_tau_e: float
    mean_flux: float
    mean_lapse: float
    mean_coherence: float
    mean_fource: float
    darkness_functional: float


def transmissivity(kappa: float) -> float:
    """Simple monotonic boundary law for the toy model."""
    return math.exp(-5.0 * kappa)


def run(kappa: float, cfg: Config) -> Result:
    rng = random.Random(cfg.seed + int(kappa * 1000))
    T = transmissivity(kappa)

    # Sector labels: False = bright, True = dark.
    sectors = [rng.random() > 0.5 for _ in range(cfg.particles)]
    phases = [rng.random() * math.tau for _ in range(cfg.particles)]
    memory = phases[:]

    tau_e = 0.0
    fluxes: List[float] = []
    lapses: List[float] = []
    coherences: List[float] = []
    fources: List[float] = []
    return_scores: List[float] = []

    for _ in range(cfg.steps):
        crossings = 0
        for i in range(cfg.particles):
            # Boundary exchange attempt.
            if rng.random() < 0.025 * T:
                old_dark = sectors[i]
                sectors[i] = not sectors[i]
                crossings += 1
                if sectors[i] and not old_dark:
                    memory[i] = phases[i]
                elif (not sectors[i]) and old_dark:
                    score = 0.5 + 0.5 * math.cos(phases[i] - memory[i])
                    return_scores.append(score)

            # Weak phase drift/noise.
            phases[i] = (phases[i] + rng.gauss(0, 0.015)) % math.tau

        flux = crossings / cfg.particles
        lapse = flux / cfg.phi0 if cfg.phi0 else 0.0
        tau_e += lapse

        bright_phases = [phases[i] for i, s in enumerate(sectors) if not s]
        if bright_phases:
            c = abs(sum(complex(math.cos(p), math.sin(p)) for p in bright_phases) / len(bright_phases))
        else:
            c = 0.0

        exchange = 1.0 - math.exp(-flux / cfg.phi0) if cfg.phi0 else 0.0
        constraint = kappa / (1.0 + kappa)
        fource = c * exchange * constraint

        fluxes.append(flux)
        lapses.append(lapse)
        coherences.append(c)
        fources.append(fource)

    burn = max(1, cfg.steps // 5)
    recent_scores = return_scores[-200:]
    darkness_functional = sum(recent_scores) / len(recent_scores) if recent_scores else 0.0

    return Result(
        kappa=kappa,
        transmissivity=T,
        final_tau_e=tau_e,
        mean_flux=sum(fluxes[burn:]) / len(fluxes[burn:]),
        mean_lapse=sum(lapses[burn:]) / len(lapses[burn:]),
        mean_coherence=sum(coherences[burn:]) / len(coherences[burn:]),
        mean_fource=sum(fources[burn:]) / len(fources[burn:]),
        darkness_functional=darkness_functional,
    )


def main() -> None:
    cfg = Config()
    barriers = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    results = [run(k, cfg) for k in barriers]

    out_dir = Path(__file__).resolve().parents[1] / "data" / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "barrier_sweep_summary.csv"
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(results[0]).keys()))
        writer.writeheader()
        for r in results:
            writer.writerow(asdict(r))

    print(f"Wrote {out_path}")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
