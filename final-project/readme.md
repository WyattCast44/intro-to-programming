# Escape From Mars

Escape from Mars is a text adventure game, built in python. 

## Requirements

You must have TinyDB installed, you can install it using the command below:

```bash
pip install tinydb
```

## Ideas

- Main Player: Mark Watney
- Main Player Resource: oxygen
- Player Trinkets: Oxygen bottles

- Enemy Name:
- Enemy Resource: 

- https://www.php2python.com/wiki/function.require-once/

## Storyline

- You're name is Mark Watney and you the only human on Mars. 
- Your mission is to cross Schiaparelli and 

# Console Component

## Creating your first CLI App

```python
from console import Application

app = Application()

app.run()
```

Yup that's it! But your application doesn't actually do anything at this point.

You can now start adding options and commands to the app in order to make it useful.

## Options

Commands are simple python classes with two mandatory methods, the `__init__` method and the `handle` method. The init method should accept the application instance and can be used to access/set the application state, and access the console helpers.

Any arguments passed to the application will first be ran thru a list of the options, so any commands with the same signature as a option will never be ran.

Options are registered with the app using the `registerOptions` method, as the example below shows.

```python
from console import Application

# Options
from options import Help, Version

app = Application({
    'name': 'My App',
    'version': '0.1.0',
    'description': 'My super-useful applications'
})

app.registerOptions([
    Help,
    Version
])
```

## Commands

Commands are simple python classes with two mandatory methods, the `__init__` method and the `handle` method. The init method should accept the application instance and can be used to access/set the application state, and access the console helpers.

Options are registered with the app using the `registerCommands` method, as the example below shows.

```python
from console import Application

# Commands
from commands import MakeFile

app = Application({
    'name': 'My App',
    'version': '0.1.0',
    'description': 'My super-useful applications'
})

app.registerCommands([
    MakeFile,
])
```