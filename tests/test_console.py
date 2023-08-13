#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
import console
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        with patch('builtins.input', side_effect=['quit']):
            console.HBNBCommand().cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "(hbnb) Goodbye!\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        with patch('builtins.input', side_effect=['help', 'quit']):
            console.HBNBCommand().cmdloop()
        expected_output = """Documented commands (type help <topic>):
========================================
EOF  help  quit
"""
        self.assertEqual(mock_stdout.getvalue(), f"(hbnb) {expected_output}(hbnb) Goodbye!\n")

    # Add more test cases for other commands

if __name__ == '__main__':
    unittest.main()
