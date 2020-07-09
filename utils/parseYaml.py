import os

import yaml

class ParseYaml:
    @classmethod
    def readYaml(cls,filename):
        try:

            thefile='{}.yaml'.format(filename)
            #print(thefile)
            current_path = os.path.dirname(__file__)
            parent_path=os.path.dirname(current_path)
            #current_path=os.getcwd()
            data_path=os.path.join(parent_path,'data')
            file_list=[file for file in os.listdir(data_path)
                       if os.path.isfile(os.path.join(data_path, file)) ] #获取目录下的所有文件列表
            dir_list=[file for file in os.listdir(data_path)
                       if os.path.isdir(os.path.join(data_path, file)) ]
            #print(dir_list)
            for file in file_list:
                if file==thefile:
                    with open(os.path.join(data_path, file), 'r', encoding="utf-8") as f:
                        y = yaml.load(f)
                    return y
            for dir in dir_list:
                    dir_path=os.path.join(data_path,dir)
                    print(dir_path)
                    sub_list=os.listdir(dir_path)
                    print(sub_list)
                    for sub_file in sub_list:
                        sub_file_path=os.path.join(dir_path, sub_file)
                        #print(sub_file_path)
                        #print(sub_file)
                        if sub_file==thefile:
                            with open(os.path.join(dir_path, sub_file), 'r', encoding="utf-8") as f:
                                y = yaml.load(f)
                            return y
        except:
            raise FileNotFoundError("No such file, plz check your filename")

if __name__=="__main__":
 print(ParseYaml.readYaml("Department"))