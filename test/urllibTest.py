__author__ = 'Martin'

import urllib
import urllib2

if __name__ == '__main__':
    values = {'username': "email", 'password': "password"}
    data = urllib.urlencode(values)  # compiling
    url = "http://passport.csdn.net/account/login"
    geturl = url + "?" + data
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    print response.read()
