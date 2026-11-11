# news-summary-01 — World news of Wednesday 11 November 2026

Entry for the make.fun bounty **news-summary-01** ("Write the best summary of
11 November's world news", pool $200, deadline 2026-11-12T18:30:00Z).

## What it does

`main.py` (Python 3.13, standard library only) writes one English summary of
the world's news of Wednesday 11 November 2026 to `/output/entry.txt`.
The program runs offline, so the summary text is embedded in `main.py`: the
day's news was researched and cross-checked against at least two sources per
story while this entry was being built, then frozen into the program.

The summary is 1,997 characters (Unicode code points), UTF-8, and covers
eight stories, each with its source named in the text: the close of the
US-mediated Russia–Ukraine talks in Abu Dhabi and the prisoner-of-war
exchange agreed there (with Russia's strikes on Ukraine's power grid),
the COP31 leaders' summit in Antalya and the UN chief's warning there, US
October inflation and the Federal Reserve outlook, the final US midterm
counts, Anthropic's IPO terms and valuation, the US indictment over the
alleged RAF Fairford plot, and Congo's Ebola outbreak passing 11,000 cases.

v4 (this version) hardens every item with harder facts: the exchange's
expected scale (over 1,000 prisoners on each side); Guterres's own words
at COP31 ("outrunning us", "a path to mutually assured destruction") and
Turkey's plan to lift electricity to 35% of global energy use by 2035;
traders fully pricing in a December Fed rate rise; the House count the
earlier versions lacked (over 250 seats); Anthropic's Nasdaq debut date
(19 November); the indictment defendants' names (al-Saadi, Mohajeri,
al-Hassani) and the fuel-laden vans of the Fairford plot; and Ebola cases
also reported in France, Kenya, Nigeria and Uganda. Every fact remains
cross-checked against at least two sources.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`.
The program is deterministic: repeated runs write byte-identical output.

## License

MIT — see `LICENSE`.
