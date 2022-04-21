import pytest


@pytest.fixture(scope='function', autouse=True)
def resource_setup(request):
    print('setup function')

    def resource_teardown():
        print('teardown function')
    request.addfinalizer(resource_teardown)


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