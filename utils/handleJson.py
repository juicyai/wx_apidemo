import json
import logging
import os

import pystache


class ParseJson:
    logging.basicConfig(
         format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s',
         datefmt='%m/%d/%Y %I:%M:%S %p',
         level=logging.DEBUG)
    @classmethod
    def readJson(cls,filename):
        # try:
        #     with open('../data/{}.json'.format(filename), 'r', encoding="utf-8") as f:
        #         j = json.load(f)
        #
        #     return j
        # except:
        #     raise FileNotFoundError("No such file, plz check your filename")
        try:

            thefile='{}.json'.format(filename)
            #print(thefile)
            current_path = os.path.dirname(__file__)
            parent_path=os.path.dirname(current_path)
            #current_path=os.getcwd()
            data_path=os.path.join(parent_path,'data')
            file_list=[file for file in os.listdir(data_path)
                       if os.path.isfile(os.path.join(data_path, file)) ] #获取data目录下的所有文件列表
            dir_list=[file for file in os.listdir(data_path)
                       if os.path.isdir(os.path.join(data_path, file)) ] #获取data目录下的所有目录
            #print(dir_list)
            for file in file_list:
                if file==thefile:
                    with open(os.path.join(data_path, file), 'r', encoding="utf-8") as f:
                        j = json.load(f)
                    return j
            for dir in dir_list:
                    dir_path=os.path.join(data_path,dir)
                    logging.info("dirpath:{}".format(dir_path))
                    sub_list=os.listdir(dir_path)
                    logging.info("sub_list:{}".format(sub_list))
                    for sub_file in sub_list:
                        sub_file_path=os.path.join(dir_path, sub_file)
                        #print(sub_file_path)
                        #print(sub_file)
                        if sub_file==thefile:
                            with open(os.path.join(dir_path, sub_file), 'r', encoding="utf-8") as f:
                                j = json.load(f)
                            return j
        except:
            raise FileNotFoundError("No such file, plz check your filename")

    @classmethod
    def parsejson(cls,fp,d: dict):
        parsed=pystache.parse(u"{}".format(fp))
        logging.info("parsed:{}".format(parsed))
        js=pystache.render(parsed,d)
        logging.info("render js:{}".format(js))
        return js


fp=ParseJson.readJson("create_body")
print(fp)
print(ParseJson.parsejson(str(fp),{"name":"jupiter","userid":123456}))