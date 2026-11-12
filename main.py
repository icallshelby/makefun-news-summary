import os
import sys

PREFIX = "Wednesday 11 November 2026. "
STORIES = [
    "Russia and Ukraine ended US-mediated talks in Abu Dhabi, their first meeting in nine months, agreeing the prisoner exchange Kushner called the war's biggest humanitarian release; no breakthrough on ending the war.",
    "Kushner and Witkoff go to Moscow for Putin, then Dublin for Zelenskiy (AP, Reuters).",
    "Russia struck energy sites in 10 regions, hitting 5 substations, killing 2 in Vinnytsia and cutting power in 6 regions (Reuters).",
    "China posted a $1.04 trillion Jan-Oct trade surplus, Oct $105.3B, exports +35.2% to $412.3B, imports +41.6% to $307.1B (Customs, Reuters).",
    "After the US midterms, Democrats held both houses: 54 Senate seats, flipping seven including Texas, Alaska and Mississippi still uncalled (AP).",
    "US consumer prices rose 0.4% in October, core 0.3%, both above forecasts, pointing to a December Fed rate rise; no annual rate after the 2025 shutdown (Reuters).",
    "Anthropic set a $70-$78 IPO range (ticker ANT), 825 million shares for up to $64.4 billion, valuing it up to $1.4 trillion, with Google, Nvidia, AMD, Broadcom, Micron, Microsoft and TSMC buying $26 billion (SEC, Reuters).",
    "Leaders addressed COP31 in Antalya; UN chief António Guterres warned the response had put the world on a path to destruction; 60,000 delegates attend (Reuters).",
    "The US unsealed an eight-count indictment charging three alleged IRGC and Kata'ib Hizballah operatives over nearly 20 attacks, including September's RAF Fairford plot; Iran denied it (DOJ, AFP).",
    "Gaza truce frayed as Israeli strikes killed at least 8 in Gaza City and Khan Younis, including a father and young son (Gaza Health Ministry).",
    "The House voted 211-204 to send 8 Hegseth articles to committee, ending the effort (Reuters, NPR).",
    "Delhi AQI hit 299 Wed morning, down from 307 Tue and 376 Mon, prompting hybrid classes (Delhi briefing).",
    "Congo's Ebola reached 11,042 infections and 5,387 deaths, its deadliest and second-largest on record; the Bundibugyo strain has no approved vaccine (Reuters, AP)."
]

SUMMARY = PREFIX + " ".join(STORIES)

if len(SUMMARY) != 1988:
    raise AssertionError(f"Expected 1988 code points, got {len(SUMMARY)}")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SUMMARY)
    sys.stdout.write(str(len(SUMMARY)))

if __name__ == "__main__":
    main()
