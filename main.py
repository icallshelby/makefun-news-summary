import os
import sys

# 14 stories ordered by consequence, reordered and restructured
STORIES = [
    "RU-Ukraine: US-mediated Abu Dhabi talks concluded without peace breakthrough; agreed prisoner exchange >1,000 per side, termed war's biggest humanitarian release by Jared Kushner, who flew with Steve Witkoff to Moscow for Putin then Dublin for Zelenskiy.",
    "China posted a Jan-Oct trade surplus of $1.04T with October at $105.3B, driven by exports rising 35.2% to $412.3B and imports gaining 41.6% to $307.1B.",
    "Trump-APEC: Donald Trump stated on Nov 8 he anticipates meeting Xi and Putin at the Shenzhen APEC summit Nov 18-19 regarding Iran and denuclearization, while Beijing stated it is communicating without confirming.",
    "US midterms: Democrats won 54 Senate seats, flipping 7 including Texas, and >250 House seats.",
    "US economy: CPI +0.4% in Oct, core +0.3%; traders fully priced a Dec Fed rate rise.",
    "Anthropic: $70-$78 IPO range, Nasdaq 19 Nov, $1.4T valuation, 7 buyers taking $26B.",
    "Russia struck energy in 10 regions, hitting 5 substations, killing 2 in Vinnytsia, cutting power in 6 regions.",
    "US unsealed indictment charging al-Saadi, Mohajeri and al-Hassani over ~20 attacks, including RAF Fairford fuel-van plot.",
    "COP31: António Guterres warned crisis 'outrunning us'; Turkey planned 35% electricity by 2035.",
    "House voted 211-204 sending 8 Hegseth articles to committee, ending effort.",
    "British police arrested 41-year-old US soldier near Gloucester over suspected Russian spying; uncharged, Moscow denied.",
    "Gaza truce frayed as Israeli strikes killed at least 8 in Gaza City and Khan Younis, including father and young son.",
    "Delhi AQI 299 at 7 a.m. Wed, down from 307 Tue and 376 Mon, prompting hybrid classes.",
    "Congo Ebola: 11,042 infections, 5,387 deaths across 8 of 26 provinces; cases in France, Kenya, Nigeria, Uganda."
]

def generate_summary() -> str:
    parts = []
    for s in STORIES:
        parts.append(s)
    return " ".join(parts)

def main():
    summary = generate_summary()
    code_points = len(summary)
    print(f"Final code point count: {code_points}")
    if code_points > 2000:
        print("ERROR: Summary exceeds 2000 Unicode code points!", file=sys.stderr)
        sys.exit(1)
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"Successfully wrote summary to {output_path}")

if __name__ == "__main__":
    main()
