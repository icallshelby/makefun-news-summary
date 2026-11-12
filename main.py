import os
import sys

def main():
    """Builds the November 11, 2026 news summary paragraph, writes it as UTF-8 bytes to entry.txt 
    in MAKEFUN_OUTPUT_DIR (defaulting to /output), and prints the code-point count to stdout.
    """
    prefix = "Wednesday 11 November 2026. "
    
    # Each story below preserves its exact facts, figures, dates, names, and source tags.
    stories = [
        "Abu Dhabi talks concluded with an expected prisoner swap exceeding 1,000 per side, termed the war's biggest humanitarian release by Jared Kushner, who flew with Steve Witkoff to Moscow for Putin then Dublin for Zelenskiy (AP, Reuters).",
        "China posted a $1.04T Jan-Oct trade surplus, with October at $105.3B as exports rose 35.2% to $412.3B and imports 41.6% to $307.1B (Customs, AP, CNBC, Reuters).",
        "In US midterms, Democrats won 54 Senate seats, flipping 7 including Texas, and over 250 House seats (AP).",
        "US CPI rose 0.4% in Oct, core 0.3%; traders fully priced a Dec Fed rate rise (Reuters).",
        "Anthropic set a $70-$78 IPO range for its 19 Nov Nasdaq debut at a $1.4T valuation, with 7 buyers taking $26B (SEC, Reuters).",
        "Russia struck energy infrastructure across 10 regions, hitting 5 substations, killing 2 in Vinnytsia and cutting power in 6 regions (Reuters).",
        "US unsealed charges against al-Saadi, Mohajeri and al-Hassani over ~20 attacks, including an RAF Fairford fuel-van plot (DOJ, AFP).",
        "At COP31, António Guterres warned the crisis was 'outrunning us', as Turkey planned 35% electricity from renewables by 2035 (Reuters).",
        "The House voted 211-204 to send 8 Hegseth articles to committee, ending the effort (Reuters, NPR).",
        "UK police arrested a 41-year-old US soldier near Gloucester over suspected Russian spying; uncharged, Moscow denied (BBC, CNN).",
        "Gaza truce frayed as Israeli strikes killed at least 8 in Gaza City and Khan Younis, including a father and young son (Gaza Health Ministry).",
        "Delhi AQI hit 299 at 7 a.m. Wed, down from 307 Tue and 376 Mon, prompting hybrid classes (Delhi briefing).",
        "Congo Ebola reached 11,042 infections and 5,387 deaths across 8 of 26 provinces, with cases in France, Kenya, Nigeria, Uganda (Reuters, AP)."
    ]
    
    paragraph = prefix + " ".join(stories)
    code_point_count = len(paragraph)
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(paragraph)
        
    print(code_point_count)
    if code_point_count > 2000:
        sys.exit(1)

if __name__ == "__main__":
    main()
