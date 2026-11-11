#!/usr/bin/env python3
"""news-summary-01 entry: the world's news of Wednesday 11 November 2026.

Writes one English summary, embedded below, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Offline, deterministic, standard library only: the news was researched
while this entry was being built and is frozen into the text.
"""

import os
from pathlib import Path

SUMMARY = (
    "World news, Wednesday 11 November 2026. "
    "Russia, Ukraine and the United States held a second day of US-mediated talks in Abu Dhabi, "
    "their first trilateral meeting in nine months; day one ran nearly four hours, was called "
    "constructive, and covered security guarantees, Europe's security architecture and a possible "
    "prisoner swap, with no deal announced (AP). "
    "As the talks opened, Russian strikes hit energy infrastructure in 10 Ukrainian regions, "
    "damaging five major substations, killing two people in Vinnytsia and cutting power in "
    "six regions (Reuters). "
    "In Antalya, Türkiye, world leaders opened COP31's leaders' summit at the UN "
    "climate conference (9-20 Nov): Türkiye's Murat Kurum is president, Australia's Chris Bowen "
    "leads negotiations, and some 60,000 delegates are attending (Le Monde, UNFCCC). "
    "US consumer prices rose 0.4% in October and core prices 0.3%, both above forecasts in "
    "Tuesday's figures, putting the Federal Reserve toward a December rate rise; no annual "
    "rate was published because the 2025 shutdown halted data collection (Reuters). "
    "A week after the US midterms, final counts gave Democrats both houses of Congress: 54 "
    "Senate seats after flipping seven Republican seats, Texas among them, with 16 races still "
    "uncalled (AP). "
    "Anthropic set a $70-$78 price range for its Nasdaq IPO (ticker ANT), offering 825 million "
    "shares to raise up to $64.4 billion, with Google, Nvidia and five other suppliers buying "
    "$26 billion of non-voting shares alongside (SEC filing). "
    "US prosecutors unsealed an eight-count indictment charging three alleged Iranian operatives "
    "over nearly 20 attacks and plots in Europe and the US, including a September plot against "
    "Britain's RAF Fairford airbase; Iran denied involvement (DOJ, AFP). "
    "In Haiti, President Nayib Bukele said Salvadoran troops and Haitian police destroyed the "
    "400 Mawozo gang's headquarters in Croix-des-Bouquets and the home of its leader Wilson "
    "Joseph; reports of 20 killed were not independently confirmed (BBC, Al Jazeera)."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
