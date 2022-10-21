
def PackMcMeta(packFormat) :
    packMcMeta = "{\n\t\"pack\": {\n\t\t\"pack_format\":" + packFormat + ",\n\t\t\"description\":\"Datapark datapack\"\n\t}\n}"
    return packMcMeta

def FunTagJson(packName, funType) :
    self.funTag = "{\n\t\"value\": [\n\t\t\"" + packName + ":" + funType + "\"\n\t]\n}"
    return funTag
