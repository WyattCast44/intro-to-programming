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

    def __init__(self, configKey):
        self.key = configKey
        print(self.key)


class RepoServiceProvider:

    def __init__(self, cont):
        self.container = cont

    def register(self):
        return Repo(self.container.resolve('key'))


c = Container()

c.bind('key', 'wyatt')
c.bind(Repo, RepoServiceProvider)

print(c.resolve(Repo))
