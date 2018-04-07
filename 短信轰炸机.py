#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-11 08:43:40
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import http.cookiejar

cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open("http://t.sohu.com/settings/bindMobile/registSendVerificationCode")
data={"mobileNumber":"18000314624"}
r=opener.open("http://t.sohu.com/settings/bindMobile/registSendVerificationCode",urllib.urlencode(data))
print(r.read())
