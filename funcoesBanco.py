import cx_Oracle   

def openConnection(user, password, dsn):
    #INFORMAR O LOCAL DO INSTANT CLIENT DO ORACLE
    instantClientOracleLocation = r'C:\instantclient_21_3' 
    try:
        cx_Oracle.init_oracle_client(lib_dir=instantClientOracleLocation)
        con = cx_Oracle.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        #con = cx_Oracle.connect('apps/appst3@kar-t-db2:1523/KAREBST3')
    except Exception as err:
        print(f'Falha ao se conectar com o banco: {err}')
    else:
        return con

def closeConnection(con):
    con.close()

def executeQuery(con, sql):
    #SAIR DA FUNÇÃO CASO A CONEXÃO COM O BANCO NÃO ESTEJA ABERTA
    if not con:
        return

    try:
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows #RETORNAR AS LINHAS RESULTANTES DA QUERY
    except cx_Oracle.DatabaseError as err:
        print(f'Erro de Banco: {err}')
    except Exception as err:
        print(f'Erro: {err}')
    finally:
        if cur:
            cur.close()


if __name__ == '__main__':
    con = openConnection('USER', 'PASSWORD', 'HOST:PORT/ORCL')
    rows = executeQuery(con, 'select * from dual')
    print(rows)
    closeConnection(con)


