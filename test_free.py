#!/usr/bin/env python3
"""
Tests for the free.py memory information utility.
"""

import unittest
import sys
import os
import io
from contextlib import redirect_stdout

# Add the current directory to the path to import free
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import free


class TestFreeUtility(unittest.TestCase):
    """Test cases for the free memory utility."""
    
    def test_get_memory_info_returns_dict(self):
        """Test that get_memory_info returns a dictionary."""
        meminfo = free.get_memory_info()
        self.assertIsInstance(meminfo, dict)
    
    def test_get_memory_info_has_required_keys(self):
        """Test that get_memory_info returns required memory keys."""
        meminfo = free.get_memory_info()
        required_keys = ['MemTotal', 'MemFree']
        for key in required_keys:
            self.assertIn(key, meminfo)
    
    def test_memory_values_are_positive(self):
        """Test that memory values are non-negative."""
        meminfo = free.get_memory_info()
        for key, value in meminfo.items():
            self.assertGreaterEqual(value, 0, f"{key} should be non-negative")
    
    def test_format_bytes(self):
        """Test the format_bytes function."""
        result = free.format_bytes(1024)
        self.assertIsInstance(result, str)
        self.assertIn('1024', result)
    
    def test_display_memory_info_no_error(self):
        """Test that display_memory_info runs without errors."""
        meminfo = free.get_memory_info()
        try:
            # Redirect stdout to suppress output during test
            f = io.StringIO()
            with redirect_stdout(f):
                free.display_memory_info(meminfo)
            
            output = f.getvalue()
            # Check that output contains expected headers
            self.assertIn('total', output)
            self.assertIn('used', output)
            self.assertIn('free', output)
            self.assertIn('Mem:', output)
            self.assertIn('Swap:', output)
        except Exception as e:
            self.fail(f"display_memory_info raised an exception: {e}")
    
    def test_main_returns_zero(self):
        """Test that main function returns 0 (success)."""
        f = io.StringIO()
        with redirect_stdout(f):
            result = free.main()
        
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
