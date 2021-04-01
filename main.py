import sys
import os
import pandas as pd
import numpy as np
import packages.wanbian_help.help as wHelp
import packages.wanbian_html.html_testing as wHtmlTesting
import packages.wanbian_word.word_testing as wWordTesting


class WanBian:

    def __init__(self, projectName, projectType):
        # default is false when file is not exist.
        self.__fileExistenceStatus = False
        self.projectName = projectName
        self.CreateFile()

    # CreateFile() be used in initialize related parameters about file.
    def CreateFile(self):
        # step 1: create a file path which be used storage csv file according to the project name.
        # step 2: create a csv file according to the project name.
        # step 3: process all initialization variables.
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
            print("the {} file path was created just now.".format(aimFolder))
            if not aimFile:
                fi = open("data/"+self.projectName + "/_index.csv", 'w')
                fi.close()
                print("the {} file path was created just now.".format(aimFile))
            else:
                print("the {} file path was existed.".format(aimFile))
        else:
            print(
                "the {} file path was existed , please switch to another project name.".format(aimFolder))

    # BuildProject() is used to complie designated item.
    def BuildProject(self, projectName):
        if projectName == "":
            pass
        self.ReadCsv(projectName)
        # this method return corresponding arguments that according to the outputType.

    def ReadCsv(self, projectType):
        if self.__fileExistenceStatus:
            try:
                # data be used to storage Question col data which in csv.
                data = pd.read_csv("data/"+self.projectName+"/_index.csv", usecols=[0, 1], converters={
                    "Question": str, "Answer": str}, encoding='utf-8')
                dataQuestion = np.array(data['Question'].values.tolist())
                dataAnswer = np.array(data['Answer'].values.tolist())
            except ValueError:
                dataQuestion = dataAnswer = "it's seem happened some crash"
                print("csv has been created , but it is nothing in itself.")
        else:
            dataQuestion = dataAnswer = "it's nothing now , please editor it to make it appear to be filled with some content.\n"
            print("the project csv file has been created , you can editor now in {}\n".format(
                "data/"+self.projectName+"/_index.csv"))
        return dataQuestion, dataAnswer


def main():
    # Determine whether the corresponding parameters are passed in that by the sys.argv length when starting the program.
    if len(sys.argv) == 3:
        if sys.argv[1] == 'new' and len(sys.argv) == 4:
            projectName = str(sys.argv[2])
            projectType = str(sys.argv[3])
            # instantiate the WanBian class.
            WB = WanBian(projectName, projectType)
            WB.CreateFile()
        elif sys.argv[1] == 'build' and len(sys.argv) == 3:
            projectName = str(sys.argv[2])
            WB.BuildFile(projectName)
        elif sys.argv[1] == 'help' and len(sys.argv) == 1:
            wHelp.Help()
        elif sys.argv[1] == 'helpProjectType' and len(sys.argv) == 2:
            wHelp.HelpProjectType()
        else:
            wHelp.HelpNothingInput()
    else:
        if sys.argv[1] is None or sys.argv[2] is None:
            wHelp.HelpNothingInput()
        else:
            pass


if __name__ == "__main__":
    main()
