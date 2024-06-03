from contextlib import nullcontext as does_not_raise
import pytest
from fuel import convert, gauge


@pytest.mark.parametrize("input, expected, expectation",
                         [("3/4", 75, does_not_raise()),
                          ("1/3", 33, does_not_raise()),
                          ("2/3", 67, does_not_raise()),
                          ("0/100", 0, does_not_raise()),
                          ("1/100", 1, does_not_raise()),
                          ("100/100", 100, does_not_raise()),
                          ("three/four", None, pytest.raises(ValueError)),
                          ("10/3", None, pytest.raises(ValueError)),
                          ("1.5/4", None, pytest.raises(ValueError)),
                          ("3/5.5", None, pytest.raises(ValueError)),
                          ("5-10", None, pytest.raises(ValueError)),
                          ("0/0", None, pytest.raises(ZeroDivisionError)),
                          ("99/100", 99, does_not_raise())
                          ])
def test_convert(input, expected, expectation):
    with expectation:
        assert convert(input) == expected


@pytest.mark.parametrize("input,expected",
                         [(75, "75%"),
                          (33, "33%"),
                          (67, "67%"),
                          (0, "E"),
                          (1, "E"),
                          (100, "F"),
                          (99, "F")
                          ])
def test_gauge(input, expected):
    assert gauge(input) == expected
