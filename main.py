import pandas as pd
import numpy as np
import wanbian_html.html_testing as wHtml
import wanbian_word.word_testing as wWord


def ReadCsv():
    # data be used to storage QUestion col data which in csv.
    data = pd.read_csv("resource/demo/demo.csv", usecols=[0, 1], converters={
        "Question": str, "Answer": str}, encoding='GB18030')
    dataQuestion = np.array(data['Question'].values.tolist())
    dataAnswer = np.array(data['Answer'].values.tolist())
    return dataQuestion, dataAnswer


def main():
    dataQuestion, dataAnswer = ReadCsv()
    wHtml.CreateHTML(dataQuestion, dataAnswer)
    wWord.CreateWord(dataQuestion, dataAnswer)


if __name__ == "__main__":
    main()
