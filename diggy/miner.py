import re
import socket
from urlparse import urlparse


class Miner(object):

    _ga_patterns = [ 
        (re.compile(r"""getTracker\s*\(\s*['"](.*?)['"]""", 
                    re.MULTILINE|re.DOTALL), 0),
        (re.compile(r"""ga\(\s*['"]create['"]\s*,\s*['"](UA-.*?)['"]""", 
                    re.MULTILINE|re.DOTALL), 0),
        (re.compile(r"""\[\s*['"]([\w_]+\.)?_setAccount['"]\s*,\s*['"](UA-.*?)['"]""", 
                    re.MULTILINE|re.DOTALL), 1),
        (re.compile(r"""_uacct\s*=\s*['"](UA-.*?)['"].*urchinTracker""", 
                    re.MULTILINE|re.DOTALL), 0)
        ]

    _newrelic_pattern = re.compile(r'agent.newrelic.com', re.MULTILINE|re.DOTALL)

    ## Return the ip address (string) for the url (string)
    @staticmethod
    def get_ip(url):
        result = urlparse(url)
        netloc = result.netloc
        m = re.match(r'(.*):\d+$', netloc)
        if m != None:
            hostname = m.group(1)
        else:
            hostname = netloc
        try:
            ip_str = socket.gethostbyname(hostname)
        except Exception as e:
            ip_str = ''

        return ip_str

    ## 
    @classmethod
    def _match_ga_code(cls, pattern_pair, text):
        pattern, pos = pattern_pair
        codes = []
        results = pattern.findall(text)
        for result in results:
            result_type = type(result)
            if result_type == tuple:
                codes.append(result[pos])
            else:
                codes.append(result)
        return codes

    ## Extract Google Analytics tracking codes
    @classmethod
    def get_ga_codes(cls, html_text):
        ga_codes = []

        for pattern in cls._ga_patterns:
            codes = cls._match_ga_code(pattern, html_text)
            ga_codes += codes

        return ga_codes

    ## Return True if the text contains a NewRelic code
    @classmethod
    def has_newrelic(cls, html_text):
        match = cls._newrelic_pattern.search(html_text)
        return match != None
