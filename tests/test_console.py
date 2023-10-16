#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test class for the console"""

    def create(self):
        """Create an instance of the HBNBCommand class."""
        return HBNBCommand()

    def test_quit(self):
        """Test the 'quit' method in the console."""
        console_instance = self.create()
        # Attempt to execute the 'quit' command and assert the return value
        self.assertTrue(console_instance.onecmd("quit"))

    def test_EOF(self):
        """Test the 'EOF' method in the console."""
        console_instance = self.create()
        # Attempt to execute the 'EOF' command and assert the return value
        self.assertTrue(console_instance.onecmd("EOF"))

