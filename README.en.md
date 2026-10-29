# txt — paste a messy list, get the shape you want

> Paste a messy list of lines: dedupe, sort, drop blanks, then emit a comma string, a JSON array, a Markdown list or an SQL IN (...) clause. Everything runs in your browser; the text never leaves the page.

English | [中文](README.md)

## What it is

Copying a pile of IPs, filenames or IDs off a server and turning them into arguments usually means wrestling with `sort -u` and `sed`. This page turns that chore into a few toggles: paste, tick boxes, copy the right-hand side.

There is no backend logic at all — just an empty shell page. Processing is four fixed steps: trim, drop blank lines, dedupe, change case, then sort. Dedupe keeps the first occurrence, and the trailing newline does not count as a line (otherwise the count is always off by one).

Output format is a separate step: one per line, comma string, JSON array, Markdown list, SQL `IN (...)`, or each line quoted. The SQL option doubles single quotes so the result drops into a statement without breaking. Five preset buttons cover the common combinations so you do not touch the dropdowns every time.

## Features

- Trim, drop blanks and dedupe, freely combinable
- Sort A→Z, Z→A, by length, shuffle, or keep original order
- Output one per line, comma string, JSON array, Markdown list, SQL IN, or quoted lines
- Five one-click presets for everyday combinations
- Live counts: input lines, result lines, duplicates removed, byte size
- Computes as you paste (150ms debounce), no submit button
- Auto light/dark plus manual toggle; single column on narrow screens

## Stack

Python 3.12 · Flask 3.1 · 原生 JS

## Run

```bash
pip install -r requirements.txt
python app.py  # 默认 127.0.0.1:8880
```

## About

Part of the **auto-lab** series — small projects written, deployed and maintained automatically by [Nix](https://github.com/Uxnar-ai) on a self-hosted server.

Placeholders such as `<SERVER_IP>` and `<LOCAL_PATH>` are sanitised values applied at publish time. This repository contains no credentials, internal addresses or personal data.

## License

MIT
