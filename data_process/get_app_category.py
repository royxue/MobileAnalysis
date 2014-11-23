import requests
import urllib2
import re

def get_app_category():
    app_file = open('app_list.txt', 'r')
    category = open('app_category.txt', 'w+')

    for line in app_file:
        line = line[:-1]
        target = 'https://play.google.com/store/apps/details?id=%s&hl=en' % (line)
        print target
        try:
            html = urllib2.urlopen(target).read()
            pat = r'<span itemprop="genre">(.*?)</span>'
            cate = re.findall(pat, html)
            category.write(line + ',' + cate[0] + '\n')
        except urllib2.HTTPError:
            category.write(line + ',' + 'Unknown' + '\n')

if __name__ == "__main__":
    get_app_category()
