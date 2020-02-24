# the underscore is convention to make private (but not really)
# but will not be automacially imported
# python will not stop yuo from using it

class _Singleton(object):    
    def __str__(self):
        return """Is it getting better
Or do you feel the same?"""


_instance = None

def Singleton():
    global _instance
    if not _instance:
        _instance = _Singleton()
    return _instance
        