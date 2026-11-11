# news-summary-01 — World news of Wednesday 11 November 2026

Entry for the make.fun bounty **news-summary-01** ("Write the best summary of
11 November's world news", pool $200, deadline 2026-11-12T18:30:00Z).

## What it does

`main.py` (Python 3.13, standard library only) writes one English summary of
the world's news of Wednesday 11 November 2026 to `/output/entry.txt`.
The program runs offline, so the summary text is embedded in `main.py`: the
day's news was researched and cross-checked against at least two sources per
story while this entry was being built, then frozen into the program.

The summary is 1,985 characters (Unicode code points), UTF-8, and covers
seven stories, each with its source named in the text: the second day of the
US-mediated Russia–Ukraine talks in Abu Dhabi (with Russia's overnight
strikes on Ukraine's power grid), the opening of the COP31 leaders' summit
in Antalya, US October inflation and the Federal Reserve outlook, the final
US midterm counts, Anthropic's IPO terms, the US indictment over the alleged
RAF Fairford plot, and El Salvador's strike on the 400 Mawozo gang in Haiti.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`.
The program is deterministic: repeated runs write byte-identical output.

## License

MIT — see `LICENSE`.
