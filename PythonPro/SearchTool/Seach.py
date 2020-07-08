import Common
import database
import psycopg2
import os


ce = Common.common

class Search(Common.common):

    ce = Common.common

    def preprocess(self,SourceFile):
        log = Common.common.getlogger(self)
        log.info("started loading the Excel file")
        excel_data = database.load_excel(SourceFile)
        log.info("Total number of rows and columns in Excel source" + str(excel_data.shape))
        csvfile = database.convert_toCSV(excel_data)
        log.info("Total number of rows and columns in CSV Source" + str(excel_data.shape))

    def load_data(self,CSV_Filename):
        database.load_intoDBTable(CSV_Filename)

    def create_index(self):
        database.create_index()

    def search_results(self):
        database.search_results()

    def execution_time(self):
        database.execution_time()

SourceFile = r"InputData.xlsx"
CSVFile = r"C:\PythonPro\untitled\InputData.csv"

os.remove(r"logfile.log")
s = Search()
s.preprocess(SourceFile)
s.load_data(CSVFile)
#s.create_index()
#s.search_results()
#s.execution_time()
