from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:root@localhost:3306/cenivam")
#orden: usuario,contraseña,dirección de localhost, nombre de la base de datos


meta_data = MetaData()
