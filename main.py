import sys
import os
import pandas as pd
import numpy as np
import packages.wanbian_help.help as wHelp
import packages.wanbian_html.html_testing as wHtmlTesting
import packages.wanbian_word.word_testing as wWordTesting


class WanBian:
    def __init__(self, projectName, projectType):
        self.projectName = projectName
        self.CreateFile()
        # default is false when file is not exist.
        self.fileExistenceStatus = False

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

    #
    def BuildProject(self,args):
        self.ReadCsv()
        # this method return corresponding arguments that according to the outputType.

    def ReadCsv(self, projectType):
        if self.fileExistenceStatus:
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
        # instantiate the WanBian class.
        WB = WanBian(projectName, projectType)
        swicth(sys.argv[1]){
            case 'new' and len(sys.argv) == 4:
            # pass two arguments to corresponding variables.
                projectName = str(sys.argv[2])
                projectType = str(sys.argv[3])
                WB.
                break
            case 'build' and len(sys.argv) == 3:
                projectName = str(sys.argv[2])
                WB.
                break
            case 'help' and len(sys.argv) == 1:
                wHelp.Help()
                break
            case 'helpProjectType' and len(sys.argv) == 2:
                wHelp.HelpProjectType()
            default:
                wHelp.HelpNothingInput()
                break
        }
        # wHtmlTesting.Create(projectName, dataQuestion, dataAnswer)
        # wWordTesting.Create(projectName, dataQuestion, dataAnswer)
        print(dataQuestion, dataAnswer)
    else:
        if sys.argv[1] is None and sys.argv[2] is None:
            wHelp.HelpNothingInput()
        else:
            pass


if __name__ == "__main__":
    main()
