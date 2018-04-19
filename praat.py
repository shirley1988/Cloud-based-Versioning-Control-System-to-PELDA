from flask import Flask, render_template, redirect, url_for, request, session, json
from flask_cors import CORS
import string
import pymysql
import subprocess
import bcrypt

app = Flask(__name__)
#app = Flask(__name__, static_url_path='')

# Add CORS headers to allow cross-origin requests
CORS(app)

# Import views
from views import * 

# Locations of required files
_images_dir = "images/"
_scripts_dir = "scripts/"
_sounds_dir = "sounds/"
_eaf_dir = "eaf/"
# _linkElanPraat_dir = "combined/"


# Run script 'scriptName' with the provided parameters
def runScript(scriptName, args):
   praatExec = ["/Applications/Praat.app/Contents/MacOS/Praat", "--run", "--no-pref-files", scriptName];
   praatExec.extend(args)
   #print str(praatExec)
   output = subprocess.check_output(praatExec);
   #print "output from praat.py is: "+str(output)
   return output

# Run server on port 5000
if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.run(threaded=True, debug=True)


