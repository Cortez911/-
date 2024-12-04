import pytest
pytest_plugins = ['pytester']

def pytest_configure(config):
    config.addinivalue_line("markers", "suppress_movedin20_warning")
