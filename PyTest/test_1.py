import pytest


def setup():
    print("basic setup into module")

def teardown():
    print("basic teardown into module")

def setup_module():
    print("module setup")

def teardown_module():
    print("module teardown")

def setup_function(f):
    print(f'function {f} setup')

def teardown_function(f):
    print(f'function {f} teardown')


def test_add_2_3_should_be_5():
    # arrange
    a = 2
    b = 3
    expected = 5
    print(f'test {a}+{b}={expected}')

    # act
    actual = a + b

    # assert
    assert expected == actual


def test_mul_2_2_should_be_4():
    # arrange
    a = 2
    b = 2
    expected = 4
    print(f'test {a}*{b}={expected}')

    # act
    actual = a * b

    # assert
    assert expected == actual