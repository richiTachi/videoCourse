import requests
import json
from pyquery import PyQuery


import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Spider():

    url = "https://www.hsehome.com/document/home"

    def __fetch_content(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(Spider.url, headers=headers)
        return response.text


    def __analysis(self,htmls):
        doc = PyQuery(htmls)
        root_html = doc("div.doc-ls .doc-item.inB")
        list = []
        for item in root_html.items():
            info = {}
            info["title"] = item.find(".text-oh.title").text()
            info["price"] = item.find(".price").text()
            info["user"] = item.find(".inB.b-title.text-oh.middle.cur").text()
            list.append(info)
        print(list)
        return list

    def write_to_file(self, content):
        # 写入文件
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(json.dumps(content, ensure_ascii=False) + "\n")


    def go(self):
        htmls = self.__fetch_content()
        # print(htmls)
        list = self.__analysis(htmls)
        for item in list:
            self.write_to_file(item)
        # print(anchors)

spider = Spider()
spider.go()