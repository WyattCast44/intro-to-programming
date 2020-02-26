# Standard Libraries
from options import Version
import os
import sys

# Other Libraries
from tinydb import TinyDB, Query

# Init the database
db = TinyDB('db.json')
