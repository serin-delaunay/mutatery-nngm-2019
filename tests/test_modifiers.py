#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Unit tests for pytracery
"""
from __future__ import print_function
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from tracery import modifiers


class TestModifiers(unittest.TestCase):

    def test_replace(self):
        # Arrange
        text = "a big ship"

        # Act
        output = modifiers.replace(text, "ship", "shop")

        # Assert
        self.assertEqual(output, "a big shop")

    def test_capitalize_all(self):
        # Arrange
        text = "abc def"

        # Act
        output = modifiers.capitalizeAll(text)

        # Assert
        self.assertEqual(output, "Abc Def")

    def test_capitalize_(self):
        # Arrange
        text = "abc def"

        # Act
        output = modifiers.capitalize_(text)

        # Assert
        self.assertEqual(output, "Abc def")

    def test_a_consonant(self):
        # Arrange
        text = "house"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "a house")

    def test_a_u_something_i(self):
        # Arrange
        text = "unicorn"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "a unicorn")

    def test_a_u_not_i(self):
        # Arrange
        text = "underdog"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "an underdog")

    def test_a_vowel(self):
        # Arrange
        text = "elephant"

        # Act
        output = modifiers.a(text)

        # Assert
        self.assertEqual(output, "an elephant")

    def test_first_s(self):
        # Arrange
        text = "elephant in a phonebox"

        # Act
        output = modifiers.firstS(text)

        # Assert
        self.assertEqual(output, "elephants in a phonebox")

    def test_s_ends_in_x(self):
        # Arrange
        text = "box"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "boxes")

    def test_s_ends_in_non_s(self):
        # Arrange
        text = "goat"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "goats")

    def test_s_ends_in_vowel_y(self):
        # Arrange
        text = "monkey"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "monkeys")

    def test_s_ends_in_y_but_not_vowel_y(self):
        # Arrange
        text = "telly"

        # Act
        output = modifiers.s(text)

        # Assert
        self.assertEqual(output, "tellies")

    def test_ed_ends_in_e(self):
        # Arrange
        text = "glide"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "glided")

    def test_ed_ends_in_y_but_not_vowel_y(self):
        # Arrange
        text = "shimmy"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "shimmied")

    def test_ed_ends_in_non_e_and_non_y(self):
        # Arrange
        text = "jump"

        # Act
        output = modifiers.ed(text)

        # Assert
        self.assertEqual(output, "jumped")

    def test_uppercase(self):
        # Arrange
        text = "jump up"

        # Act
        output = modifiers.uppercase(text)

        # Assert
        self.assertEqual(output, "JUMP UP")

    def test_lowercase(self):
        # Arrange
        text = "GET DOWN"

        # Act
        output = modifiers.lowercase(text)

        # Assert
        self.assertEqual(output, "get down")


if __name__ == "__main__":
    unittest.main()

# End of file
