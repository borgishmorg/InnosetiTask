import pytest


def pytest_addoption(parser):
    parser.addoption("--ip", action="store", default="localhost")


@pytest.fixture
def port(request):
    return request.config.getoption("--ip")
