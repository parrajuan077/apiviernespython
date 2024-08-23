from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import engine

#conexion a la BD
#nombrebd
dataBaseName ="gestinbd"



#usuariobd
userName="root"

#contraseña del usuario
userPassword=""

#servidor de localhost
serverConnection="localhost"

#puerto de conexion
conexionPort="3306"

#creando la conexion
connectionToDatabase=f"mysql+mysqlconnector://{userName}:{userPassword}@{serverConnection}:{conexionPort}/{dataBaseName}"


engine = create_engine(connectionToDatabase)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)