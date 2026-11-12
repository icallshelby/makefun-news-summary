import os
import sys

PART1 = (
    "Wednesday 11 November 2026. Abu Dhabi talks ended with an announced prisoner swap of 1,000 per side, called the war's biggest humanitarian release by Kushner, due in Moscow for Putin, then Dublin for Zelenskiy (AP, Reuters). "
    "The Telegraph reported Ukraine rejected a US proposal to redraw Donetsk and Luhansk borders as Abu Dhabi talks ended with no breakthrough. "
    "Ukraine struck Russia's Ust-Luga Baltic oil terminal, damaging 5 tanks with 150,000 m³ plus a hydrocracking unit (Ukrainian General Staff). "
    "NATO scrambled jets after at least 4 drones strayed into Baltic airspace during Ukrainian strikes on Russia (Reuters). "
    "Russia struck 6 electrical substations in Ukraine, injuring at least 14 (Ukrainian reports). "
    "At COP31, Guterres warned the climate crisis was 'outrunning us', as 102 leaders gathered (Reuters, Zark News). "
    "Delhi AQI hit 299 Wed, down from 307 Tue, 376 Mon, prompting hybrid classes (Zark News). "
    "Congo Ebola hit 11,042 infections, 5,387 deaths in 8 of 26 provinces, cases in France, Kenya, Nigeria and Uganda, whose outbreak ended (AP, WHO). "
)

PART2 = (
    "Iran designated Argentina's navy and air force as terrorist organisations in reciprocity for Argentina's April IRGC listing (Reuters). "
    "Tue: Israeli strikes killed at least 7 in Gaza, including a father and his 13-year-old son (Reuters). "
    "Tue: US charged three Iran-backed operatives over ~20 attacks, including an RAF Fairford fuel-van plot (DOJ). "
    "Tue: UK police arrested a US soldier, 41, near Gloucester for suspected Russian spying; uncharged (BBC, CNN). "
    "Tue: China posted $1.04T Jan-Oct trade surplus, October at $105.3B as exports rose 35.2% to $412.3B and imports 41.6% to $307.1B (Customs, Reuters). "
    "Tue: US CPI rose 0.4% in Oct, core 0.3%; traders priced Dec Fed rate rise (BLS). "
    "Tue: Anthropic set $70-$78 IPO range, targeting 19-20 Nov Nasdaq debut at implied $1.4T valuation, 7 buyers taking $26B (TechCrunch). "
    "Tue: House voted 211-204 sending 8 Hegseth articles to committee, effectively ending the effort (NPR)."
)

SUMMARY = PART1 + PART2
assert len(SUMMARY) == 1986, f"Expected length 1986, got {len(SUMMARY)}"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    else:
        out_path = "entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SUMMARY)
    sys.stdout.write(SUMMARY)

if __name__ == "__main__":
    main()
