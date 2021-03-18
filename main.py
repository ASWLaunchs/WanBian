import pandas as pd
import numpy as np
import wanbian_html.wanbian_html as wh
import wanbian_word.wanbian_word as ww


def ReadCsv():
    # data be used to storage QUestion col data which in csv.
    data = pd.read_csv("resource/demo/demo.csv", usecols=[0, 1], converters={
        "Question": str, "Answer": str}, encoding='GB18030')
    dataQuestion = np.array(data['Question'].values.tolist())
    dataAnswer = np.array(data['Answer'].values.tolist())


def main():
    ReadCsv()
    wh.CreateHTML()
    ww.Output()


if __name__ == "__main__":
    main()
