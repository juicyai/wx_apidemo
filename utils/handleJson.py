import json
import pystache


class ParseJson:
    @classmethod
    def readJson(cls,filename):
        try:
            with open('../data/{}.json'.format(filename), 'r', encoding="utf-8") as f:
                j = json.load(f)

            return j
        except:
            raise FileNotFoundError("No such file, plz check your filename")

    @classmethod
    def parsejson(cls,fp,dict):
        return pystache.render(fp,dict)


#fp=ParseJson.readJson("create_body")
# print(fp)
# print(ParseJson.parsejson(str(fp),{"name":"jupiter","userid":123456}))