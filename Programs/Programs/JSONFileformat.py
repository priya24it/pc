import requests
import json
import pandas as pd
import time
from xl2dict import XlToDict
import settings
import os
import pymssql



def convertinto_json():
    data = pd.read_excel(settings.source_file)
    df = pd.DataFrame(data)
    print(df.columns.tolist())

    df = df.rename(columns = {"RPD Link": "RPD_Link",
                            "RPD #":"RPD#",
                            "Updated Date": "Updated_Date",
                            "Created Date": "Created_Date",
                            "Query Type": "Query_Type",
                            "Industry Type": "Industry_Type",
                            "Question Type": "Question_Type",
                            "Report Type": "Report_Type",
                            "Time-Series": "Time_Series",
                            "Year ( 2018, 2017, 2016, etc.)": "Year",
                            "Company Priority": "Company_Priority",
                            "SDB/STD Code Number (No multiple items; if related to multiple items just choose the most critical) *Refer to DocEx for the Code number": "SDB_STD_Code",
                            "Field Name": "Field_Name",
                            "Specific Account Name": "Specific_Account_Name",
                            "Company Name": "Company_Name",
                            "PPI (Voyager and Supercore)": "PPI",
                            "Memo or definition used as reference": "Memo_definition",
                            "# Comments": "#Comments"
                            } )

    df['Updated_Date'] = df['Updated_Date'].dt.strftime("%m%d%y")
    print(df.columns.tolist())
    l1 = str(df.columns.tolist())
    print(l1)
    df.to_excel(settings.updated_sourcefile,index=False)
    df.to_json("rpd1.json",orient="records",lines=True)


    if os.path.isfile("rpd.json"):
        os.remove("rpd.json")

    print("currently following this procedure -- converting excel data into Json data")
    myxlobject= XlToDict()
    print(settings.source_file)
    #data = myxlobject.convert_sheet_to_dict(file_path=settings.source_file, sheet="Sheet1")
    data = myxlobject.convert_sheet_to_dict(file_path=settings.updated_sourcefile, sheet="Sheet1")
    print(len(data))
    for i in range(0,len(data)):
        tabledata = json.dumps(data[i], separators=(',', ':'))
        with open("rpd.json", "a") as outfile:
            outfile.write(tabledata+"\n")

convertinto_json()


