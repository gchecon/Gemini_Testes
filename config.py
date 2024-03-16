from dotenv import load_dotenv
import os

load_dotenv()

BD_SENHA = os.getenv("BD_SENHA")
BD_USER = os.getenv("BD_USER")
BD_NOME = os.getenv("BD_NOME")
# IP_BD = os.getenv("IP_BD")
IP_BD = 'localhost'
PORT_BD = os.getenv('PORT_BD')

STR_CONN = "postgresql://" + BD_USER + ":" + BD_SENHA + '@' + IP_BD + ':' + PORT_BD + '/' + BD_NOME