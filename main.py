import sys
import packages.wanbian.wanbian as WanBian
import packages.wanbian_help.help as wHelp

def main():
    # Determine whether the corresponding parameters are passed in that by the sys.argv length when starting the program.
    WHelp = wHelp.Help()
    # instantiate the WanBian class.
    WB = WanBian.WanBian()
    if len(sys.argv) >= 2:
        # new operation.
        if sys.argv[1] == 'new' and len(sys.argv) == 4:
            projectName = str(sys.argv[2])
            projectType = str(sys.argv[3])
            WB.CreateFile(projectName, projectType)
        # build operation.
        elif sys.argv[1] == 'build' and len(sys.argv) == 3:
            projectName = str(sys.argv[2])
            WB.BuildProject(projectName)
        # delete operation.
        elif sys.argv[1] == 'delete' and len(sys.argv) == 3:
            projectName = str(sys.argv[2])
            WB.DeleteProject(projectName)
        # help operation.
        elif sys.argv[1] == 'help' and len(sys.argv) == 2:
            WHelp.Help()
        # help project type operation.
        elif sys.argv[1] == 'helpProjectType' and len(sys.argv) == 2:
            WHelp.HelpProjectType()
        # default choice.
        else:
            WHelp.HelpNothingInput()
    else:
        WHelp.HelpNothingInput()


if __name__ == "__main__":
    main()
