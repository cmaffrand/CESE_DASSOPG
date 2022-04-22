from flask import Flask, request
import sqlite3
from flask import g
from ControllerDevices import ControllerDevices

app = Flask(__name__)

app = Flask(__name__)

#************** Manejo de DB ****************************
DATABASE = 'devices.db3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#________________________________________________________


@app.route('/devices')
def devices():
	controller = ControllerDevices(app,request,get_db())
	return controller.getAll()

@app.route('/devices/<devId>', methods=['PUT'])
def setDevice(devId):
    value = request.args.get('value', '0')
    controller = ControllerDevices(app,request,get_db())
    return controller.setSome(devId,value)

@app.route('/log')
def log():
    page = request.args.get('page', '0')
    size = request.args.get('size', '10')
    page = str(int(page) * int(size))
    controller = ControllerDevices(app,request,get_db())
    return controller.getSome(page,size)

if __name__ == '__main__':
	app.debug = True
	app.run()
