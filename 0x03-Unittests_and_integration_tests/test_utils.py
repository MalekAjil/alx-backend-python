#!/usr/bin/env python3
"""test_utils module"""
import unittest
from parameterized import parameterized
import utils
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap (unittest.TestCase):
    """TestAccessNestedMap class"""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """Test access_nested_map with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
            self.assertEqual(str(cm.exception), str(path[-1]))

'''
class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    def test_get_json(self):
        """test get_json method"""
        assert get_json == test_payload


class TestMemoize(unittest.TestCase):
    """TestMemoize class"""
    def test_memoize(self):
        """test memoize method"""
'''
