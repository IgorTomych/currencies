#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
from google.appengine.api import urlfetch

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')
        url = "http://bank.gov.ua/control/uk/curmetal/detail/currency?period=daily"
        result = urlfetch.fetch(url)
        if result.status_code == 200:
          #match = re.search(r'<td class="cell_c">(.*)</td>\s+</tr>', result.content, re.MULTILINE)
          match = re.findall(r'<td class="cell_c">(.*)</td>\s+<td class="cell_c">(.*)</td>\s+<td class="cell_c">(.*)</td>\s+<td class="cell">(.*)</td>\s+<td class="cell_c">(.*)</td>\s+</tr>', result.content, re.MULTILINE)
          if match:                      
            self.response.out.write(match)
          else:
            self.response.out.write('did not find')
          #self.response.out.write(result.content)

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
