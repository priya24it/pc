import json
import datetime
from testrail.client import TestRail
from testrail.api import API
from testrail.case import Case


class TestRail1:
    def test_getmilestones(self):
        testrail_file = 'testrail.env'
        testrail_url = "https://priyanewpage.testrail.io/index.php/login/auth"
        client = TestRail(testrail_url)
        email = "priya.bharathi@newpage.io"
        key = "uW9aLHW1v8RlJqZhZbmR-k2DBXoq3MS836eZXUcAd"
        print(client.projects())





