import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# тест для метода capitalize

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])

def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])

def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# тест для метода trim

@pytest.mark.parametrize("input_str, expected", [
    (" Skypro", "Skypro"),
    (" Hello world", "Hello world"),
    (" Python", "Python"),
])

def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    (" .", "."),
    ("   ", ""),
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# тест для метода contains

@pytest.mark.parametrize("string, symbol", [
    (" Skypro", "S",),
    (" Hello", "e",),
    (" Python", "y",),
])

def test_contains_positive(string, symbol) -> bool:
    assert string_utils.contains(string, symbol) == True

@pytest.mark.parametrize("string, symbol", [
    (" Skypro", "U",),
    (" Hello", "s",),
    (" Python", "a",),
])

def test_contains_positive(string, symbol) -> bool:
    assert string_utils.contains(string, symbol) == False
res = False

# для метода delete_symbol

@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "S", "kypro"),
    ("Hello", "e", "Hllo"),
    ("Python", "y", "Pthon"),
])

def test_delete_symbol_positive(string, symbol, expected) :
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "", "Skypro"),
    ("Hello", "P", "Hello"),
])

def test_delete_symbol_negative(string, symbol, expected) :
    assert string_utils.delete_symbol(string, symbol) == expected
