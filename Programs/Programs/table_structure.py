import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict
import settings

databasename = settings.INDEX_NAME
tablename = settings.TYPE_NAME
tablestructure = {"settings": {"mappings": {"properties": {"RPD_Link":{"type": "text"}, "RPD#":{"type": "text"},
                  "Updated_Date":{"type": "text"}, "Created_Date":{"type": "text"}, "Type":{"type": "text"}, "Author":{"type": "text"},
                  "Title":{"type": "text"}, "Category":{"type": "text"}, "Severity":{"type": "text"}, "Assignee":{"type": "text"},
                  "Status":{"type": "text"}, "Database":{"type": "text"}, "Group":{"type": "text"}, "Template":{"type": "text"},
                  "Query_Type":{"type": "text"}, "Country":{"type": "text"}, "Profile":{"type": "text"}, "Industry_Type":{"type": "text"},
                  "Question_Type":{"type": "text"}, "Report_Type":{"type": "text"}, "Time_Series":{"type": "text"}, "Year":{"type": "text"},
                 "Company_Priority":{"type": "text"}, "SDB_STD_Code":{"type": "text"}, "Field_Name":{"type": "text"},
                "Specific_Account_Name":{"type": "text"}, "Company_Name":{"type": "text"}, "PPI":{"type": "text"},
                "Memo_definition":{"type": "text"}, "#Comments":{"type": "text"}, }}}}


tabledata = ""
header = settings.header
#working structure.

print("creating Index and table ...")
query = settings.Endpoint_URL+databasename+"/"+tablename
response = requests.post(query,data= json.dumps(tablestructure),headers=header)
print(response.text)
print("database and table has created successfully....")