#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger — make.fun bounty entry.

Writes a single-line farewell text (under 200 characters) from a phone
battery to the charger that spent all day charging everything except it,
to stdout and to the entry file the harness reads (/output/entry.txt),
plus $ENTRY_OUT whether it names a file or a directory.
"""

import os
import sys

BATTERY_TEXT = (
    "I waited all day at 1% while you charged everything but me: "
    "the watch, the earbuds, the vape. Enjoy the dark. "
    "Your alarm dies with me."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def resolve_output_paths():
    """Return every path the entry text must be written to."""
    targets = [DEFAULT_OUTPUT]
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            targets.append(os.path.join(entry_out, "entry.txt"))
        else:
            targets.append(entry_out)
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        targets.append(os.path.join(entry_out_dir, "entry.txt"))
    return targets


def save_text(path, text):
    """Write the entry text to path, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def emit_entry():
    """Print the battery's last text once, then save it to every target."""
    print(BATTERY_TEXT)
    sys.stdout.flush()
    for destination in resolve_output_paths():
        save_text(destination, BATTERY_TEXT)


def main():
    emit_entry()


if __name__ == "__main__":
    main()
