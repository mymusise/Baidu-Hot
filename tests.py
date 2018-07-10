import unittest
from unittest import TestCase
from get import Clawer, Runner, Parser


class TestClawer(TestCase):

    def setUp(self):
        self.runner = Runner()
        self.clawer = Clawer()

    def test_runner(self):
        url = self.runner.base_url.format(42)
        doc = self.clawer.request(url)

        parser = Parser(doc)
        data = parser.parse()
        self.assertEqual(len(data), 51)


if __name__ == "__main__":
    unittest.main()