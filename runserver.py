"""
This script runs the FlaskWebProject1 application using a development server.
"""

#from os import environ
#from FlaskWebProject1 import app

#if __name__ == '__main__':
 #   HOST = environ.get('SERVER_HOST', 'localhost')
  #  try:
    #     PORT = int(environ.get('SERVER_PORT', '5555'))
  #  except ValueError:
   #     PORT = 5555
   # app.run(HOST, PORT)

import os
from HelloFlask import app    # Imports the code from HelloFlask/__init__.py

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)