from flask import Flask
from flask.ext.mysqldb import MySQL
import os


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DB')

mysql.init_app(app)


@app.route('/')
def hello_world():
	cursor = mysql.connect().cursor()
	# test sql statement
	sql = 'SELECT * FROM authors LIMIT 1'
	cursor.execute(sql)
	data=cursor.fetchall()
	
	for f in data :
		theID = f[0]
		theName = f[1]
		theEmail = f[2]
	
	html = str(theID) + ", " + theName + ", " + theEmail
	html += html + '<br> Hello, World!'
	
	return html
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)