Enunciado da tarefa:


Crie um programa em python capaz de gerenciar um cadastro de alunos. As opções do
programa devem ser as seguintes
Incluir um aluno
Alterar um aluno
Deletar um aluno
Listar os alunos
O modelo do banco de dados deve ser o seguinte. Usar obrigatoriamente esses dados de
acesso, banco de dados e tabela

create database tarefa_python;
create user tarefa_python identified by '12345';
grant all on tarefa_python.* to tarefa_python;
use tarefa_python;
create table tb_aluno(
aluno_id integer auto_increment primary key,
nome varchar(45) not null,
cpf varchar(11) not null,
e_mail varchar(60) not null,
telefone varchar(11) not null
);
