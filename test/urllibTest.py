__author__ = 'Martin'

import urllib
import urllib2

# create header
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

values = {'username': "email", 'password': "password"}
data = urllib.urlencode(values)  # compiling
url = "http://passport.csdn.net/account/login"


if __name__ == '__main__':
    # geturl = url + "?" + data
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    print response.read()
