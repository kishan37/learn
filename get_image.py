import urllib2
import re
from os.path import basename
from urlparse import urlsplit

url = "http://www.atigunstocks.com/"
urlContent = urllib2.urlopen(url).read()
# HTML image tag: <img src="url" alt="some_text"/>
imgUrls = re.findall('img .*?src="(.*?)"', urlContent)

# download all images
for imgUrl in imgUrls:
    try:
        imgData = urllib2.urlopen(imgUrl).read()
        fileName = basename(urlsplit(imgUrl)[2])
        output = open(fileName,'wb')
        output.write(imgData)
        output.close()
    except:
        pass
