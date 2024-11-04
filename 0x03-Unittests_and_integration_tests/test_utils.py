#!/usr/bin/env python3
"""test_utils module"""
import unittest
from unittest.mock import patch, Mock
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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test access_nested_map raises KeyError for invalid paths"""
        with self.assertRaises(KeyError) as cm:
            utils.access_nested_map(nested_map, path)
            self.assertEqual(str(cm.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict[str, Any]) -> None:
        """Test get_json with various inputs"""
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = payload
            mock_get.return_value = mock_response
            result = utils.get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator"""

    def test_memoize(self) -> None:
        """Test memoize decorator"""

        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock_:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_.assert_called_once()
