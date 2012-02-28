import inspect

class Model( object ):

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
                k = k.lstrip( '#' ).lstrip( '@' )
                try:
                    model = getattr( ModelFactory, k )
                    if isinstance(v, list):
                        results = []
                        for item in v:
                            results.append( model.parse( api, item) )
                        setattr( obj, k, results )
                    else:
                        setattr( obj, k, model.parse( api, v ) )
                except AttributeError:
                    setattr( obj, k, v )
        else:
            return json
        return obj  


class User( Model ):

    def get_info(self, **kargs):
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

class Image(Model):
    pass

class Chart(Model):
    @classmethod
    def parse(cls, api, json):
        obj = cls(api)
        if hasattr(json, 'items'):
            for k, v in json.items():
                k = k.lstrip('#').lstrip('@')
                try:
                    model = getattr(ModelFactory, k)
                    if isinstance(v, list):
                        results = []
                        for item in v:
                            results.append( model.parse( api, item) )
                        setattr( obj, k, results )
                    else:
                        if k == 'from':
                            setattr(obj, 'start', model.parse(api, v))
                        elif k == 'to':
                            setattr(obj, 'end', model.parse(api, v))
                        else:
                            setattr(obj, k, model.parse(api, v))
                except AttributeError:
                    setattr( obj, k, v )
        else:
            return json
        return obj    

class ModelFactory( object ):

    user=User
    image=Image
    chart=Chart
    weeklychartlist=Chart