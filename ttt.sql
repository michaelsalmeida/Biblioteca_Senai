drop database biblioteca;
create database biblioteca;
use biblioteca;

CREATE TABLE cadastro (
pk_matricula int(8) PRIMARY KEY,
nome VARCHAR(200),
curso VARCHAR(80), --
turma VARCHAR(4), ----
data_registro DATE,
hora_registro VARCHAR(5)
);

-- registro de utilizacao
-- fk_matricula
--

/* 1 tabela pra cadastrar o aluno e outra registro de atividade */

create table utilizacao (
pk_registro int (8) PRIMARY KEY AUTO_INCREMENT,
fk_matricula int(8),
mesa_estudos int(4),
usou_computador int(4),
Foreign Key (fk_matricula) REFERENCES cadastro (pk_matricula)
);



CREATE TABLE mesa_estudos(
pk_estudos int(10) PRIMARY KEY auto_increment,
fk_matricula int(8),
data_estudo DATE,
hora_estudo VARCHAR(5),
foreign key (fk_matricula) references cadastro (pk_matricula)
);

CREATE TABLE usar_computador (
id_computador int(10) PRIMARY KEY auto_increment,
fk_matricula int(8),
data_computador DATE,
hora_computador VARCHAR(5),
foreign key (fk_matricula) references cadastro (pk_matricula)
);


create table masterkey (
id_senha int(10) primary key auto_increment,
loginn varchar(50),
senha varchar(50)
);

insert into masterkey values(default, 't', '1');
insert into cadastro values(22224354, 'Michael', 'Técnico em Desenvolvimento de Sistema', '2DT', '2023-02-10', '12:34');
insert into cadastro values(22224355, 'josilene', 'Técnico em Desenvolvimento de Sistema', '1DT', '2023-02-11', '12:50');

insert into utilizacao values (DEFAULT, 22224354, '0', '3');
insert into utilizacao values (DEFAULT, 22224355, '3', '9');

insert into usar_computador values(default, '22224354', '2023-03-14', '13:44');
insert into usar_computador values(default, '22224354', '2023-03-15', '13:00');
insert into usar_computador values(default, '22224354', '2023-03-16', '13:12');


insert into usar_computador values(default, '22224355', '2023-03-22', '13:44');
insert into usar_computador values(default, '22224355', '2023-03-20', '13:00');
insert into usar_computador values(default, '22224355', '2023-03-24', '12:50');
insert into usar_computador values(default, '22224355', '2023-03-25', '13:11');
insert into usar_computador values(default, '22224355', '2023-03-26', '13:15');
insert into usar_computador values(default, '22224355', '2023-03-28', '13:23');
insert into usar_computador values(default, '22224355', '2023-03-30', '13:55');
insert into usar_computador values(default, '22224355', '2023-04-04', '13:22');
insert into usar_computador values(default, '22224355', '2023-03-10', '13:32');

insert into mesa_estudos values(default, '22224355', '2023-04-22', '13:44');
insert into mesa_estudos values(default, '22224355', '2023-04-12', '13:44');
insert into mesa_estudos values(default, '22224355', '2023-05-01', '13:44');


select * from utilizacao;
