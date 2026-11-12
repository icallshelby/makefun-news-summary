import os
import sys

PREFIX = "Wednesday 11 November 2026. "

STORIES = [
    "Abu Dhabi talks ended with prisoner swap over 1,000 per side, termed war's biggest humanitarian release by Jared Kushner, who flew with Steve Witkoff to Moscow for Putin then Dublin for Zelenskiy (AP, Reuters).",
    "China posted $1.04T Jan-Oct trade surplus, October at $105.3B as exports rose 35.2% to $412.3B and imports 41.6% to $307.1B (Customs, AP, CNBC, Reuters).",
    "In US midterms, Democrats won 54 Senate seats, flipping 7 including Texas, plus over 250 House seats (AP).",
    "US CPI rose 0.4% in Oct, core 0.3%; traders priced Dec Fed rate rise (Reuters).",
    "Anthropic set $70-$78 IPO range for 19 Nov Nasdaq debut at $1.4T valuation, 7 buyers taking $26B (SEC, Reuters).",
    "Russia struck energy infrastructure across 10 regions, hitting 5 substations, killing 2 in Vinnytsia, cutting power in 6 (Reuters).",
    "Ukraine struck Russia's Ust-Luga Baltic oil terminal, damaging 5 tanks holding 150,000 cubic metres plus a hydrocracking unit (Ukrainian General Staff).",
    "NATO scrambled jets after at least four drones strayed into Baltic airspace during Ukrainian strikes on Russia (NATO).",
    "US unsealed charges against al-Saadi, Mohajeri and al-Hassani over ~20 attacks, including RAF Fairford fuel-van plot (DOJ, AFP).",
    "At COP31, António Guterres warned crisis was 'outrunning us', as Turkey planned 35% renewable electricity by 2035 (Reuters).",
    "House voted 211-204 sending 8 Hegseth articles to committee, ending effort (Reuters, NPR).",
    "UK police arrested 41-year-old US soldier near Gloucester over suspected Russian spying; uncharged, Moscow denied (BBC, CNN).",
    "Gaza truce frayed as Israeli strikes killed at least 8 in Gaza City and Khan Younis, including father, son (Gaza Health Ministry).",
    "Delhi AQI hit 299 at 7 a.m. Wed, down from 307 Tue and 376 Mon, prompting hybrid classes (Delhi briefing).",
    "Congo Ebola hit 11,042 infections, 5,387 deaths across 8 of 26 provinces, with cases in France, Kenya, Nigeria, Uganda (Reuters, AP)."
]

def main():
    paragraph = PREFIX + " ".join(STORIES)
    count = len(paragraph)
    
    if count > 2000:
        sys.stderr.write(f"Error: length {count} exceeds 2000 code points.\n")
        sys.exit(1)
        
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(paragraph)
    except Exception as e:
        sys.stderr.write(f"Warning/Error writing output: {e}\n")
        raise
        
    print(count)

if __name__ == "__main__":
    main()
