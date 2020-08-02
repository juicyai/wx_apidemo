from wx_api.baseApi import BaseApi


class Media(BaseApi):

   def upload(self,type=None,filename=None,content_type=None,**kwargs):
       # fp=
       # m=self.get_multipartm()
       # headers={
       #     "content_type":m.content_type
       # }
       # self.source("media","upload").set_params(type=type).set_headers(headers).set_data(m).run()
       return self

