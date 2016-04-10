import pytest
from json_parsing import JsonParser

def test_parse_json_string():
    parser = JsonParser()
    parser.parse_json_string('{"name": "john doe"}')

def test_parse_json_string_fail():
    parser = JsonParser()
    parser.parse_json_string('{"name": john doe"}')


if __name__ == "__main__":
    pytest.main()
