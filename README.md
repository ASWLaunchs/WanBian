# WanBian

![Logo](images/logo.png)

Wanbian (WanBian), an intelligent production tool capable of various changes, can automatically produce static web pages.

The back-end and artificial intelligence technology uses Python scripting language combined with Github's mature tool libraries for rapid development. The front-end page technology uses traditional HTML, CSS, and JS. The tool core of the entire project is produced based on the Linux operating system, and the data is sent out through the api. Need to call api to get data.
because of the armhf architecture cannot support newest MongoDB，so we cancel storge date in database and use document system replace this method.

After the development of the entire program is completed, the first version will be released on Github, open source and share all technologies.

# How did it work ?

## data stream
![DataStream](images/DataStream_en.png)

# How is the work progress?
Now it is cannot avaliable , the project is still under developing status. 

# Our project plan (Now is the Early stage)
Early stage: achieve automatic production of unlimited non-repetitive web pages. （√）
Middle stage: It can automatically produces web site source codes which only supports the server language is Node.js.（×）
late stage:It can designs all kinds of IoT project solutions , packs the website server ny the way.(×)
# Usage
## how to automatically produce docx and html files , other types ,and so on? 
- (1) launch the main.py with some arguments which in WanBian folder.

format:
```bash
main.py [project name] [product type]
```

usage example:
```bash
#if you want to product a docx file which name is "demo" , then input as below format.
main.py demo docx
#Let's change another type , such as HTML.
main.py demo html
```

which product types do it supports now ?
```bash
    html , docx   
```

- (2) input the project name what you want to create.
- (3) find the csv file with the corresponding project name what in the resource folder in the corresponding project name folder , then editor it following to right content format.
- (4) when you finished step (3) , save that csv file and input "WanBian server" in console , it's start up !
- (5) it is in the data folder that your want.