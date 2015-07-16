import logging
import re
from urlparse import urljoin

class ResponsiveDesign(object):

    def __init__(self, html_get):
        """
        html_get: function (url), returns HTML text from url.
        """
        self.html_get = html_get

    def guess(self, html, base_url):
        return self.detect_media_queries(html, base_url)

    def detect_media_queries(self, html, base_url):
        p = re.compile(r'''<link[^>]*?['"]([^'"]+\.css)''')
        regex_iter = p.finditer(html)

        for m in regex_iter:
            p = re.compile(r'\\')
            css_url = p.sub('', m.group(1))
            p = re.compile(r' ')
            css_url = p.sub(r'%20', css_url)
            p = re.compile(r'\.\./')
            css_url = p.sub('', css_url)
            css_url = urljoin(base_url, css_url)
            
            print 'C %s' % css_url

            if self.find_media_tag(css_url):
                return True
        return False

    def find_media_tag(self, css_url):
        try:
            response = self.html_get(css_url)
            css_text = unicode(response.content, errors='replace')
            p = re.compile(r'@media')
            m = p.search(css_text)
            return m != None
        except Exception as e:
            logging.warning('FAILED processing %s - %s' % (css_url, str(e)))
        return False
