import yaml
import pytest

from syllabipy.sonoripy import SonoriPy


cases = yaml.safe_load(open("cases.yaml"))


@pytest.mark.parametrize("name,data", cases.items())
def test_case(name, data):
    expected = data["output"]
    actual = SonoriPy(data["input"])
    assert expected == actual
