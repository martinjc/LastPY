import inspect

class Model( object ):

    members = {}

    def __init__( self, api=None ):
        self._api = api

    def __getstate__( self ):
        # pickle
        pickle = dict( self.__dict__ )
        try:
            del pickle['_api']  # do not pickle the API reference
        except KeyError:
            pass
        return pickle

    def restore_api( self, api ):
        
        self._api = api

        members = inspect.getmembers( self, inspect.isclass )
        for name, member in members:
            if isinstance( member, Model ):
                member.restore_api( api )

    @classmethod
    def parse( cls, api, json ):
        obj = cls( api )
        if hasattr( json, 'items' ):
            for k, v in json.items():
                k = k.lstrip( '@' ).lstrip( '#' )
                try:
                    model = getattr( ModelFactory, k )
                    if isinstance(v, list):
                        results = []
                        for item in v:
                            results.append( model.parse( api, item) )
                        k = cls.members.get(k, k)
                        setattr( obj, k, results )
                    else:
                        k = cls.members.get(k, k)
                        setattr( obj, k, model.parse( api, v ) )
                except AttributeError:
                    k = cls.members.get(k, k)
                    setattr( obj, k, v )
        else:
            return json
        return obj  


class User( Model ):

    members = {
        'image' : 'images'
    }

    def info(self, **kargs):
        return self._api.user_getinfo( user=self.name, **kargs )

    def weeklychartlist( self, **kargs ):
        return self._api.user_getweeklychartlist( user=self.name, **kargs )

    def weeklyalbumchart( self, **kargs ):
        return self._api.user_getweeklyalbumchart( user=self.name, **kargs )

    def weeklyartistchart( self, **kargs ):
        return self._api.user_getweeklyartistchart( user=self.name, **kargs )

    def weeklytrackchart( self, **kargs ):
        return self._api.user_getweeklytrackchart( user=self.name, **kargs )

    def toptracks( self, **kargs ):
        return self._api.user_gettoptracks( user=self.name, **kargs )

    def topartists( self, **kargs ):
        return self._api.user_gettopartists( user=self.name, **kargs )

    def topalbums( self, **kargs ):
        return self._api.user_gettopalbums( user=self.name, **kargs )

    def toptags( self, **kargs ):
        return self._api.user_gettoptags( user=self.name, **kargs )

    def artisttracks( self, **kargs ):
        return self._api.user_getartisttracks( user=self.name, **kargs )

    def bannedtracks( self, **kargs ):
        return self._api.user_getbannedtracks( user=self.name, **kargs )

    def events( self, **kargs ):
        return self._api.user_getevents( user=self.name, **kargs )

    def friends( self, **kargs ):
        return self._api.user_getfriends( user=self.name, **kargs )

    def lovedtracks( self, **kargs ):
        return self._api.user_getlovedtracks( user=self.name, **kargs )

    def neighbours( self, **kargs ):
        return self._api.user_getneighbours( user=self.name, **kargs )

    def newreleases( self, **kargs ):
        return self._api.user_getnewreleases( user=self.name, **kargs )

    def pastevents( self, **kargs ):
        return self._api.user_getpastevents( user=self.name, **kargs )

    def personaltags( self, **kargs ):
        return self._api.user_getpersonaltags( user=self.name, **kargs )

    def playlists( self, **kargs ):
        return self._api.user_getplaylists( user=self.name, **kargs )

    def recentstations( self, **kargs ):
        return self._api.user_getrecentstations( user=self.name, **kargs )

    def recenttracks( self, **kargs ):
        return self._api.user_getrecenttracks( user=self.name, **kargs )

    def recommendedartists( self, **kargs ):
        return self._api.user_getrecommendedartists( user=self.name, **kargs )

    def recommendedevents( self, **kargs ):
        return self._api.user_getrecommendedevents( user=self.name, **kargs )

    def shouts( self, **kargs ):
        return self._api.user_getshouts( user=self.name, **kargs )

    def shout( self, **kargs ):
        return self._api.user_shout( user=self.name, **kargs )

