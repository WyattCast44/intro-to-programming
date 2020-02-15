class Application(ConsoleOutput, ConsoleInput):

    config = {}

    def __init__(self, config):

        self.config = config

        self.name = config.get('name')
        self.version = config.get('version')
        
        self.main()

    def main(self):
        self.success(f'\n{self.name}\nv{self.version}')

# app = Application({
#     'name': 'My Console App',
#     'version': '0.1.0',
# })