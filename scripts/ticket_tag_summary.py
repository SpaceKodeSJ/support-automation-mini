import csv
import sys
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("Usage: python ticket_tag_summary.py tickets.csv")
        sys.exit(1)

    inp = sys.argv[1]
    counts = Counter()

    # Expect a column called "tags" where tags are separated by commas
    with open(inp, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("No headers found.")
            sys.exit(1)

        # Try common tag column names
        tag_col = None
        for candidate in ["tags", "tag", "labels", "label"]:
            if candidate in [h.lower() for h in reader.fieldnames]:
                tag_col = candidate
                break

        # fallback: try exact match
        if "tags" in reader.fieldnames:
            tag_col = "tags"

        if not tag_col:
            print("Couldn't find a tags/labels column. Expected a column like 'tags'.")
            sys.exit(1)

        for row in reader:
            raw = row.get(tag_col) or row.get(tag_col.capitalize()) or ""
            tags = [t.strip().lower() for t in raw.split(",") if t.strip()]
            counts.update(tags)

    print("Top tags:")
    for tag, n in counts.most_common(20):
        print(f"{tag}: {n}")

if __name__ == "__main__":
    main()