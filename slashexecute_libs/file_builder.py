
def PackMcMeta(packFormat, path) :
    packMcMeta = "{\n\t\"pack\": {\n\t\t\"pack_format\":" + packFormat + ",\n\t\t\"description\":\"Datapark datapack\"\n\t}\n}"
    path.write(packMcMeta)

def FunTagJson(packName, funType, path) :
    funTag = "{\n\t\"values\": [\n\t\t\"" + packName + ":" + funType + "\"\n\t]\n}"
    path.write(funTag)
