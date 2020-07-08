from datetime import datetime
import pytest
from testrail_api import TestRailAPI
from utils import get_testrail_params

@pytest.mark.usefixtures("setup")
class Testrail():
    config = get_testrail_params()
    def test_addProject(self):
        #self.driver.projects.add_project("Canvas-Sample")  #project id:4
        print("Projects added successfully...")

    def test_getlistofProjects(self):
        listofProjects = self.driver.projects.get_projects()
        print(listofProjects)


    def test_addmilestones(self):
        # self.driver.milestones.add_milestone(4,"Sample-MileStones") #project id:44
        print("add milestones..")

    def test_getmilestones(self):
        milestones = self.driver.milestones.get_milestones(4) #milestone ID:13 , Project_ID:4
        print(milestones)

    def test_addSuit(self):
        # self.driver.suites.add_suite(4,"SampleCanvasSuit")
        print("adding suites ")

    def test_getsuits(self):
        print(self.driver.suites.get_suites(4)) #projectID:4 , SuitID:4

    def test_addsections(self):
        print("")
        #self.driver.sections.add_section(project_id=4,suite_id=4,name="CanvasSampleSection")


    def test_getsections(self):
        print("")
        print(self.driver.sections.get_sections(project_id=4,suite_id=4)) #section 6


    def test_addtestcases(self):
        print("")
        # self.driver.cases.add_case(section_id=6,milestone_id=13,title="First Testcase in Sample Canvas")

    def test_gettestcases(self):
        print("")
        print(self.driver.cases.get_cases(project_id=4,suite_id=4)) #Testcase ID:11

    def test_addresults(self):
        # my_test_run = api.runs.add_run(project_id=4, suite_id=4, name="Second Testcase", include_all=True, milestone_id=13)
        # print(my_test_run)
        result = self.driver.results.add_result_for_case(run_id=20, case_id=11, status_id=1, comment="Pass", version="1")
















