class MyClass:

    def get(self, *args):
        return self

    def name(self, *args):
        return self

def MyFunction():
    pass

def option(key, desc, handler):
    print(key, desc, handler, type(handler))

def command(key, desc, handler):
    print(key, desc, handler, type(handler))
    def handle():
        print('my')

def route(*args):
    return MyClass()

# Options
option('--i', 'Use application in interactive mode', MyClass)
option('--h', 'Display the application help window', MyClass)

# Commands
command('make:folder', 'Create a new folder', MyFunction)

# Routes
route().get('/', 'MyController@index').name('hello')