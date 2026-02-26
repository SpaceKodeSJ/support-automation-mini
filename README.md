# Support Automation Mini Tools (SJ)

A small collection of Python scripts that reflect common support/ops tasks: cleaning CSV exports and summarising ticket tags.

## Scripts
- `scripts/csv_cleaner.py` — cleans a CSV export (removes blank rows, normalises headers, outputs cleaned file)
- `scripts/ticket_tag_summary.py` — reads a CSV of tickets and outputs a tag frequency report

## Why this exists
I work in SaaS support/ops and use automation to reduce repetitive work and improve reporting/visibility.

## How to run
```bash
python scripts/csv_cleaner.py input.csv output.csv
python scripts/ticket_tag_summary.py tickets.csv

