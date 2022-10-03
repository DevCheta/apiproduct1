#import os
import sqlite3
from flask import Flask, request, jsonify
#from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
#UPLOAD_FOLDER = '/path/to/the/uploads'
#application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///productdb.db"
application.config["SECRET_KEY"] = "my super secret key"

db = SQLAlchemy(application)

#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

"""def allowed_file(filename):
    return filetype in allowed_extensions"""

class Products (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #avatar = db.Column(db.String(20), nullable=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer,  nullable=False)
    category = db.Column(db.String(200))
    description = db.Column(db.String(200))
    #accountName = db.Column(db.String(200))
    #accountNumber = db.Column(db.Integer)
    #bankName = db.Column(db.String(200))

    
    def __init__(self, name, price, category, description):
        #self.avatar = avatar
        self.name = name
        self.price = price
        self.category = category
        self.description = description
        """self.accountName = accountName
        self.accountNumber = accountNumber
        self.bankName = bankName"""
        
    def __repr__(self):
        return '<Product %d>' % self.id


@application.route("/", methods = ['GET'])
def index():
     get_products = Products.query.all()
     return jsonify({"products": get_products})
     
     
"""@application.route('/products', methods = ['POST'])
def create_author():
    data = request.get_json()
    
    result = {
        "name" : data["name"],
        "price" : data["price"],
        "category" : data["category"],
        "description" : data["description"]
    }
    
    db.session.add(result)
    db.session.commit()
     
    return jsonify({"product": result}), 201
    
@application.route('/products/<id>', methods = ['GET'])
def get_product_by_id(id):
    get_product = Products.query.get(id)
    if not get_product:
  
        return jsonify({"message" : "product does not exist"}), 404
        
    return jsonify({"product": get_product})
    
@application.route('/products/<id>', methods = ['PUT'])
def update_product_by_id(id):
    data = request.get_json()
    get_product = Products.query.get(id)
    if data.get('name'):
        get_product.name = data['name']
    if data.get('price'):
        get_product.price = data['price']
    if data.get("category"):
        get_product.category = data["category"]
    if data.get("description"):
        get_product.description = data["description"]
    db.session.add(get_product)
    db.session.commit()
    return jsonify({"product": get_product})
    
@application.route('/products/<id>', methods = ['DELETE'])
def delete_product_by_id(id):
    get_product = Products.query.get(id)
    db.session.delete(get_author)
    db.session.commit()
    return " ", 204
    
@application.route('/avatar/<id>', methods=['POST'])
def upsert_product_avatar(id):
    try:
        file = request.files['avatar']
        get_product = Products.query.get(id)
        if file and allowed_file(file.content_type):
            filename = secure_filename(file.filename)
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
        get_product.avatar = url_for('uploaded_file', filename=filename, _external=True)
        db.session.add(get_product)
        db.session.commit()
        return "SUCCESS_200", jsonify({"product": get_product})
    except Exception as e:
        #print (e)
        return "INVALID INPUT 422
         
@application.route("/products/<name>", methods=["GET"])
def search_products(name):
    get_product = Products.query.filter_by(name=name).first()
    if not get_product:
        return jsonify({"message" : "product not found"})
    
    return jsonify({"product" : get_product})
    
@application.route("/products/<category>", methods=["GET"])
def search_category(category):
    get_product = Products.query.filter_by(category=category).first()
    if not get_product:
        return jsonify({"message" : "product not found"})
    
    return jsonify({"product" : get_product})
    
@application.route("/payments", methods=["POST"])
def payment_info():
    data = request.get_json()
    
    result = {
        "accountName" : data["accountName"],
        "accountNumber" : data["accountNumber"],
        "bankName" : data["bankName"]
    }
    
    db.session.add(result)
    db.session.commit()
     
    return jsonify({"product": result}), 201"""
    
if __name__ == "__main__":
    #application = create_app()
    application.run(debug=True)
