"""
This module prints exactly one paragraph of 13 dated world-news stories joined from a STORIES list.
"""

STORIES = [
    "Wednesday 11 November 2026. Abu Dhabi talks concluded with an expected prisoner swap exceeding 1,000 per side, termed the war's biggest humanitarian release by Jared Kushner, who flew with Steve Witkoff to Moscow for Putin then Dublin for Zelenskiy (AP, Reuters).",
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

# Print the 13 news stories joined into a single paragraph
print(" ".join(STORIES))
