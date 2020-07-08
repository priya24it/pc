import json
import datetime
from testrail.client import TestRail
from testrail.api import API
from testrail.case import Case
from testrail_integration.testrail_utils import  initialize_testrail_client
from testrail_integration.testrail_utils import  get_project_suite

testrail_file = 'testrail.env'
testrail_url = "https://priyanewpage.testrail.io/index.php/login/auth"
client = TestRail(testrail_url)
email = "priya.bharathi@newpage.io"
key = "uW9aLHW1v8RlJqZhZbmR-k2DBXoq3MS836eZXUcAd"
tr = initialize_testrail_client(1)
get_project_suite(tr,1,'MDM','abc')

#print(client.active_users())
#print(client.projects())
#print(client)
#print(client.milestones())
#print(client.tests())
#print(client.projects())
#print(client.statuses())
