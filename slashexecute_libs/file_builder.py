
class PackMcMeta:
    def __init__(self, packFormat):
        self.packMcMeta = "{\n\t\"pack\": {\n\t\t\"pack_format\":" + packFormat + ",\n\t\t\"description\":\"Datapark datapack\"\n\t}\n}"
    def __str__(self):
        return "{seft.packMcMeta}"

class FunTagJson:
    def __init__(self, packName, funType):
        self.funTag = "{\n\t\"value\": [\n\t\t\"" + packName + ":" + funType + "\"\n\t]\n}"
    def __str__(self):
        return "{seft.funTag}"
