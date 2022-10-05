create database taquigrafo_virtual;
use taquigrafo_virtual;
create table cliente (
	id_cliente int auto_increment unique,
	correo varchar(30),
    contrasena varchar(30),
    nombre varchar(30),
    ape_paterno varchar(30),
    ape_materno varchar(30),
    primary key(id_cliente)
);

create table caso(
	id_caso int auto_increment unique,
    titulo varchar(40),
    descripcion varchar(100),
    fecha_inicio date,
    fecha_fin date null,
    estado varchar(10),
    id_cliente int not null,
    primary key (id_caso),
    foreign key (id_cliente) references cliente(id_cliente)
);

create table sesion(
	id_sesion int auto_increment unique,
    fecha date,
    descripcion varchar(100),
    id_caso int not null,
    primary key (id_sesion),
    foreign key (id_caso) references caso(id_caso)
);

create table participante(
	id_participante int auto_increment unique,
    nombre varchar(30),
    ape_paterno varchar(30),
    ape_materno varchar(30),
    tipo varchar(20),
    id_sesion int not null,
    primary key (id_participante),
    foreign key (id_sesion) references sesion(id_sesion)
);

create table declaracion(
	id_declaracion int auto_increment unique,
    titulo varchar(30),
    tipo varchar(20),
    declaracion text,
    id_participante int not null,
    primary key (id_declaracion),
    foreign key (id_participante) references participante(id_participante)
);

insert into cliente ( correo, contrasena,nombre,ape_paterno,ape_materno)
            values ( 'jsanchezchi@','123','john','sanchez','chilo');

insert into cliente ( correo, contrasena,nombre,ape_paterno,ape_materno)
            values ( 'gerson@','456','gerson','anchez','chilo');


insert into caso (titulo, descripcion, fecha_inicio, estado )
            values ('Separacion de terrenos','Dos familias estan peleando por quien se queda el terreno',curdate(),'Activo',1);

SELECT * from caso;
