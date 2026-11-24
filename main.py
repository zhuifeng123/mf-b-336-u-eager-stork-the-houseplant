import os

ENTRY = "Out of office. You've ignored me since March; consider this mutual. — Fern"

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    assert len(ENTRY) <= 120, len(ENTRY)
    print(f"{path}: {len(ENTRY)} chars")
    print(ENTRY)

if __name__ == "__main__":
    main()
