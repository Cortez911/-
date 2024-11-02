import pytest
from string_utils import StringUtils

class TestStringUtils:
  def setup_method(self):
    self.string_utils = StringUtils()

  # capitilize
  def test_capitilize_positive_1(self):
    assert self.string_utils.capitilize("skypro") == "Skypro"

  def test_capitilize_positive_2(self):
    assert self.string_utils.capitilize("hello world") == "Hello world"

  def test_capitilize_negative_1(self):
    assert self.string_utils.capitilize("") == ""

  def test_capitilize_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.capitilize(None)

  # trim
  def test_trim_positive_1(self):
    assert self.string_utils.trim("  skypro") == "skypro"

  def test_trim_positive_2(self):
    assert self.string_utils.trim(" hello world") == "hello world"

  def test_trim_negative_1(self):
    assert self.string_utils.trim("") == ""

  def test_trim_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.trim(None)

  # to_list
  def test_to_list_positive_1(self):
    assert self.string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]

  def test_to_list_positive_2(self):
    assert self.string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]

  def test_to_list_negative_1(self):
    assert self.string_utils.to_list("") == []

  def test_to_list_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.to_list(None)

  # contains
  def test_contains_positive_1(self):
    assert self.string_utils.contains("SkyPro", "S") == True

  def test_contains_positive_2(self):
    assert self.string_utils.contains("hello world", "o") == True

  def test_contains_negative_1(self):
    assert self.string_utils.contains("", "S") == False

  def test_contains_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.contains(None, "S")

  # delete_symbol
  def test_delete_symbol_positive_1(self):
    assert self.string_utils.delete_symbol("SkyPro", "k") == "SyPro"

  def test_delete_symbol_positive_2(self):
    assert self.string_utils.delete_symbol("hello world", "o") == "hell wrld"

  def test_delete_symbol_negative_1(self):
    assert self.string_utils.delete_symbol("", "k") == ""

  def test_delete_symbol_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.delete_symbol(None, "S")

  # starts_with
  def test_starts_with_positive_1(self):
    assert self.string_utils.starts_with("SkyPro", "S") == True

  def test_starts_with_positive_2(self):
    assert self.string_utils.starts_with("hello world", "h") == True

  def test_starts_with_negative_1(self):
    assert self.string_utils.starts_with("", "S") == False

  def test_starts_with_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.starts_with(None, "S")

  # end_with
  def test_end_with_positive_1(self):
    assert self.string_utils.end_with("SkyPro", "o") == True

  def test_end_with_positive_2(self):
    assert self.string_utils.end_with("hello world", "d") == True

  def test_end_with_negative_1(self):
    assert self.string_utils.end_with("", "o") == False

  def test_end_with_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.end_with(None, "o")

  # is_empty
  def test_is_empty_positive_1(self):
    assert self.string_utils.is_empty("") == True

  def test_is_empty_positive_2(self):
    assert self.string_utils.is_empty(" ") == True

  def test_is_empty_negative_1(self):
    assert self.string_utils.is_empty("SkyPro") == False

  def test_is_empty_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.is_empty(None)

  # list_to_string
  def test_list_to_string_positive_1(self):
    assert self.string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"

  def test_list_to_string_positive_2(self):
    assert self.string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"

  def test_list_to_string_negative_1(self):
    assert self.string_utils.list_to_string([]) == ""

  def test_list_to_string_negative_2(self):
    with pytest.raises(TypeError):
      self.string_utils.list_to_string(None)
