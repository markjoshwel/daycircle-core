"""
daycircle.cli: command line entry and interface for daycircle
-------------------------------------------------------------
by mark <mark@joshwel.co>

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

from argparse import ArgumentParser
from pathlib import Path
from sys import stderr

from .parser import DaycircleFile, parse
from .utils import Result


def handle_args() -> list[Path]:
    parser = ArgumentParser(
        description="beautifully chart your average day over a period of time"
    )
    parser.add_argument("targets", nargs="*", help="the target file(s) to read from")
    return [Path(target) for target in parser.parse_args().targets]


def main() -> None:
    """command-line entry point for daycircle"""
    behaviour = handle_args()

    data: list[DaycircleFile] = []

    for target in behaviour:
        if not target.exists():
            print(f"warn: '{target}' does not exist, skipping", file=stderr)
            continue

        if not target.is_file():
            print(f"warn: '{target}' is not a file, skipping", file=stderr)
            continue

        target_data: Result = parse(
            target.read_text(encoding="utf-8"), filename=target.name
        )
        if not target_data:
            print("warn:", target_data.cry(string=True), file=stderr)
        else:
            data.append(target_data.get())
