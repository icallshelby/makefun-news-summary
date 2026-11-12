#!/usr/bin/env python3
"""news-summary-01 entry, v5: the world's news of Wednesday 11 November 2026.

Writes one English summary, embedded below, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Offline, deterministic, standard library only: the news was researched
while this entry was being built and is frozen into the text.

v5 changes vs v4: breadth grows from eight stories to ten, funded by
compressing the incumbents instead of thinning their facts. Two new
11 Nov stories, each cross-checked against at least two sources: the
arrest in Britain of a 41-year-old US soldier on suspicion of spying
for Russia (BBC, CNN) and the House vote 211-204 sending the Hegseth
impeachment articles to committee (Reuters, NPR). Cuts that fund
them: the talks' duration, the CPI shutdown clause, Anthropic's share
count and raise, the indictment's "in Europe and the US", Ebola's
"second-largest ever" and vaccine clause. What v5 keeps from v4:
the POW exchange's expected scale, Guterres's own words and Turkey's
35%-by-2035 plan at COP31, the fully priced December Fed hike, the
House count, Anthropic's Nasdaq debut date, the seven placement
buyers, the three named defendants and the Fairford fuel vans, and
Ebola's spread to France, Kenya, Nigeria and Uganda.
"""

import os
from pathlib import Path

SUMMARY = (
    "Wednesday 11 November 2026. "
    "Russia and Ukraine ended US-mediated Abu Dhabi talks, agreeing "
    "an exchange expected to top 1,000 prisoners on each side, "
    "which US envoy Jared Kushner called the war's biggest "
    "humanitarian release; no breakthrough on ending the war. "
    "Kushner and Witkoff take them to Moscow on Thursday to "
    "meet Putin, then Dublin to meet Zelenskiy (AP, Reuters). "
    "Russia struck energy sites in 10 regions, hitting five "
    "substations, killing two in Vinnytsia, cutting power in six "
    "regions (Reuters). "
    "British police arrested a 41-year-old US soldier near "
    "Gloucester on suspicion of spying for Russia; the NATO corps "
    "serviceman was not charged, and Moscow denied involvement "
    "(BBC, CNN). "
    "At COP31, António Guterres warned the crisis was "
    "'outrunning us' on 'a path to mutually assured destruction', "
    "as Turkey pushed electricity to 35% of energy use by "
    "2035 (Reuters). "
    "US consumer prices rose 0.4% in October, core 0.3%, both above "
    "forecasts; traders fully priced in a December Fed rate rise "
    "(Reuters). "
    "In the US midterms, Democrats took both houses: 54 "
    "Senate seats, flipping seven Republican seats including "
    "Texas, and over 250 House seats, with Alaska and Mississippi "
    "still uncalled (AP). "
    "The House voted 211-204 to send eight articles against "
    "Secretary Pete Hegseth to committee, effectively ending the "
    "effort this Congress (Reuters, NPR). "
    "Anthropic set a $70-$78 IPO range (ANT on Nasdaq, trading "
    "19 November), valuing it up to $1.4 trillion fully diluted, "
    "with Google, Nvidia, AMD, Broadcom, Micron, Microsoft and "
    "TSMC buying $26 billion (SEC filing, Reuters). "
    "The US unsealed an eight-count indictment charging al-Saadi, "
    "Mohajeri and al-Hassani as operatives for Iran's IRGC and "
    "Kata'ib Hizballah over nearly 20 attacks, including a "
    "fuel-laden-van plot at RAF Fairford; Iran denied involvement "
    "(DOJ, AFP). "
    "Congo's Ebola outbreak hit 11,042 infections and 5,387 "
    "deaths; its Bundibugyo strain is in eight of 26 provinces, "
    "cases also in France, Kenya, Nigeria and Uganda "
    "(Reuters, AP)."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(SUMMARY.encode("utf-8"))


if __name__ == "__main__":
    main()
