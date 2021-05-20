import markdown

class Markdown:
	def __init__(self):
		pass
	
	#Create() is used to create a html by modularize 
	def Create(self,markdownContent):
		
		html = markdown.markdown(markdownContent)
