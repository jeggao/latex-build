import unittest
from os import chdir
from time import perf_counter
import logging
import shutil

import imp

target = imp.load_source("build", "project_name/build")


class TestParse(unittest.TestCase):
    def test_toml(self):
        @classmethod
        def setUpClass(cls):
            chdir("./project_name")

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
                    "latex-build": {"version": target.script_version},
                    "latexmk": {
                        "LATEX": "pdflatex",
                        "TEX_NAME": "main.tex",
                        "AUX_DIR": "./tmp",
                        "OUT_DIR": "./",
                        "OUT_NAME": "main",
                    },
                },
            )


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    unittest.main()
