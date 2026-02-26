import csv
import sys

def clean_header(h: str) -> str:
    return h.strip().lower().replace(" ", "_")

def main():
    if len(sys.argv) < 3:
        print("Usage: python csv_cleaner.py input.csv output.csv")
        sys.exit(1)

    inp, out = sys.argv[1], sys.argv[2]

    with open(inp, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("Input file is empty.")
        sys.exit(1)

    header = [clean_header(h) for h in rows[0]]
    data = [r for r in rows[1:] if any(cell.strip() for cell in r)]

    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    print(f"Cleaned {len(data)} rows -> {out}")

if __name__ == "__main__":
    main()