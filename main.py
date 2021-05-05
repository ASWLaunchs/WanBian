import sys
import os
import time
import shutil
import json
import numpy as np
import pandas as pd
import packages.wanbian_help.help as wHelp
import packages.wanbian_html.html_testing as wHtmlTesting
import packages.wanbian_word.word_testing as wWordTesting


class WanBian:

    def __init__(self):
        # default is false when file is not exist.
        self.__fileExistenceStatus = False
        self.projectName = ""
        self.projectType = ""

        # initialize testing variables.
        self.dataQuestion = self.dataAnswer = ''
        # initialize webpage variables.
        self.webpageContent = {}

    # CreateFile() be used in initialize related parameters about file.

    def CreateFile(self, projectName, projectType):
        self.projectName = projectName
        self.projectType = projectType
        # step 1: create a file path which be used storage csv file according to the project name.
        # step 2: create a csv file according to the project name.
        # step 3: create the _config.json file while modify it.
        # step 4: process all initialization variables.
        # the aim folder.
        aimFolder = os.path.exists("data/"+self.projectName)
        # the aim file.
        aimFile = os.path.exists(
            "data/"+self.projectName+"/_index"+".csv")

        # determine whether there is a aim folder and aim file.
        # there are two if-else parts :
        # (1) first part be used to check the aim folder exist or not .
        # (2) second part be used to check the aim file exist or not after the step done.
        if not aimFolder:
            os.makedirs('data/'+self.projectName)
            if not aimFile:
                # create the _index.csv file.
                fi = open("data/"+self.projectName + "/_index.csv", 'w')
                fi.close()

                # set the _config.json file.
                jsonText = {'config': []}
                jsonText['config'].append({'projectName': self.projectName,
                                           'projectType': self.projectType,
                                           'projectDate': time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())})
                jsonData = json.dumps(jsonText, indent=4,
                                      separators=(',', ': '))
                fi = open("data/"+self.projectName + '/_config.json', 'w')
                fi.write(jsonData)
                fi.close()
                print("the {} project was successfully created just now.".format(
                    self.projectName))
            else:
                print("the {} file path was existed.".format(self.projectName))
        else:
            print(
                "the {} file path was existed , please switch to another project name.".format(self.projectName))

    # BuildProject() is used to complie designated item.
    def BuildProject(self, projectName):
        self.projectName = projectName
        # checking whether the file exist.
        self.__fileExistenceStatus = self.__checking()
        # if checked file is existed.
        if self.__fileExistenceStatus:
            if self.projectName == "":
                print("please input the project name.")
            else:
                # get infomation of project configuration.
                fi = open("data/" + self.projectName + "/_config.json", "r")
                rs = json.load(fi)
                self.projectType = rs["config"][0]['projectType']
                fi.close()

                # choice the function() according to the projectType
                if self.projectType == '0_testing':
                    self.__readCsvTesting()
                elif self.projectType == '0_webpage':
                    pass
                elif self.projectType == '0_game':
                    pass
                elif self.projectType == '1_testing':
                    pass
                elif self.projectType == '1_webpage':
                    pass
                elif self.projectType == '1_game':
                    pass
                else:
                    pass
        else:
            print("the project csv file has been created , you can editor now in {}\n".format(
                "data/"+self.projectName+"/_index.csv"))

    # DeleteProject() is used to delete a existed project.

    def DeleteProject(self, projectName):
        self.projectName = projectName
        if self.projectName == "":
            print("please input the project name.")
        else:
            shutil.rmtree('data/'+self.projectName)
            print("the {} was successfully deleted.".format("self.projectName"))

    # testing
    def __readCsvTesting(self):
        try:
            # data be used to storage Question col data which in csv.
            data = pd.read_csv("data/"+self.projectName+"/_index.csv", usecols=[0, 1], converters={
                "Question": str, "Answer": str}, encoding='utf-8')
            self.dataQuestion = np.array(data['Question'].values.tolist())
            self.dataAnswer = np.array(data['Answer'].values.tolist())
            print("result was ready.")
            print(self.dataQuestion, self.dataAnswer)
        except ValueError:
            self.dataQuestion = self.dataAnswer = "it's seem happened some crash"
            print("csv has been created , but it is nothing in itself.")

    # __checking is used to check the file existence status.
    # this method return Boolean value.

    def __checking(self):
        # the aim folder.
        aimFolder = os.path.exists("data/"+self.projectName)
        # the aim file.
        aimFile = os.path.exists(
            "data/"+self.projectName+"/_index"+".csv")
        # the aim configuration file.
        aimConfig = os.path.exists(
            "data/" + self.projectName + "/_config.json")
        if aimFolder and aimFile and aimConfig:
            return True
        else:
            return False


def main():
    # Determine whether the corresponding parameters are passed in that by the sys.argv length when starting the program.
    WHelp = wHelp.Help()
    # instantiate the WanBian class.
    WB = WanBian()
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'new' and len(sys.argv) == 4:
            projectName = str(sys.argv[2])
            projectType = str(sys.argv[3])
            WB.CreateFile(projectName, projectType)
        elif sys.argv[1] == 'build' and len(sys.argv) == 3:
            projectName = str(sys.argv[2])
            WB.BuildProject(projectName)
        elif sys.argv[1] == 'delete' and len(sys.argv) == 3:
            projectName = str(sys.argv[2])
            WB.DeleteProject(projectName)
        elif sys.argv[1] == 'help' and len(sys.argv) == 2:
            WHelp.Help()
        elif sys.argv[1] == 'helpProjectType' and len(sys.argv) == 2:
            WHelp.HelpProjectType()
        else:
            WHelp.HelpNothingInput()
    else:
        WHelp.HelpNothingInput()


if __name__ == "__main__":
    main()
