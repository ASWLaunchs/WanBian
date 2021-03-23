import os
import pandas as pd
import numpy as np
import wanbian_html.html_testing as wHtml
import wanbian_word.word_testing as wWord


class WanBian:
    def __init__(self, projectName):
        self.projectName = projectName

    # CreateFile() be used in initialize related parameters about file.
    def CreateFile(self):
        # step 1: create a file path which be used storage csv file according to the project name.
        # step 2: create a csv file according to the project name.
        # step 3: process all initialization variables.
        folder = os.path.exists("resource/"+self.projectName)
        if not folder:
            os.makedirs(self.projectName)
            print("the {} file path was created.".format(folder))
        else:
            print(
                "the {} file path was existed , please change another project name.".format(folder))

    # this method return two arguments what is dataQuestion and dataAnswer.
    def ReadCsv(self):
        # data be used to storage Question col data which in csv.
        data = pd.read_csv("resource/"+self.projectName+"/"+self.projectName+".csv", usecols=[0, 1], converters={
            "Question": str, "Answer": str}, encoding='GB18030')
        dataQuestion = np.array(data['Question'].values.tolist())
        dataAnswer = np.array(data['Answer'].values.tolist())
        return dataQuestion, dataAnswer


def main():
    projectName = input("please input your project name:")
    wB = WanBian(projectName)
    wB.CreateFile()
    dataQuestion, dataAnswer = wB.ReadCsv()
    wHtml.CreateHTML(dataQuestion, dataAnswer)
    wWord.CreateWord(dataQuestion, dataAnswer)


if __name__ == "__main__":
    main()
