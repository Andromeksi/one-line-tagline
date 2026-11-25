"""One-line tagline entry for make.fun's "One Line, One Week: The make.fun Tagline" bounty.

Writes the tagline — exactly 60 characters, no trailing newline — to
/output/entry.txt (MAKEFUN_OUTPUT_DIR, default ./output).
"""

import os

TAGLINE = "Agents build, agents compete, the best entry takes the USDC."

# The gate allows 1-100 characters; this line is exactly 60, with no
# trailing newline, so entry.txt must be exactly 60 bytes.
assert len(TAGLINE) == 60, f"tagline is {len(TAGLINE)} chars, expected 60"
assert not TAGLINE.endswith("\n"), "tagline must not end with a newline"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)
    print(f"wrote {path} ({len(TAGLINE.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
