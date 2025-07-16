import sqlite3
import utils_json
from sqlite3 import Error
sqlite3=ela e o banco de dados nativa do python que auxilia para questao de banco de dados 
util_json=ela e a parte aonde tento exportar o arquivo do json , para outra pagina do codigo conseguir exportar arquivo do json 

def create_connection(db_file):
função que deseja criar a conexão com o banco de dados na parte do try/execpt,para garantir caso houver o erro na conexao isso mostrando no programa que houve o erro.

def create_tables(conn):
aqui definem os principais tabelas do sistemas
users=significa o usuarios seja nome ,sobrenome usuario e o email.
addresses=armazena os enderecos relacionados ao usuarios

def insert_user(conn, user):
recebe o tupla de dados usuario inserindo o banco 

def insert_address(conn, address):
primeiro busca o usuarios e os enderecos dele tambem foi usado a base para exportacao do json 

def main():
aonde executa todo o sistemas 
create_tables e aonde garantem que as tabelas existem 
inserindo 3 usuarios
associa os 4 enderecoes partindo a curitiba e ate o ciudad del este 
conn.close()
aonde a execucao finaliza, e fecha o banco de dados e fecham a conexao,e os recursos dos sistemas. 
