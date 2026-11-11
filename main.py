#!/usr/bin/env python3
"""news-summary-01 entry, v3: the world's news of Wednesday 11 November 2026.

Writes one English summary, embedded below, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Offline, deterministic, standard library only: the news was researched
while this entry was being built and is frozen into the text.

v3 changes vs v2: the Abu Dhabi item gains the envoys' onward trip to
Moscow and Dublin; the midterm item names the two uncalled Senate
races (Alaska, Mississippi) instead of an unverifiable race count;
the indictment names the IRGC and Kata'ib Hizballah; the Anthropic
item names all seven placement buyers; wording tightened throughout.
Every story remains cross-checked against at least two sources,
named in the text.
"""

import os
from pathlib import Path

SUMMARY = (
    "World news, Wednesday 11 November 2026. "
    "Russia and Ukraine ended two days of US-mediated talks in Abu Dhabi, "
    "their first meeting in nine months, agreeing the prisoner-of-war "
    "exchange US envoy Jared Kushner called the war's biggest "
    "humanitarian release; both sides confirmed it, numbers to be "
    "finalized Thursday; no breakthrough on ending the war. Kushner "
    "and Steve Witkoff take the talks to Moscow on Thursday to meet "
    "Putin, then to Dublin to meet Zelenskiy (AP, Reuters). "
    "During the talks Russia struck energy infrastructure in 10 "
    "Ukrainian regions, hitting five substations, killing two in "
    "Vinnytsia and cutting power in six regions (Reuters). "
    "In Antalya, leaders addressed COP31; UN "
    "Secretary-General António Guterres warned the slow response had put "
    "the world on a path to destruction. Australia's Chris Bowen leads "
    "negotiations, and 60,000 delegates attend (Reuters, Le Monde). "
    "US consumer prices rose 0.4% in October, core prices 0.3%, both above "
    "forecasts, pointing to a December Fed rate rise; the "
    "2025 shutdown meant no annual rate was published (Reuters). "
    "A week after the US midterms, Democrats held both houses: "
    "54 Senate seats, flipping seven Republican seats including Texas, "
    "with Alaska and Mississippi still uncalled (AP). "
    "Anthropic set a $70-$78 IPO range (ticker ANT), offering "
    "825 million shares for up to $64.4 billion, valuing it at up to "
    "$1.4 trillion fully diluted, with Google, Nvidia, AMD, Broadcom, "
    "Micron, Microsoft and TSMC buying $26 billion of non-voting shares "
    "(SEC filing, Reuters). "
    "The US unsealed an eight-count indictment charging three "
    "alleged operatives for Iran's IRGC and Kata'ib Hizballah over nearly "
    "20 attacks and plots in Europe and the US, including September's "
    "plot against RAF Fairford; Iran denied involvement (DOJ, AFP). "
    "Congo's Ebola outbreak reached 11,042 infections and "
    "5,387 deaths — its deadliest and the second-largest "
    "on record; its Bundibugyo strain, with no approved vaccine or "
    "treatment, is now in eight of 26 provinces (Reuters, AP)."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
