#!/usr/bin/env python

"""Tests for `elgamalfl` package."""


import unittest

from elgamalfl import elgamalfl


class TestElgamalfl(unittest.TestCase):
    """Tests for `elgamalfl` package."""

    def test_p(self):
        p = elgamalfl.generate_p()
        self.assertGreater(p, 0)

    def test_g(self):
        x = elgamalfl.generate_g()
        self.assertGreater(x, 0)

    def test_h(self):
        x = elgamalfl.calc_h()
        self.assertGreater(x, 0)

    def test_x(self):
        x = elgamalfl.generate_x()
        self.assertGreater(x, 0)


    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
