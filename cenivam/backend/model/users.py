from sqlalchemy import Table, Column   
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

users = Table("users", meta_data, 
              Column("id", Integer, primary_key=True),
              Column("nombre_usuario", String(255), nullable=False),
              Column("numero_doc_usuario", Integer, nullable=False),
              Column("usuario", String(255), nullable=False),
              Column("contrasenia_usuario", String(255), nullable=False))

meta_data.create_all(engine)