#!/usr/bin/python
from subprocess import run
import argparse

TEX_NAME = "main.tex"
AUX_DIR = "./tmp"
OUT_DIR = "./"
OUT_NAME = "main"

LATEX = "pdflatex"


def build(live=False, draft=False, verbose=False):
    command = ["latexmk"]
    if live:
        command.append("-pvc")

    if verbose:
        command.append("-verbose")
    else:
        command.append("-silent")

    command += [
        "-" + LATEX,
        "--output-directory=" + OUT_DIR,
        "-aux-directory=" + AUX_DIR,
        "-halt-on-error",
        "-interaction=nonstopmode",
        TEX_NAME,
    ]

    if verbose:
        run(["ls", "-l"])
        print(command)

    run(command)


def main():
    parser = argparse.ArgumentParser("build.py")
    parser.add_argument(
        "-l", "--live", dest="live", action="store_true", help="specify build type"
    )
    parser.add_argument(
        "-d", "--draft", dest="draft", action="store_true", help="not include images"
    )
    parser.add_argument(
        "-s", "--spell-check", dest="spell", action="store_true", help="enable aspell"
    )
    parser.add_argument(
        "-v", "--verbose", dest="verbose", action="store_true", help="make verbose"
    )
    args = parser.parse_args()

    live = args.live
    draft = args.draft
    verbose = args.verbose
    spell = args.spell

    if verbose:
        print(args)

    if spell:
        run(["aspell", "--mode=tex", "check", TEX_NAME])

    build(live, draft, verbose)


if __name__ == "__main__":
    main()
