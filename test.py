import unittest
from os import chdir
from time import perf_counter
import logging
import shutil

import imp
target = imp.load_source('build', 'project_name/build')


class TestBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chdir("./project_name")

    def test_default(self):
        """
        Test normal build.
        """
        target.build(live=False, draft=False, verbose=True)
        shutil.rmtree("tmp/", ignore_errors=True)

    def test_draft(self):
        """
        Test normal build.
        """
        target.build(live=False, draft=True, verbose=True)
        shutil.rmtree("tmp/", ignore_errors=True)


if __name__ == "__main__":
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    unittest.main()
