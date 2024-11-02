#!/usr/bin/env python3
"""test_utils module"""
from unittest import TestCase
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap (TestCase):
    """TestAccessNestedMap class"""
    @parameterized.expand
    def test_access_nested_map():
        """test access_nested_map method"""

    @parameterized.expand
    def test_access_nested_map_exception():
        """test_access_nested_map_exception mothod"""
        assertRaises KeyError


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    def test_get_json():
        """test get_json method"""
        assert get_json == test_payload


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""
    def test_memoize():
        """test memoize method"""
