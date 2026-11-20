"""News-image entry for make.fun's news-image-20261120 bounty.

Copies the finished 20 November 2026 world-news summary image (entry.png,
drawn during the build) to the grader's output directory as entry.png.
Standard library only; deterministic, so both grader runs write the same
bytes. The output is exactly the repository's entry.png, byte for byte.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
