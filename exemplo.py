import mysql.connector
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "m4th3u5G!",
    database = "tarefa_python"
)

#criar um requisição
requisicao = conexao.cursor()
#Inserindo Dados
sql = "insert into tb_aluno(nome, cpf, e_mail, telefone) values (%s, %s, %s, %s)"
valores = ("Matheus Griza Estrazulas", "01684788030", "matheusgriza@sou.faccat.br", "51996294733")
requisicao.execute(sql,valores)
#confirmando requisição
conexao.commit()
#Obtendo a chave inserida
print("Novo registro inserido. ID:", requisicao.lastrowid)
#conexao.disconnect()

#Obtendo os resultados 
sql = "select nome, cpf from tb_aluno"
requisicao.execute(sql)
resultado = requisicao.fetchall()

#percorrendo dados
for pessoa in resultado:
   print("ID:", requisicao.lastrowid)
   print(f"Nome:{pessoa[0]}")
   print(f"Cpf:{pessoa[1]}")
conexao.disconnect()

