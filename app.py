from flask import Flask,request
import database
app = Flask(__name__)
create = database.Create()
read = database.Read()
update = database.Update()
delete = database.Delete()
query_processor = database.QueryProcessor(create,read,update,delete)

@app.route('/')
def hello_world():
    return """Welcome to the sample CRUD application!"""

@app.route('/create',methods = ['POST'])
def create():
    name = request.form['name']
    price = request.form['price']
    year = request.form['year']
    label = request.form['label']
    return str(query_processor.create_one((name,price,year,label)))

@app.route('/update_year',methods = ['POST'])
def update_year():
    id = request.form['id']
    year = request.form['year']
    return str(query_processor.update_year((year,id)))

@app.route('/read_all',methods = ['GET'])
def read_all():
    return str(query_processor.read_all())

@app.route('/delete_one',methods = ['POST'])
def delete_one():
    id = request.form['id']
    return str(query_processor.delete_one((id)))