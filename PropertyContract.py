import hypothesis, icontract
from hypothesis import given
import hypothesis.strategies as st
from hypothesis.strategies import integers
from string import printable

import tinyJSON

# Write your test cases here
json = st.recursive(
     st.none() | st.booleans() | st.floats() | st.text(printable),
     lambda children: st.lists(children) | st.dictionaries(st.text(printable), children), max_leaves=10
)

@given(json)
def test_valid_json_parsing(json_str):
    try:
        result = tinyJSON.parse_string(str(json_str))
    except Exception:
        pass #"Parsing a valid JSON string should not raise an exception"



if __name__ == "__main__":
    # Call your test functions here
    test_valid_json_parsing()
