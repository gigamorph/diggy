import diggy.const

class FrameworkGuesser(object):

    d7_markers = [
        'Drupal 7'
    ]

    d6_markers = []

    wp_markers = []

    ## response: a response from requests module
    @classmethod
    def guess_framework(cls, response):
        generator = response.headers.get('x-generator')

        if cls.match(generator, cls.d7_markers):
            return diggy.const.DRUPAL7
        elif cls.match(generator, cls.d6_markers):
            return diggy.const.DRUPAL6
        elif cls.match(generator, cls.wp_markers):
            return diggy.const.WORDPRESS

        return None

    @classmethod
    def match(cls, s, markers):
        if s != None:
            for marker in markers:
                if s.find(marker) > -1:
                    return True
        return False
