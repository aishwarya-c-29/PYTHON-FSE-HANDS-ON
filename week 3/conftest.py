#conftest
import pytest

@pytest.fixture
def sample_numbers():
    return (20, 10)

@pytest.fixture
def zero():
    return 0
