# coding:utf-8

import webbrowser
import random
import wanbian_hash.hash as wHash

class HtmlTesting:
    def __init__(self):
        # initialize extra class.
        self.WHash = wHash.Hash()
        
    # CreateHashArr() produces the file ,it's file name according to time hash value. 
    def CreateHashArr(self, projectName, projectTitle, dataQuestion, dataAnswer, count):
        while count > 0:
            # create html.
            fileHTML = "data/"+projectName+"/"+self.WHash.hash()+".html"
            # open the file ready to write.
            f = open(fileHTML, 'w')

            # assign some content.
            str1 = 'my name is :'
            str2 = '--zongxp--'

            message = """
                <html>
                <head></head>
                <body>
                <p>%s</p>
                <p>%s</p>
                </body>
                </html>""" % (str1, str2)

            # write sth to the file.
            f.write(message)
            # close file.
            f.close()

            # automatically show it in webpages.
            webbrowser.open(fileHTML, new=1)
            '''
                webbrowser.open(url, new=0, autoraise=True) 
                Display url using the default browser. If new is 0, the url is opened in the same browser window if possible. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible. If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
                '''
