import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

NM = os.getenv('USER_NAME')
PD = os.getenv('PASSWD')
KEY = os.getenv('KEY')
user = os.getenv('user')
host = os.getenv('host')

res = f'{user};{host};'
print(res)