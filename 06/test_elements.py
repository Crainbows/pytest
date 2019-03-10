from elements import Identify

import pytest

@pytest.mark.parametrize("element, expected", [('snow', 'water'), ('tin', 'solder'), ('something else', 'tungsten')])
def test_action_with_parametrization(element, expected):
    sc = Identify()
    sc.element = element
    sc.melt()
    assert sc.element == expected