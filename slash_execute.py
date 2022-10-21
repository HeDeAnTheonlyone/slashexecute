
import slashexecute_libs.command_code as command_code

file = open("script.slashexe", "r")

# get new code line
def getNewLine():
    code = file.readline()
    if (code != "\n"):
        return(code[:-1]) if (code.endswith("\n")) else (code)


# main Code
for lines in file:
    args = getNewLine().split(" ")

    if (args[0] == "datapack"): command_code.createPackTemplate(args[1].strip("()").split(","))
    if (args[0] == "func"): command_code.createNewFile(args)