class Image( Model ):
    
    members = {
        'text' : 'url',
        'image': 'images'
    }

class Library( Model ):

    def __init__(self, user, api=None):
        self.user = user
        self._api = api

    def tracks( self, **kargs ):
        return self._api.library_gettracks( user=self.user.name, **kargs )

    def artists( self, **kargs ):
        return self._api.library_getartists( user=self.user.name, **kargs )

    def albums( self, **kargs ):
        return self._api.library_getalbums( user=self.user.name, **kargs )

    def addartist( self, **kargs ):
        return self._api.library_addartist( **kargs )

    def addtrack( self, **kargs ):
        return self._api.library_addtrack( **kargs )

    def addalbum( self, **kargs ):
        return self._api.library_addalbum( **kargs )

    def removeartist( self, **kargs ):
        return self._api.library_removeartist( **kargs )

    def removetrack( self, **kargs ):
        return self._api.library_removetrack( **kargs )

    def removealbum(self, **kargs ):
        return self._api.library_removealbum( **kargs )

    def removescrobble( self, **kargs ):
        return self._api.library_removescrobble( **kargs )        

class List( Model ):
    
    members = {
        'album' : 'albums',
        'artist' : 'artists',
        'track' : 'tracks',
        'tag' : 'tags',
        'chart' : 'charts',
        'user' : 'users',
        'venue' : 'venues',
        'event' : 'events',
    }
    


class Chart( Model ):

    members = {
        'album' : 'albums',
        'artist' : 'artists',
        'track' : 'tracks',
        'tag' : 'tags',
        'chart' : 'charts',
        'user' : 'users',
        'venue' : 'venues',
        'event' : 'events',    
        'from' : 'start',
        'to' : 'end'
    }

    def hypedartists( self, **kargs ):
        return self._api.chart_gethypedartists( **kargs )

    def hypedtracks( self, **kargs ):
        return self._api.chart_gethypedtracks( **kargs )

    def lovedtracks( self, **kargs ):
        return self._api.chart_getlovedtracks( **kargs )

    def topartists( self, **kargs ):
        return self._api.chart_gettopartists( **kargs )

    def toptags( self, **kargs ):
        return self._api.chart_gettoptags( **kargs )

    def toptracks( self, **kargs ):
        return self._api.chart_gettoptracks( **kargs )

class Registration( Model ):

    members = {
        'text' : 'text'
    }

