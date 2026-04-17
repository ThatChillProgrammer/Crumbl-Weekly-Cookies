from lxml import etree
import urllib.request as urlreq


def getHTML(url:str):
    opener = urlreq.build_opener()
    opener.addheaders = [('User-Agent', 'MyApp/1.0')]
    urlreq.install_opener(opener)
    return urlreq.urlopen(url)

def getCookies(response):
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    print("Weekly Crumbl Cookies:")
    for i in range(2,10):
        try:
            print(tree.xpath(f'/html/body/div/div/div[4]/div[1]/div[2]/div[{i}]/div/div[2]/div[1]/p[1]')[0].text)
        except: return 1
    return 0


html = getHTML('https://crumblcookies.com/')
getCookies(html)


