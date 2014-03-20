import re
import socket
from urlparse import urlparse

class Miner(object):

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


