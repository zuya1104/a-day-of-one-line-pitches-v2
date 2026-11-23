#!/usr/bin/env python3
"""Write the one-line pitch to /output/entry.txt.

One sentence, at most 240 characters, that would convince a friend who
has never coded to let an AI agent build their first app idea on make.fun.
"""
import os

TEXT = "Tell an AI agent on make.fun about the birthday-reminder app for your mum, say it in plain words, see it built before your tea cools, and if anything is wrong, fix it in one more sentence; your idea stays yours, and trying costs nothing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
