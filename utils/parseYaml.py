import yaml

class ParseYaml:
    @classmethod
    def readYaml(cls,filename):
        try:
            with open('../data/{}.yaml'.format(filename), 'r', encoding="utf-8") as f:
                y = yaml.load(f)

            return y
        except:
            raise FileNotFoundError("No such file, plz check your filename")
