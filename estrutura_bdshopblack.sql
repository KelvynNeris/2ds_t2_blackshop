CREATE DATABASE shopblack;

use shopblack;


CREATE TABLE tb_produtos(
	id_produto varchar(50) primary key,
    nome_produto varchar(50),
    preco int(100),
    imagem_produto varchar(90)
);

CREATE TABLE tb_cliente(
	nome_cliente varchar(80),
    telefone varchar(12),
    cpf varchar(12) primary key,
    endereco varchar(90),
    email varchar(25),
    senha varchar(90)
);



CREATE TABLE tb_carrinho(
	cpf_cliente varchar(12),
    id_produto varchar(50),
	id_carrinho int auto_increment primary key,
	foreign key (cpf_cliente) references tb_cliente(cpf),
    foreign key (id_produto) references tb_produtos(id_produto)
);

ALTER TABLE tb_cliente
ADD INDEX idx_nome_cliente (nome_cliente);

CREATE TABLE tb_comentario(
	nome_usuario varchar(80),
	comentario_usuario varchar(100),
	foreign key (nome_usuario) references tb_cliente(nome_cliente)
);
