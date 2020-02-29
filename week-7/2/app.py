from cliff import Application
from commands import DrawShapeFile, GenerateShapeFile

Application({
    'name': 'Shape Generator/Drawer',
    'description': 'A program to generate shape files and draw shapes in the files',
    'version': '1.0.0'
}).registerCommands([
    DrawShapeFile,
    GenerateShapeFile,
]).run()
