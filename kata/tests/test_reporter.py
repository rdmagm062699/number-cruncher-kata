import pytest
import unittest
from unittest.mock import patch
from src.reporter import crunch_report

# Hint: patch the name as it is imported into reporter, not where it is defined.
#   @patch("src.reporter.crunch_the_numbers")


class TestCrunchReport(unittest.TestCase):

    def test_placeholder(self):
        self.fail("Replace this with your first real test")


if __name__ == "__main__":
    unittest.main()
