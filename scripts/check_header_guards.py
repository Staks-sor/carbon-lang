#!/usr/bin/env python3

"""Checks for missing or incorrect header guards."""

__copyright__ = """
Part of the Carbon Language project, under the Apache License v2.0 with LLVM
Exceptions. See /LICENSE for license information.
SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
"""

from pathlib import Path
import re
import sys
from typing import Iterable, List, NamedTuple, Optional


class Guard:
    def __init__(self, line, prefix, content):
        self.line = line
        self.prefix = prefix
        self.content = content


def get_old_guard(lines, guard_prefix):
    for i, line in enumerate(lines):
        if line.startswith(guard_prefix):
            prefix, content = line.split(" ", 1)
            return Guard(i, prefix, content.strip())

    return None


def change_guard(filepath, new_guard, guard_prefix="#"):
    path = Path(filepath)

    lines = path.read_text().splitlines()

    old_guard = get_old_guard(lines, guard_prefix)

    if old_guard:
        line = lines[old_guard.line].rstrip("\n")
        lines[old_guard.line] = f"{guard_prefix} {new_guard}\n"

    path.write_text("\n".join(lines))


filepath = "example.txt"
new_guard = "new_guard"




if __name__ == "__main__":
    change_guard(filepath, new_guard)
