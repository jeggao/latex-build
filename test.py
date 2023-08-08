import unittest
from os import chdir
from time import perf_counter
import logging
import shutil

import imp

target = imp.load_source("build", "project_name/build")


class TestParse(unittest.TestCase):
    def test_toml(self):
        """
        Test toml read.
        """
        args, build_config = target.parse_arguments(toml_location="./build.toml")
        self.assertFalse(args.live)
        self.assertFalse(args.draft)
        self.assertFalse(args.spell)
        self.assertFalse(args.verbose)

        self.assertDictEqual(
            build_config,
            {
                "latex-build": {"version": "v2.0"},
                "latexmk": {
                    "LATEX": "pdflatex",
                    "TEX_NAME": "main.tex",
                    "AUX_DIR": "./tmp",
                    "OUT_DIR": "./",
                    "OUT_NAME": "main",
                },
            },
        )


class TestBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chdir("./project_name")

    def test_default(self):
        """
        Test normal build.
        """
        target.build(
            build_config={
                "latex-build": {"version": "v2.0"},
                "latexmk": {
                    "LATEX": "pdflatex",
                    "TEX_NAME": "main.tex",
                    "AUX_DIR": "./tmp",
                    "OUT_DIR": "./",
                    "OUT_NAME": "main",
                },
            },
            live=False,
            draft=False,
            spell=False,
            verbose=True,
        )
        shutil.rmtree("tmp/", ignore_errors=True)

    def test_draft(self):
        """
        Test normal build.
        """
        target.build(
            build_config={
                "latex-build": {"version": "v2.0"},
                "latexmk": {
                    "LATEX": "pdflatex",
                    "TEX_NAME": "main.tex",
                    "AUX_DIR": "./tmp",
                    "OUT_DIR": "./",
                    "OUT_NAME": "main",
                },
            },
            live=False,
            draft=True,
            spell=False,
            verbose=True,
        )
        shutil.rmtree("tmp/", ignore_errors=True)


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    unittest.main()
