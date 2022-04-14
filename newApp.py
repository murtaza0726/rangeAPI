import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL, MySQLdb

#from flaskext.mysql import mysql
#import mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'be32eb4083c64f'
app.config['MYSQL_PASSWORD'] = 'b41f6242'
app.config['MYSQL_DB'] = 'heroku_16c301709b71772'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
  
 
@app.route('/api/client/v0.1/api/range') 
def get_user():
    #cursor = None;
    City = request.args.get('City')
    Country = request.args.get('Country')
    if City:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM ProjectDP WHERE City=%s AND Country=%s", (City,Country))
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        cursor.close() 
    return resp
 
if __name__ == "__main__":
    app.run(debug=True)