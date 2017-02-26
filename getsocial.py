'''
Ever wonder what social media accounts your favorite website uses?
Wait no more!
example usage:
$python getsocial.py 'https://wwww.myfavoritewebsite.com'
'''

import sys
from crawl import Crawler
from social import PageParse


def main(argv):
    '''Demonstrate it working by printing out results'''
    a = Crawler()
    a.init_browser()
    html = a.getContent(argv[0])
    d = PageParse(html, argv[0])
    data = d.socialmedia()
    a.exit()
    print(data)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        print(type(e), e.args, e)

