import unittest

from diggy.miner import Miner


class TestMiner(unittest.TestCase):

    def test_get_ga_codes(self):
        html = '''<html><head><title>SagaX</head><body>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-99997777-1', 'example.com');
  ga('create', 'UA-77779999-1', 'example.com', {'name': 'second_ua'});  // Second UA tracker.
  ga('send', 'pageview');
  ga('second_ua.send', 'pageview');
</script>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-99997777-2']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
</body></html>'''
        codes = Miner.get_ga_codes(html)
        
        print 'codes=%s' % codes

