# coding:utf-8

import webbrowser
import random
import wanbian_markdown.md as wMarkdown
import wanbian_hash.hash as wHash

class HtmlTesting:
    def __init__(self):
        # initialize extra class.
        self.WHash = wHash.Hash()     
        self.WMarkdown = wMarkdown.Markdown()
        # import css file.
        self.htmlStyle = ''
        
    #get project configuration about style.
    def GetConf(self):
        styleNum=random.randint(0,3)
        if styleNum == 0:
            self.htmlStyle = 'bootstrap'
         elif styleNum == 1:
            self.htmlStyle = 'layui'
         else:
            self.htmlStyle = 'kok'
        
    # CreateHashArr() produces the file ,it's file name according to time hash value. 
    def CreateHashArr(self, projectName, projectTitle, markdownContent, count):
        while count > 0:
            # create html.
            fileHTML = "data/"+projectName+"/"+self.WHash.hash()+".html"
            # open the file ready to write.
            f = open(fileHTML, 'w')

            # assign some contents.
            #first %s is page title,second %s is css link , third %s is html content.
            htmlCss = "<link rel=\'stylesheet\' href=\'" + self.htmlStyle + "\'>"
            htmlMain = '<html><title>%s</title><head>%s</head><body>%s</body></html>' % (projectTitle,htmlCss)
            htmlContent = self.WMarkdown.modularize(markdownContent)

            # write sth to the file.
            f.write(htmlMain+htmlContent)
            # close file.
            f.close()

            # automatically show it in webpages.
            webbrowser.open(fileHTML, new=1)
            '''
                webbrowser.open(url, new=0, autoraise=True) 
                Display url using the default browser. If new is 0, the url is opened in the same browser window if possible. If new is 1, a new browser window is opened if possible. If new is 2, a new browser page (“tab”) is opened if possible. If autoraise is True, the window is raised if possible (note that under many window managers this will occur regardless of the setting of this variable).
                '''
