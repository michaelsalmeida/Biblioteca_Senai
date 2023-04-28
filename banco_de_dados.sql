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
data_livro DATE,
hora_livro VARCHAR(5),
foreign key (fk_matricula) references cadastro (pk_matricula)
);

CREATE TABLE usar_computador (
pk_computador int(10) PRIMARY KEY auto_increment,
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
