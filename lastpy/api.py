
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

    user_getartisttracks = bind_api(
        endpoint = u'user.getartisttracks',
        allowed_params=['user', 'artist', 'startTimestamp', 'page', 'endTimestamp']
    )

    user_getbannedtracks = bind_api(
        endpoint = u'user.getbannedtracks',
        allowed_params=['user', 'limit', 'page']
    )

    user_getevents = bind_api(
        endpoint = u'user.getevents',
        allowed_params=['user', 'limit', 'page', 'fetivalsonly']
    )

    user_getfriends = bind_api(
        endpoint = u'user.getfriends',
        allowed_params=['user', 'recenttracks', 'limit', 'page']
    )

    user_getlovedtracks = bind_api(
        endpoint = u'user.getlovedtracks',
        allowed_params=['user', 'limit', 'page']
    )

    user_getneighbours = bind_api(
        endpoint = u'user.getneighbours',
        allowed_params=['user', 'limit']
    )

    user_getnewreleases = bind_api(
        endpoint = u'user.getnewreleases',
        allowed_params=['user', 'userecs']
    )

    user_getpastevents = bind_api(
        endpoint = u'user.getpastevents',
        allowed_params=['user', 'limit', 'page']
    )

    user_getpersonaltags = bind_api(
        endpoint = u'user.getpersonaltags',
        allowed_params=['user', 'tag', 'taggingtype', 'limit', 'page']
    )

    user_getplaylists = bind_api(
        endpoint = u'user.getplaylists',
        allowed_params=['user']
    )

    user_getrecentstations = bind_api(
        endpoint = u'user.getrecentstations',
        allowed_params=['user', 'limit', 'page'],
        require_auth=True
    )

    user_getrecenttracks = bind_api(
        endpoint = u'user.getrecenttracks',
        allowed_params=['user', 'limit', 'page', 'to', 'from']
    )

    user_getrecommendedartists = bind_api(
        endpoint = u'user.getrecommendedartists',
        allowed_params=['limit', 'page'],
        require_auth=True
    )

    user_getrecommendedevents = bind_api(
        endpoint = u'user.getrecommendedevents',
        allowed_params=['limit', 'page']
    )

    user_getshouts = bind_api(
        endpoint = u'user.getshouts',
        allowed_params=['user', 'limit', 'page']
    )

    user_shout = bind_api(
        endpoint = u'user.shout',
        allowed_params=['user', 'message'],
        require_auth=True,
        method='POST'
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

    """ Venue Methods """

    venue_getevents = bind_api(
        endpoint=u'venue.getevents',
        allowed_params=['venue','festivalsonly']
    )

    venue_getpastevents = bind_api(
        endpoint=u'venue.getpastevents',
        allowed_params=['venue','festivalsonly','page','limit']
    )

    venue_search = bind_api(
        endpoint=u'venue.search',
        allowed_params=['venue','page','limit','country']
    )

    """ Chart Methods """
    chart_gethypedartists = bind_api(
        endpoint=u'chart.gethypedartists',
        allowed_params=['page', 'limit']
    )

    chart_gethypedtracks = bind_api(
        endpoint=u'chart.gethypedtracks',
        allowed_params=['page', 'limit']
    )

    chart_getlovedtracks = bind_api(
        endpoint=u'chart.getlovedtracks',
        allowed_params=['page', 'limit']
    )

    chart_gettopartists = bind_api(
        endpoint=u'chart.gettopartists',
        allowed_params=['page', 'limit']
    )

    chart_gettoptags = bind_api(
        endpoint=u'chart.gettoptags',
        allowed_params=['page', 'limit']
    )

    chart_gettoptracks = bind_api(
        endpoint=u'chart.gettoptracks',
        allowed_params=['page', 'limit']
    )

    """ Library Methods """
    library_gettracks = bind_api(
        endpoint=u'library.gettracks',
        allowed_params=['user','artist','album','page','limit']
    )

    library_getalbums = bind_api(
        endpoint=u'library.getalbums',
        allowed_params=['user','artist','page','limit']
    )

    library_getartists = bind_api(
        endpoint=u'library.getartists',
        allowed_params=['user','page','limit']
    )

    library_addtrack = bind_api(
        endpoint=u'library.addtrack',
        allowed_params=['artist', 'track'],
        require_auth=True,
        method='POST'
    )

    library_addartist = bind_api(
        endpoint=u'library.addartist',
        allowed_params=['artist'],
        require_auth=True,
        method='POST'
    )

    library_addalbum = bind_api(
        endpoint=u'library.addalbum',
        allowed_params=['artist', 'album'],
        require_auth=True,
        method='POST'
    )

    library_removetrack = bind_api(
        endpoint=u'library.removetrack',
        allowed_params=['artist', 'track'],
        require_auth=True,
        method='POST'
    )

    library_removeartist = bind_api(
        endpoint=u'library.removeartist',
        allowed_params=['artist'],
        require_auth=True,
        method='POST'
    )

    library_removealbum = bind_api(
        endpoint=u'library.removealbum',
        allowed_params=['artist', 'album'],
        require_auth=True,
        method='POST'
    )

    library_removescrobble = bind_api(
        endpoint=u'library.removescrobble',
        allowed_params=['artist', 'album', 'timestamp'],
        require_auth=True,
        method='POST'
    )

    """ Track Methods """

track.addTags
track.addTags
track.ban
track.ban
track.getBuylinks
track.getBuylinks
track.getCorrection
track.getCorrection
track.getFingerprintMetadata
track.getFingerprintMetadata
track.getInfo
track.getInfo
track.getShouts
track.getShouts
track.getSimilar
track.getSimilar
track.getTags
track.getTags
track.getTopFans
track.getTopFans
track.getTopTags
track.getTopTags
track.love
track.love
track.removeTag
track.removeTag
track.scrobble
track.scrobble
track.search
track.search
track.share
track.share
track.unban
track.unban
track.unlove
track.unlove
track.updateNowPlaying
track.updateNowPlaying 