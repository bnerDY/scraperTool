__author__ = 'Martin'

import urllib
import urllib2


class Urltest:
    def __init__(self):
        # create header
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

        self.values = {'username': "email", 'password': "password"}
        self.data = urllib.urlencode(self.values)  # compiling
        self.url = "http://passport.csdn.net/account/login"

    def request(self):
        request = urllib2.Request(self.url, self.data, self.headers)
        response = urllib2.urlopen(request)
        print response.read()


class ErrorHandler:
    def __init__(self):
        self.req = urllib2.Request('aaa')

    def handle(self):
        try:
            response = urllib2.urlopen(self.req)
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
            elif hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason

        else:
            print 'No exception was raised.'


if __name__ == '__main__':
    u = Urltest()
    u.request()
    e = ErrorHandler()
    e.handle()
