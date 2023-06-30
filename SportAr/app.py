from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user:password@localhost/proyecto'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/sportar'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# # defino la tabla
# class Producto(db.Model):   # la clase Producto hereda de db.Model    
#     id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
#     nombre=db.Column(db.String(100))
#     precio=db.Column(db.Integer)
#     stock=db.Column(db.Integer)
#     imagen=db.Column(db.String(400))
#     def __init__(self,nombre,precio,stock,imagen):   #crea el  constructor de la clase
#         self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
#         self.precio=precio
#         self.stock=stock
#         self.imagen=imagen

#     #  si hay que crear mas tablas , se hace aqui

# ---- SportAr -----------------------------------------------------
class Articulo(db.Model):
    id=db.Column(db.Integer, primary_key=True)  
    titulo=db.Column(db.String(100))
    descripcion=db.Column(db.String(100))
    category=db.Column(db.String(20))
    subcategory=db.Column(db.String(20))
    precio=db.Column(db.Integer)
    cantidad=db.Column(db.Integer)
    image=db.Column(db.String(400))
    cuotas=db.Column(db.Integer)
    descuento=db.Column(db.Integer)

    def __init__(self,titulo,descripcion,category,subcategory,precio,cantidad,image,cuotas,descuento):
        self.titulo=titulo
        self.descripcion=descripcion
        self.category=category
        self.subcategory=subcategory
        self.precio=precio
        self.cantidad=cantidad
        self.image=image
        self.cuotas=cuotas
        self.descuento=descuento        
# ---- SportAr -----------------------------------------------------



with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************


# class ProductoSchema(ma.Schema):
#     class Meta:
#         fields=('id','nombre','precio','stock','imagen')



# producto_schema=ProductoSchema()            # El objeto producto_schema es para traer un producto
# productos_schema=ProductoSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

#INSERT INTO `articulo`( `titulo`, `descripcion`, `category`, `subcategory`, `precio`, `cantidad`, `image`, `cuotas`, `descuento`) VALUES ('Remera New Balance','Dry Fit Color Verde','Indumentaria','Remeras',3500,7,'../img/remera1.jpg',3,30);
#INSERT INTO `articulo`( `titulo`, `descripcion`, `category`, `subcategory`, `precio`, `cantidad`, `image`, `cuotas`, `descuento`) VALUES ('Remera Assys','Dry Fit Degrade Negro','Indumentaria','Remeras',3500,5,'../img/remera2.jpg',0,0);

# ---- SportAr -----------------------------------------------------
class ArticuloSchema(ma.Schema):
    class Meta:
        fields=('id','titulo','descripcion','category','subcategory','precio','cantidad','image','cuotas','descuento')

articulo_schema=ArticuloSchema()                # El objeto articulo_schema es para traer un articulo
articulos_schema=ArticuloSchema(many=True)      # El objeto articulos_schema es para traer multiples registros de articulo


# crea los endpoint o rutas (json)
@app.route('/articulos',methods=['GET'])
def get_Articulos():
    all_articulos=Articulo.query.all()              # el metodo query.all() lo hereda de db.Model
    result=articulos_schema.dump(all_articulos)     # el metodo dump() lo hereda de ma.schema y
                                                    # trae todos los registros de la tabla
    return jsonify(result)                          # retorna un JSON de todos los articulos de la tabla


@app.route('/articulos/<id>',methods=['GET'])
def get_articulo(id):
    articulo=Articulo.query.get(id)
    return articulo_schema.jsonify(articulo)        # retorna el JSON de un articulo recibido como parametro


@app.route('/articulos/<id>',methods=['DELETE'])
def delete_articulo(id):
    articulo=Articulo.query.get(id)
    db.session.delete(articulo)
    db.session.commit()
    return articulo_schema.jsonify(articulo)        # me devuelve un json con el registro eliminado


@app.route('/articulos', methods=['POST'])          # crea ruta o endpoint
def create_articulo():
    #print(request.json)  # request.json contiene el json que envio el cliente
    titulo=request.json['titulo']
    descripcion=request.json['descripcion']
    category=request.json['category']
    subcategory=request.json['subcategory']
    precio=request.json['precio']
    cantidad=request.json['cantidad']
    image=request.json['image']
    cuotas=request.json['cuotas']
    descuento=request.json['descuento']

    new_articulo=Articulo(titulo,descripcion,category,subcategory,precio,cantidad,image,cuotas,descuento)
    db.session.add(new_articulo)
    db.session.commit()
    return articulo_schema.jsonify(new_articulo)


@app.route('/articulos/<id>' ,methods=['PUT'])
def update_articulo(id):
    articulo=Articulo.query.get(id)
 
    articulo.titulo=request.json['titulo']
    articulo.descripcion=request.json['descripcion']
    articulo.category=request.json['category']
    articulo.subcategory=request.json['subcategory']
    articulo.precio=request.json['precio']
    articulo.cantidad=request.json['cantidad']
    articulo.image=request.json['image']
    articulo.cuotas=request.json['cuotas']
    articulo.descuento=request.json['descuento']

    db.session.commit()
    return articulo_schema.jsonify(articulo)

# ---- SportAr -----------------------------------------------------


# # crea los endpoint o rutas (json)
# @app.route('/productos',methods=['GET'])
# def get_Productos():
#     all_productos=Producto.query.all()         # el metodo query.all() lo hereda de db.Model
#     result=productos_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
#                                                  # trae todos los registros de la tabla
#     return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




# @app.route('/productos/<id>',methods=['GET'])
# def get_producto(id):
#     producto=Producto.query.get(id)
#     return producto_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro




# @app.route('/productos/<id>',methods=['DELETE'])
# def delete_producto(id):
#     producto=Producto.query.get(id)
#     db.session.delete(producto)
#     db.session.commit()
#     return producto_schema.jsonify(producto)   # me devuelve un json con el registro eliminado


# @app.route('/productos', methods=['POST']) # crea ruta o endpoint
# def create_producto():
#     #print(request.json)  # request.json contiene el json que envio el cliente
#     nombre=request.json['nombre']
#     precio=request.json['precio']
#     stock=request.json['stock']
#     imagen=request.json['imagen']
#     new_producto=Producto(nombre,precio,stock,imagen)
#     db.session.add(new_producto)
#     db.session.commit()
#     return producto_schema.jsonify(new_producto)


# @app.route('/productos/<id>' ,methods=['PUT'])
# def update_producto(id):
#     producto=Producto.query.get(id)
 
#     producto.nombre=request.json['nombre']
#     producto.precio=request.json['precio']
#     producto.stock=request.json['stock']
#     producto.imagen=request.json['imagen']


#     db.session.commit()
#     return producto_schema.jsonify(producto)
 


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000