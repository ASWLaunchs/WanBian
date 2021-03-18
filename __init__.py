import pandas as pd
import numpy as np


def ReadData():
    # data be used to storage QUestion col data which in csv.
    data = pd.read_csv("data/testing.csv", usecols=[0, 1], converters={
        "Question": str, "Answer": str}, encoding='GB18030')
    dataQuestion = np.array(data['Question'].values.tolist())
    dataAnswer = np.array(data['Answer'].values.tolist())

def main():
    ReadData()

if __name__ == "__main__":
    main()
