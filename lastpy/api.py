
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
        allowed_params = ['user', 'from', 'to'],
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

    """ album methods """
    album_getinfo = bind_api(
        endpoint = u'album.getinfo',
        allowed_params=['album', 'artist', 'mbid', 'lang', 'autocorrect', 'username']
    )

    album_addtags = bind_api(
        endpoint = u'album.addtags',
        allowed_params=['artist', 'album', 'tags'],
        require_auth=True,
        method = 'POST'
    )

    album_gettags = bind_api(
        endpoint = u'album.gettags',
        allowed_params=['artist', 'album', 'mbid', 'autocorrect', 'user']
    )

    album_getbuylinks = bind_api(
        endpoint = u'album.getbuylinks',
        allowed_params=['artist','album','mbid','autocorrect','country']
    )

    album_removetag = bind_api(
        endpoint = u'album.removetag',
        allowed_params=['artist', 'album', 'tag'],
        require_auth=True,
        method='POST'
    )

    album_gettoptags = bind_api(
        endpoint=u'album.gettoptags',
        allowed_params=['artist','album','mbid','autocorrect']
    )

    album_getshouts = bind_api(
        endpoint=u'album.getshouts',
        allowed_params=['artist','mbid','limit','autocorrect','page']
    )

    album_search = bind_api(
        endpoint=u'album.search',
        allowed_params=['limit','page','album']
    )

    album_share = bind_api(
        endpoint=u'album.share',
        allowed_params=['artist','album','public','message','recipient'],
        method='POST',
        require_auth=True
    )

    """ artist methods """
    artist_getinfo = bind_api(
        endpoint = u'artist.getinfo',
        allowed_params=['artist', 'mbid', 'lang', 'autocorrect', 'username']
    )

    artist_addtags = bind_api(
        endpoint = u'artist.addtags',
        allowed_params=['artist', 'tags'],
        require_auth=True,
        method = 'POST'
    )

    artist_removetag = bind_api(
        endpoint = u'artist.removetag',
        allowed_params=['artist','tag'],
        method='POST',
        require_auth=True
    )

    artist_gettags = bind_api(
        endpoint = u'artist.gettags',
        allowed_params=['artist', 'mbid', 'user', 'autocorrect']
    )

    artist_getcorrection = bind_api(
        endpoint=u'artist.getcorrection',
        allowed_params=['artist']
    )

    artist_getevents = bind_api(
        endpoint=u'artist.getevents',
        allowed_params=['artist','mbid','autocorrect','limit','page','festivalsonly']
    )

    artist_getimages = bind_api(
        endpoint= u'artist.getimages',
        allowed_params=['artist','mbid','page','limit','autocorrect','order']
    )

    artist_getpastevents = bind_api(
        endpoint = u'artist.getpastevents',
        allowed_params=['artist','mbid','page','autocorrect','limit']
    )

    artist_getsimilar = bind_api(
        endpoint=u'artist.getsimilar',
        allowed_params=['artist','limit','autocorrect','mbid']
    )

    artist_getshouts = bind_api(
        endpoint=u'artist.getshouts',
        allowed_params=['artist', 'mbid', 'limit', 'autocorrect', 'page']
    )

    artist_gettopalbums = bind_api(
        endpoint=u'artist.gettopalbums',
        allowed_params=['artist', 'mbid', 'limit', 'autocorrect', 'page']
    )
    artist_gettoptags = bind_api(
        endpoint=u'artist.gettoptags',
        allowed_params=['artist', 'mbid', 'autocorrect']
    )

    artist_gettoptracks = bind_api(
        endpoint=u'artist.gettoptracks',
        allowed_params=['artist', 'mbid', 'limit', 'autocorrect', 'page']
    )

    artist_gettopfans = bind_api(
        endpoint=u'artist.gettopfans',
        allowed_params=['artist', 'mbid', 'autocorrect']
    )

    artist_getpodcast = bind_api(
        endpoint=u'artist.getpodcast',
        allowed_params=['artist', 'mbid', 'autocorrect']
    )

    artist_search = bind_api(
        endpoint=u'artist.search',
        allowed_params=['limit','page','artist']
    )

    artist_share = bind_api(
        endpoint=u'artist.share',
        allowed_params=['artist','public','message','recipient'],
        method='POST',
        require_auth=True
    )

    artist_shout = bind_api(
        endpoint=u'artist.shout',
        allowed_params=['artist','message'],
        method='POST',
        require_auth=True        
    )