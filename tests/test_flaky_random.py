import random
import pytest



def test_flaky_random() -> None:
    pytest.skip("skip flaky test")
    assert random.random() > 0.2
