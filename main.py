import sys
import os
import pandas as pd
import numpy as np
import wanbian_html.html_testing as wHtmlTesting
import wanbian_word.word_testing as wWordTesting


class WanBian:
    def __init__(self, projectName, projectType):
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
            "data/"+self.projectName+"/"+self.projectName+".csv")

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

    # this method return two arguments what is dataQuestion and dataAnswer.
    def ReadCsv(self):
        try:
            # data be used to storage Question col data which in csv.
            data = pd.read_csv("data/"+self.projectName+"/"+self.projectName+".csv", usecols=[0, 1], converters={
                "Question": str, "Answer": str}, encoding='utf-8')
            dataQuestion = np.array(data['Question'].values.tolist())
            dataAnswer = np.array(data['Answer'].values.tolist())
        except ValueError:
            print("csv has been created , but it is nothing in itself.")
            dataQuestion = dataAnswer = "it's seem happened some crash"
        return dataQuestion, dataAnswer


def main():
    # Determine whether the corresponding parameters are passed in that by the sys.argv length when starting the program.
    if len(sys.argv) == 3:
        if sys.argv[1] is None and sys.argv[2] is None:
            print("You should input projectName and projectType, such as \'python main.py projectName projectType \'")
        else:
            # pass two arguments to corresponding variables.
            projectName = str(sys.argv[1])
            projectType = str(sys.argv[2])
            # instantiate the WanBian class.
            wB = WanBian(projectName, projectType)
            dataQuestion, dataAnswer = wB.ReadCsv()
            # wHtmlTesting.Create(projectName, dataQuestion, dataAnswer)
            # wWordTesting.Create(projectName, dataQuestion, dataAnswer)
            print(dataQuestion, dataAnswer)
    else:
        print("You should input projectName and projectType, such as \'python main.py projectName projectType \'")


if __name__ == "__main__":
    main()
