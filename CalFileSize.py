from odps.udf import annotate
import urllib.request


@annotate("string -> string,string,string,string,string")
class CalFileSize(object):
    def evaluate(self, arg):
        # 不会下载文件
        resp = urllib.request.urlopen(arg)
        # 响应数据的数据长度，单位是byte
        file_size = resp.headers['content-length']
        print(file_size)
        return file_size
