from sqlalchemy import Table, Column   
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import engine, meta_data

riterios_aceptabilidad = Table("datos_entrega", meta_data,
              Column("id", Integer, primary_key=True),
              Column("cantidad_de_muestra", Boolean, nullable=False),
              Column("preservacion", Boolean, nullable=False),
              Column("empaque", Boolean, nullable=False),
              Column("embalaje", Boolean, nullable=False),
              Column("identificacion", Boolean, nullable=False),
              Column("observaciones", String(2048), nullable=False))

meta_data.create_all(engine)