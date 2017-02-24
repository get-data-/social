'''docstring for identifying social media accounts'''

from bs4 import BeautifulSoup
import tldextract


def getDomain(url):
    return tldextract.extract(url).domain


def hasSubdomain(url):
    return tldextract.extract(url).subdomain


class PageParse(object):
    '''This function takes a webpage's HTML and
    extracts information from it'''

    # Unique social media domain strings
    socials = [
            '500px',
            'abou.to',
            'about.me',
            'angel.co',
            'aviary',
            'badoo',
            'bandcamp',
            'basecamphq',
            'behance.net',
            'bitbucket.org',
            'bitly',
            'blinklist',
            'blip.fm',
            'blogspot',
            'buzzfeed',
            'cafemom',
            'canva',
            'cash.me',
            'codecademy',
            'codementor.io',
            'coinbase',
            'colourlovers',
            'community.wikia',
            'contently',
            'creativemarket',
            'crokes',
            'dailymotion',
            'designspiration.net',
            'deviantart',
            'disqus',
            'dribbble',
            'ebay',
            'edmodo',
            'ello.co',
            'en.gravatar',
            'etsy',
            'facebook',
            'fanpop',
            'fiverr',
            'flavors.me',
            'flickr',
            'flipboard',
            'fotolog',
            'foursquare',
            'geekli.st',
            'getsatisfaction',
            'github',
            'gogobot',
            'goodreads',
            'hitbox.tv',
            'houzz',
            'hubpages',
            'ifttt',
            'ifunny.co',
            'imgur',
            'instagram',
            'instructables',
            'keybase.io',
            'kongregate',
            'last.fm',
            'livejournal',
            'medium',
            'meetup',
            'mig.me',
            'miiverse.nintendo.net',
            'myspace',
            'newgrounds',
            'news.ycombinator',
            'okcupid',
            'open.spotify',
            'pandora',
            'papaly',
            'pastebin',
            'patreon',
            'paypal.me',
            'photobucket',
            'pinterest',
            'plus.google',
            'postagon',
            'producthunt',
            'reddit',
            'reverbnation',
            'roblox',
            'scribd',
            'seatwish',
            'slack',
            'slideshare.net',
            'snapchat',
            'soundcloud',
            'soup.io',
            'steamcommunity',
            'stream.me',
            'stumbleupon',
            'teamtreehouse',
            'technorati',
            'tracky',
            'trakt.tv',
            'tripadvisor',
            'tripit',
            'tsu.co',
            'tumblr',
            'twitch.tv',
            'twitter',
            'ustream.tv',
            'venmo',
            'viddler',
            'vimeo',
            'vine.co',
            'vk.com',
            'wattpad',
            'webcred.it',
            'wikia',
            'wikipedia.org',
            'wishlistr',
            'wittyprofiles',
            'wordpress',
            'world.kano.me',
            'xfire',
            'yelp',
            'youtube',
            'story.kakao',
            'cafe.naver',
            'blog.naver',
            'weibo',
            'qyer',
            'youku.com',
            'qq.com',
            'weibo.com',
            'ok.ru']

    def __init__(self, html, url):
        '''Pass the webpage's HTML as a string which is then turned into a
        BeautifulSoup object'''
        self.html = html
        self.url = url
        self.soup = BeautifulSoup(html, 'html5lib')

    def gethrefs(self):
        hrefs = self.soup.find_all('a', href=True)
        data = [link['href'] for link in hrefs if 'http' in link['href']]
        return data

    def getDomain(self):
        return tldextract.extract(self.url).domain

    def hasSubdomain(self):
        return tldextract.extract(self.url).subdomain

    def socialmedia(self):
        hrefs = self.gethrefs()
        results = [href for s in self.socials for href in hrefs if s in href]
        data = {'url': self.url}
        for result in results:
            data.update({getDomain(result): result})
        return data
