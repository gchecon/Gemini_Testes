from dotenv import load_dotenv
import os

load_dotenv()

BD_SENHA = os.getenv("BD_SENHA")
BD_USER = os.getenv("BD_USER")
BD_NOME = os.getenv("BD_NOME")