from sqlalchemy import Table, Column   
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import engine, meta_data

inspeccion = Table("inspeccion", meta_data,
              Column("id", Integer, primary_key=True),
              Column("analisis_o_ensayo", String(255), nullable=False),
              Column("analista_s", String(255), nullable=False),
              Column("equipo_usado", String(255), nullable=False),
              Column("preparacion_muestra", String(1024), nullable=False),
              Column("muestra_o_matriz", Boolean, nullable=False),
              Column("observaciones", String(2048), nullable=False),
              Column("aceptacion_muestra", Boolean, nullable=False),
              Column("motivo_rechazo", String(1024), nullable=False),
              Column("fecha_rechazo", String(1024), nullable=False),
              Column("respuesta_cliente", String(1024), nullable=False),
              Column("fecha de respuesta", String(1024), nullable=False),
              Column("comentario", String(1024), nullable=False))
                          
meta_data.create_all(engine)