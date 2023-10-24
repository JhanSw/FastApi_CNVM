from sqlalchemy import Table, Column   
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import engine, meta_data

cliente = Table("cliente", meta_data, 
              Column("id", Integer, primary_key=True),
              Column("cliente", String(255), nullable=False),
              Column("nit", String(255), nullable=False),
              Column("solicitante", String(255), nullable=False),
              Column("cargo", String(255), nullable=False),
              Column("direccion", String(255), nullable=False),
              Column("municipio", String(255), nullable=False),
              Column("telefono", String(255), nullable=False),
              Column("fax", String(255), nullable=False),
              Column("consecutivo", String(255), nullable=False),
              Column("observaciones", String(1024), nullable=False))

meta_data.create_all(engine)