import pytest
import oc

def test_login():
    expected = 'success'
    assert oc.login() == expected


if __name__ == '__main__':
    pytest.main()