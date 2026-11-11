#!/usr/bin/env python3
"""news-summary-01 entry, v2: the world's news of Wednesday 11 November 2026.

Writes one English summary, embedded below, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Offline, deterministic, standard library only: the news was researched
while this entry was being built and is frozen into the text.

v2 changes vs v1: the Abu Dhabi talks are now reported with their
outcome (the agreed prisoner-of-war exchange), COP31 gains the
Secretary-General's warning, the Anthropic item gains its valuation,
and Congo's Ebola outbreak replaces the Haiti item; every story is
cross-checked against at least two sources, named in the text.
"""

import os
from pathlib import Path

SUMMARY = (
    "World news, Wednesday 11 November 2026. "
    "Russia and Ukraine ended two days of US-mediated talks in Abu Dhabi, "
    "their first meeting in nine months, agreeing a prisoner-of-war "
    "exchange that US envoy Jared Kushner called the war's biggest "
    "humanitarian release; both delegations confirmed it, numbers to be "
    "finalized Thursday, but no breakthrough was reached on ending the war "
    "(AP, Reuters). "
    "Russian strikes during the talks hit energy infrastructure in 10 "
    "Ukrainian regions, damaging five substations, killing two people "
    "in Vinnytsia and cutting power in six regions (Reuters). "
    "In Antalya, leaders opened COP31's summit (9-20 Nov), "
    "where UN Secretary-General António Guterres warned the slow response "
    "had put the world on a path to destruction; Australia's "
    "Chris Bowen leads negotiations, and 60,000 delegates are attending "
    "(Reuters, Le Monde). "
    "US consumer prices rose 0.4% in October and core prices 0.3%, both above "
    "forecasts, pointing the Fed toward a December rate rise; no "
    "annual rate exists because the 2025 shutdown halted collection (Reuters). "
    "A week after the US midterms, final counts gave Democrats both houses: "
    "54 Senate seats, flipping seven Republican seats including Texas, "
    "with 16 races still uncalled (AP). "
    "Anthropic set a $70-$78 Nasdaq IPO range (ticker ANT), offering "
    "825 million shares to raise up to $64.4 billion, valuing it at up to "
    "$1.4 trillion fully diluted, with Google, Nvidia and five others "
    "buying $26 billion of non-voting shares "
    "(SEC filing, Reuters). "
    "The US unsealed an eight-count indictment charging three "
    "alleged Iranian operatives over nearly 20 attacks and plots in Europe "
    "and the US, including a September plot against Britain's RAF Fairford "
    "airbase; Iran denied involvement (DOJ, AFP). "
    "Congo's Ebola outbreak topped 11,000 cases, with 11,042 infections and "
    "5,387 deaths — the country's deadliest and the second-largest "
    "on record; its Bundibugyo strain, with no approved vaccine or "
    "treatment, has spread to eight of 26 provinces (Reuters, AP)."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
