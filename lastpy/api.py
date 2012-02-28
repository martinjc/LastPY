
from lastpy.executor import bind_api
from lastpy.rate_controller import RateController
from lastpy.parsers import ModelParser

class API(object):

    def __init__( self, auth_handler=None,
                    cache=None, retry_count=0,
                    retry_delay=0, retry_errors=None,
                    parser=None, rate_controller=None ):
        self.auth_handler = auth_handler
        self.cache = cache
        self.retry_count = retry_count
        self.retry_errors = retry_errors
        self.parser = parser or ModelParser()
        self.rate_controller = rate_controller or RateController()

        self.scheme = 'http://'
        self.host = 'ws.audioscrobbler.com'
        self.root = '/2.0/'

    """ user methods """
    user_getinfo = bind_api(
        endpoint=u'user.getinfo',
        allowed_params=['user']
    )

    user_getweeklychartlist = bind_api(
        endpoint = u'user.getWeeklyChartList',
        allowed_params = ['user']
    )

    user_getweeklyalbumchart = bind_api(
        endpoint = u'user.getweeklyalbumchart',
        allowed_params = ['user', 'from', 'to']
    )

    user_getweeklytrackchart = bind_api(
        endpoint = u'user.getweeklytrackchart',
        allowed_params = ['user', 'from', 'to']
    )

    user_getweeklyartistchart = bind_api(
        endpoint = u'user.getweeklyartistchart',
        allowed_params = ['user', 'from', 'to']
    )

    user_gettoptracks = bind_api(
        endpoint = u'user.gettoptracks',
        allowed_params = ['user', 'period', 'limit', 'page']
    )

    user_gettopartists = bind_api(
        endpoint = u'user.gettopartists',
        allowed_params = ['user', 'period', 'limit', 'page']
    )

    user_gettopalbums = bind_api(
        endpoint = u'user.gettopalbums',
        allowed_params = ['user', 'period', 'limit', 'page']
    )

    user_gettoptags = bind_api(
        endpoint = u'user.gettoptags',
        allowed_params = ['user', 'limit']
    )