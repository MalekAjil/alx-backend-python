#!/usr/bin/env python3
"""test_utils module"""
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap (TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand
    def test_access_nested_map():
        """test access_nested_map method"""

    @parameterized.expand
    def test_access_nested_map_exception():
        """test_access_nested_map_exception mothod"""
        assertRaises KeyError
