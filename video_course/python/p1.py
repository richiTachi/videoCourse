import re
from urllib import request

class Spider():
    url = "https://www.douyu.com/"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        return htmls


    def __analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            number = re.findall(Spider.number_pattern,html)
            anchor = {"name":name,"number":number}
            anchors.append(anchor)
        print(anchors[0])
        return anchors

    def __sort(self,anchors):

    def refine(self,anchors):
        l = lambda anchor:{
            "name":anchor[0].strip(),
            'number':anchor[o]
            }
        return map(l,anchors)


    def go(self):
        self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.refine(anchors))
        print(anchors)

spider = Spider()
spider.go()


print(123123)