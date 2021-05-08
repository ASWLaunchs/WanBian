from docx import Document
from docx.shared import Inches
import docx
import wanbian_hash.hash as wHash


class wordTesting:
    def __init__(self):
        # initialize extra class.
        self.WHash = wHash.Hash()

    def CreateHashArr(self, projectName, projectTitle, dataQuestion, dataAnswer, count):
        while count > 0:
            count -= 1
            document = Document()
            document.add_heading(projectTitle, 0)
            for i in range(0, len(dataQuestion)):
                document.add_paragraph(
                    dataQuestion[i]+"\n"+dataAnswer[i] + "\n", style='List Number'
                )
            document.add_page_break()
            document.save("data/"+projectName+"/"+self.WHash.hash()+".docx")

    def CreateSerialArr(self, projectName, dataQuestion, dataAnswer, count):
        pass
