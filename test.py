import unittest
import os
from time import perf_counter

from project_name import build as target


class TestBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir("./project_name")

    def test_default(self):
        """
        Test normal build.
        """
        target.build(live=False, draft=False, verbose=True)
        target.run(["rm", "-r", "tmp/"])

    def test_draft(self):
        """
        Test normal build.
        """
        target.build(live=False, draft=True, verbose=True)
        target.run(["rm", "-r", "tmp/"])


if __name__ == "__main__":
    unittest.main()
