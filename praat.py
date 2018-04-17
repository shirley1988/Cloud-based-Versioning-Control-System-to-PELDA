from flask import Flask, render_template, redirect, url_for, request, session, json
from flask_cors import CORS
import pymysql
import subprocess

database_host = 'peldaw2018.mysql.database.azure.com'
database_user = 'myadmin@peldaw2018'
database_password = '1988@Idaho'
database_db = 'peldaw'

conn = pymysql.connect(user = database_user, 
        password = database_password, 
        database = database_db, 
        host = database_host, 
        ssl = {'ssl': {'ca': 'BaltimoreCyberTrustRoot.crt.pem'}})

# Create flask app
app = Flask(__name__)
#app = Flask(__name__, static_url_path='')

# Add CORS headers to allow cross-origin requests
CORS(app)

# login page
@app.route('/')
def login():
	'''
	cursor = conn.cursor()
	sql = "SELECT * FROM user"
	cursor.execute(sql)
	results = cursor.fetchall()
	return render_template('index.html', results=results)
	'''
	return render_template('login.html')

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
	# read the posted values from the UI
	_name = request.form['inputName']
	#_email = request.form['inputEmail']
	_password = request.form['inputPassword']
	print "writing to database"

	cur = conn.cursor()
	#cur.execute("INSERT INTO user('username', 'password') VALUES (_name, _password)")
	sql = """INSERT INTO user('username', 'password') VALUES (_name, _password)"""
	print "wrote to database now!"

	cursor.execute(sql)

	data = cursor.fetchall()
	conn.commit()
    #conn.close()
	'''
	if len(data) is 0:
		conn.commit()
	    return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})
    '''
    
'''
	try:
		cursor.execute(sql)
		conn.commit()
	except:
		conn.rollback()
'''
	

'''
	# validate the received values
	if _name and _password:
		return json.dumps({'html':'<span>All fields good !!</span>'})
	else:
		return json.dumps({'html':'<span>Enter the required fields</span>'})
'''
    
	# insert into MySQL database table



# start the server with the run() method
if __name__ == '__main__':
	app.run(debug=True)


'''
# Import views
from views import * 

# Locations of required files
images_dir = "images/"
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
'''

