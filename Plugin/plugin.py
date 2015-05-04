class Plugin:
    def getId( self, plugin ):
        return plugin().newID()

class IDInterface:
    def newID( self ):
        raise NotImplementedError( "this method has not been implemented" )

class IDCounter(IDInterface):
    objectId = 0
    def newID( self ):
        IDCounter.objectId = 1 + IDCounter.objectId
        return IDCounter.objectId

class IDGenerator(IDInterface):
    objectId = 1
    def newID( self ):
        IDGenerator.objectId = IDGenerator.objectId * 2
        return IDGenerator.objectId

class Item:
    def __init__(self, id):
        self.id = id

def main():
    _print("\nGet some id's")
    _print("\nusing counter plugin:")
    _print(str(Plugin().getId(IDCounter)))
    _print(str(Plugin().getId(IDCounter)))
    _print(str(Plugin().getId(IDCounter)))
    _print(str(Plugin().getId(IDCounter)))
    _print(str(Plugin().getId(IDCounter)))
    _print(str(Plugin().getId(IDCounter)))
    _print("\nusing generator plugin:")
    _print(str(Plugin().getId(IDGenerator)))
    _print(str(Plugin().getId(IDGenerator)))
    _print(str(Plugin().getId(IDGenerator)))
    _print(str(Plugin().getId(IDGenerator)))
    _print(str(Plugin().getId(IDGenerator)))
    _print(str(Plugin().getId(IDGenerator)))

# shouldn't matter which version of python it runs
def _print(string):
    try:
        print string
    except SyntaxError:
        print(string)

if __name__ == "__main__": main()
