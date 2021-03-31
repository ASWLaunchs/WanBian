class Help:
    def __init__(self):
        pass

    def HelpNothingInput(self):
        self.promptTxt = '''
        >>> If you want to create a new project , then you should input projectName and projectType, such as \'python main.py [projectName] [projectType] \'\n
        >>> If you want to compile available project , then you should input \'python main.py [projectName] build\'\n 
        >>> If you want to view the help manual , then you should input \'python main.py help\'\n 
        '''
        self.output()

    def HelpProjectType(self):
        self.promptTxt = '''
        what means those nums maps in project type args ? \n
        - 0 prefix means single page product. \n
        - 1 prefix means multiple pages product. \n

        |   code  |introduction| \n
        |---------|------------------------------| \n
        |0_testing|produce the testing docx file.| \n
        |0_webpage|produce the homepage html file.| \n
        |0_game   |produce the game html+css+js file.| \n
        |1_testing|produce the testing docx files.| \n
        |1_webpage|produce the web page html files.| \n
        |1_game   |produce the game html+css+js files.| \n
        '''
        self.output()

    def Help(self):
        self.promptTxt = '''
        > view the help manual:
        python main.py help
        > create new project:
        python main.py new [project name] [project type]
        > start complie project:
        python main.py build [project name]
        > view the project type be supported:
        python main.py helpProjectType
        '''
        self.output()

    def output(self):
        print("{}\n".format(self.promptTxt))
