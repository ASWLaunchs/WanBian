import os
import pandas as pd
import numpy as np
import wanbian_html.html_testing as wHtml
import wanbian_word.word_testing as wWord


# CreateFile() be used in initialize related parameters about file.
def CreateFile(ProjectName):
    # step 1: create a file path which be used storage csv file according to the project name.
    # step 2: create a csv file according to the project name.
    # step 3: process all initialization variables.
    folder = os.path.exists("resource/"+ProjectName)
    if not folder:
        os.makedirs(ProjectName)
        print("the {} file path was created.".format(folder))
    else:
        print("the {} file path was existed , please change another project name.")

def ReadCsv(filePath):
    # data be used to storage Question col data which in csv.
    data = pd.read_csv("filePath", usecols=[0, 1], converters={
        "Question": str, "Answer": str}, encoding='GB18030')
    dataQuestion = np.array(data['Question'].values.tolist())
    dataAnswer = np.array(data['Answer'].values.tolist())
    return dataQuestion, dataAnswer


def main():
    filePath = input("please input your project name:")
    dataQuestion, dataAnswer = ReadCsv(filePath)
    wHtml.CreateHTML(dataQuestion, dataAnswer)
    wWord.CreateWord(dataQuestion, dataAnswer)


if __name__ == "__main__":
    main()
