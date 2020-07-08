import pytest
import request
import requests

@pytest.mark.usefixtures("addidtion")
@pytest.mark.skip
class TestBrokenLinks:
    def test_broken(self):
        print("statred")