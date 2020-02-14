from framer import Application, tap

from options import Help, Version
from commands import MakeDir, MakeFile

tap(Application({
    'name': 'Tapped Console App',
    'description': 'Example of the tap() function',
    'version': '1.0.2'
})).registerCommands([
    MakeDir, 
    MakeFile, 
]).registerOptions([
    Help, 
    Version
]).run()