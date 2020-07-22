from wx_api.baseApi import BaseApi


class Tag(BaseApi):

    def create(self,tagname,tagid):
        json={
            "tagname":tagname,
            "tagid":tagid
        }
        self.source("Tag", "create").set_params().set_json(json).run()
        return self