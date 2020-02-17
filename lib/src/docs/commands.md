# Commands

Commands are a central part of your application. They help you encapsulate your app logic in sensible groups of code that can be composed and reused.

## Registering Commands

To register commands with the application, you have two options:

- You can register a class based command
- You can register a function based command

## Built-In Commands

CLIHero has several built in commands that you can use in your app if you would like.

#### `MakeCommand` Command

The `MakeCommand` command is a used to 

## Setting a Default Command

For some applications it makes sense to have a default command that runds whenever the application is ran with no commands or options passed.

CLIHero makes this very easy to do, there is two steps:

1. Register the command using any of the supported methods
2. Call `setDefaultCommand` and pass in either
    - A string that is the signature of the command 
    - Or, a class that is the command

```python
from CLIHero import Application
from commands import DefaultCommand

Application({
    'name': 'My App',
    'description': 'A CLI with a default command',
    'version': '1.0.0'
}).registerCommands([
    DefaultCommand,
]).setDefaultCommand(DefaultCommand).run()
```
CLIHero