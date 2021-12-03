import pytest
def test_success():
    """this test syccess"""
    assert True
def test_failure():
    """this test failure"""
    assert False
def test_skip():
    """"this test is skiped """
    pytest.skip('for a reason!')
def test_broken():
    raise Exception('oop')