class Album( Model ):
    
    members = {
        '#text' : 'name',
        'image' : 'images'
    }

    def addtags( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_addtags( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_addtags( artist=self.artist, album=self.name, **kargs )

    def buylinks( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_getbuylinks( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_getbuylinks( artist=self.artist, album=self.name, **kargs )

    def info( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_getinfo( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_getinfo( artist=self.artist, album=self.name, **kargs )

    def shouts( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_getshouts( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_getshouts( artist=self.artist, album=self.name, **kargs )

    def tags( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_gettags( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_gettags( artist=self.artist, album=self.name, **kargs )

    def toptags( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_gettoptags( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_gettoptags( artist=self.artist, album=self.name, **kargs )

    def removetag( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_removetag( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_removetag( artist=self.artist, album=self.name, **kargs )

    def share( self, **kargs ):
        if hasattr(self.artist, 'name'):
            return self._api.album_share( artist=self.artist.name, album=self.name, **kargs )
        else:
            return self._api.album_share( artist=self.artist, album=self.name, **kargs )

    def search( self, **kargs ):
        return self._api.album_search( **kargs )

class Artist( Model ):
    
    members = {
        'text' : 'name',
        'image' : 'images',
        'artist' : 'artists'
    }

    def getinfo( self, **kargs ):
        return self._api.artist_getinfo( artist=self.name, **kargs )

    def addtags( self, **kargs ):
        return self._api.artist_addtags( artist=self.name, **kargs )

    def tags( self, **kargs ):
        return self._api.artist_gettags( artist=self.name, **kargs )

    def removetag( self, **kargs ):
        return self._api.artist_removetag( artist=self.name, **kargs )

    def correction( self, **kargs ):
        return self._api.artist_getcorrection( **kargs )

    def events( self, **kargs ):
        return self._api.artist_getevents( artist=self.name, **kargs )

    def images( self, **kargs ):
        return self._api.artist_getimages( artist=self.name, **kargs )

    def pastevents( self, **kargs ):
        return self._api.artist_getpastevents( artist=self.name, **kargs )

    def similar( self, **kargs ):
        return self._api.artist_getsimilar( artist=self.name, **kargs )

    def shouts( self, **kargs ):
        return self._api.artist_getshouts( artist=self.name, **kargs )

    def topalbums( self, **kargs ):
        return self._api.artist_gettopalbums( artist=self.name, **kargs)

    def toptags( self, **kargs ):
        return self._api.artist_gettoptags( artist=self.name, **kargs)

    def toptracks( self, **kargs ):
        return self._api.artist_gettoptracks( artist=self.name, **kargs)

    def topfans( self, **kargs ):
        return self._api.artist_gettopfans( artist=self.name, **kargs)

    def share( self, **kargs ):
        return self._api.artist_share( artist=self.name, **kargs )

    def search( self, **kargs ):
        return self._api.artist_search( **kargs )

    def shout( self, **kargs ):
        return self._api.artist_shout( artist=self.name, **kargs )

    def podcast( self, **kargs ):
        return self._api.artist_getpodcast( artist=self.name, **kargs )

class Track( Model ):
    
    members = {
        'image' : 'images'
    }

class Tag( Model ):
    
    members = {
        'tag' : 'tags'
    }

class Streamable( Model ):

    members = {
        'text' : 'streamable'
    }

class Attribute( Model ):
    pass

class Affiliation( Model ):

    members = {
        'affiliation' : 'affiliations'
    }

class Price( Model ):
    pass

class Shout( Model ):

    members = {
        'shout' : 'shouts'
    }

class Search( Model ):

    members = {
        'opensearch:Query' : 'query',
        'opensearch:totalResults' : 'total_results',
        'opensearch:startIndex' : 'start_index',
        'opensearch:itemsPerPage' : 'items_per_page',
    }

class Stats( Model ):
    pass

class Correction( Model ):
    pass

class Event( Model ):
    pass

class Venue( Model ):

    def events( self, **kargs ):
        return self._api.venue_getevents( venue=self.id, **kargs )

    def pastevents( self, **kargs ):
        return self._api.venue_getpastevents( venue=self.id, **kargs )

    def search( self, **kargs ):
        return self._api.venue_search( **kargs )

class Location( Model ):
    pass

class Size( Model ):
    
    members = {
        'size' : 'sizes',
        'text' : 'url'
    }

class Votes( Model ):
    pass

class RSS( Model ):
    pass

class Channel( Model ):
    pass

class Date( Model ):
    pass

class Taggings( Model ):
    pass

class ModelFactory( object ):

    user=User
    image=Image
    registered=Registration
    chart=Chart
    album=Album
    artist=Artist
    track=Track
    albums=List
    tracks=List
    artists=List
    tag=Tag
    tags=List
    artisttracks=List
    bannedtracks=List
    weeklychartlist=Chart
    weeklyalbumchart=List
    weeklyartistchart=List
    weeklytrackchart=List
    topartists=List
    topalbums=List
    toptracks=List
    toptags=List
    streamable=Streamable
    attr=Attribute
    attribute=Attribute
    affiliations=Affiliation
    affiliation=Affiliation
    physicals=Affiliation
    downloads=Affiliation
    price=Price
    shout=Shout
    shouts=Shout
    results=Search
    albummatches=List
    artistmatches=List
    trackmatches=List
    venuematches=List
    stats=Stats
    similar=Artist
    corrections=Correction
    correction=Correction
    events=List
    event=Event
    venue=Venue
    location=Location
    images=Image
    sizes=Size
    size=Size
    votes=Votes
    similarartists=List
    topfans=List
    rss=RSS
    channel=Channel
    date=Date
    friends=List
    lovedtracks=List
    neighbours=List
    taggings=Taggings

