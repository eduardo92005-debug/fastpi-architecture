from dependencies.env_dependencies import *

engine = create_engine("mysql+pymysql://root:root@/carros?charset=utf8mb4", echo=True)
Base = declarative_base()
#Para fazer consultar tem que criar uma sessao
Session = sessionmaker(bind=engine)
session = Session()