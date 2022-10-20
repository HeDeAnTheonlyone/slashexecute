
import os
import slashexecute_libs.file_builder as file_builder

# create new data pack
def createPackTemplate(args):
    global packName
    packName = args[0]
    
    os.makedirs(args[0] + "\data\\" + args[0] + "\\functions")
    os.makedirs(args[0] + "\data\minecraft\\tags\\functions")

    path = args[0] + "\data\minecraft\\tags\\functions"

    packMcMeta = open(args[0] + "\pack.mcmeta", "a")
    packMcMetaJson = file_builder.PackMcMeta(args[1])
    packMcMeta.write(packMcMetaJson.packMcMeta)
    packMcMeta.close()

    if(eval(args[2].lower().capitalize())):
        loadFun = open(path + "\load.json", "a")
        loadFunJson = file_builder.FunTagJson(args[0], "load")
        loadFun.write(loadFunJson.funTag)
        loadFun.close()

    if(eval(args[3].lower().capitalize())):
        tickFun = open(path + "\\tick.json", "a")
        tickFunJson = file_builder.FunTagJson(args[0], "tick")
        tickFun.write(tickFunJson.funTag)
        tickFun.close()
    

# create make new file
def createNewFile(args):
    path = "\\" + packName + "\data\\" + packName + "\\functions\\" + args[1] + ".mcfunction"
    funFile = open(path, "a")
    #TO DO: write code that writes code in the new file
    funFile.close()
