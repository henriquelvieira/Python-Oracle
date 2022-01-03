import os
from dotenv import load_dotenv
from funcoesBanco import openConnection, closeConnection, executeQuery


try:
    load_dotenv() #CARREGAR AS VÁRIAVEIS DE AMBIENTE DO ARQUIVO .ENV
    user, password, dsn = os.getenv('USERNAME'), os.getenv('PASSWORD'), os.getenv('DSN')
except Exception as err:
    print(f'Falha ao carregar as váriaveis de ambiente. Erro: {err}')

try:
    con = openConnection(user, password, dsn) #CONEXÃO COM O BANCO
except Exception as err:
    print(err)
    

sql = '''SELECT 'TESTE 1' FROM DUAL
         UNION 
         SELECT 'TESTE 2' FROM DUAL''';
rows = executeQuery(con, sql) #EXECUÇÃO DA QUERY

listDados = []
for row in rows:
    listDados.append(row[0]) #CREATION_DATE


closeConnection(con) #ENCERRAR A CONEXÃO COM O BANCO