#!/usr/bin/env python3
"""news-summary-01 entry, v7: the world's news of Wednesday 11 November 2026.

Writes one English summary, built from a list of 13 stories, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Offline, deterministic, standard library only.
"""

import os
from pathlib import Path

STORIES = [
    "Russia and Ukraine ended US-mediated Abu Dhabi talks, agreeing an exchange expected to top 1,000 prisoners on each side, which Jared Kushner called the war's biggest humanitarian release; Kushner and Witkoff fly to Moscow to meet Putin, then Dublin for Zelenskiy (AP, Reuters).",
    "China posted a $1.04 trillion Jan-Oct trade surplus, with October $105.3 billion as exports rose 35.2% to $412.3 billion and imports 41.6% to $307.1 billion (Customs, AP, CNBC, Reuters).",
    "In US midterms, Democrats took 54 Senate seats, flipping 7 including Texas, and over 250 House seats (AP).",
    "US consumer prices rose 0.4% in October, core 0.3%; traders fully priced a December Fed rate rise (Reuters).",
    "Anthropic set a $70-$78 IPO range (Nasdaq 19 Nov, $1.4T valuation) with 7 buyers taking $26B (SEC, Reuters).",
    "Russia struck energy sites in 10 regions, hitting 5 substations, killing 2 in Vinnytsia and cutting power in 6 regions (Reuters).",
    "The US unsealed an indictment charging al-Saadi, Mohajeri and al-Hassani over ~20 attacks, including an RAF Fairford fuel-van plot (DOJ, AFP).",
    "At COP31, António Guterres warned the crisis was 'outrunning us', as Turkey planned 35% electricity by 2035 (Reuters).",
    "The House voted 211-204 to send 8 Hegseth articles to committee, ending the effort (Reuters, NPR).",
    "British police arrested a 41-year-old US soldier near Gloucester over suspected Russian spying; uncharged, Moscow denied (BBC, CNN).",
    "Gaza truce frayed as Israeli strikes killed at least 8 in Gaza City and Khan Younis including father and young son (Gaza Health Ministry, Democracy Now).",
    "Delhi air AQI hit 299 at 7 a.m. Wed, down from 307 Tue and 376 Mon, prompting hybrid classes (Delhi briefing).",
    "Congo's Ebola outbreak hit 11,042 infections and 5,387 deaths across 8 of 26 provinces, with cases in France, Kenya, Nigeria and Uganda (Reuters, AP).",
]

SUMMARY = "Wednesday 11 November 2026. " + " ".join(STORIES)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
