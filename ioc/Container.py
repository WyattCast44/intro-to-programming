class Container:

    registry = {}

    def bind(self, key, value):
        if type(value) == type:
            # class
            self.registry[key] = value(self).register()
        elif callable(value):
            # func
            self.registry[key] = value(self)
        else:
            self.registry[key] = value
        return

    def resolve(self, key):
        if key in self.registry:
            return self.registry[key]
        else:
            return None


class Repo:

    def __init__(self, configKey, name):
        self.key = configKey
        print(self.key, name)


class RepoServiceProvider:

    def __init__(self, cont):
        self.container = cont

    def register(self):
        return Repo(self.container.resolve('key'), self.container.resolve('name'))


c = Container()

c.bind('key', 'wyatt')
c.bind('name', 'wyatt-is-cool')
c.bind(Repo, RepoServiceProvider)

print(c.resolve(Repo))
