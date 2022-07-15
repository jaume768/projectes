CREATE DATABASE marvel_mcoc;

use marvel_mcoc;

create table personatge(
    idPersonatge int(255) not null auto_increment,
    Nom varchar(30) not null,
    primary key(idPersonatge)
);

create table caracteristiques(
    idCaracte int(255) not null auto_increment,
    stars VARCHAR(20) not null,
    hp int(255) not null,
    atk int(255) not null,
    rango VARCHAR(20) not null,
    lvl int(255) not null,
    clase VARCHAR(100) not null,
    primary key(idCaracte),
    FOREIGN KEY (idCaracte) REFERENCES personatge(idPersonatge)
);

create table SuperAtaque(
    idSuperAtaque int(255) not null auto_increment,
    TipoSuper text not null,
    DejaDesventajas boolean not null,
    primary key(idSuperAtaque)
);

create table desventajas(
    idDesventajas int(255) not null auto_increment,
    Nombre varchar(100) not null,
    descripcion text not null,
    primary key(idDesventajas)
);

create table sinergias(
    idSinergias int(255) not null auto_increment,
    Personatges varchar(100) not null,
    Descripcio text not null,
    primary key(idSinergias)
);

create table descripcio_pers(
    idDescripcio int(255) not null auto_increment,
    descripcioPers text,
    primary key(idDescripcio),
    FOREIGN KEY (idDescripcio) REFERENCES personatge(idPersonatge)
);

create table pasiva(
    idPasiva int(255) not null auto_increment,
    descripcioPasiva text,
    primary key(idPasiva),
    FOREIGN KEY (idPasiva) REFERENCES personatge(idPersonatge)
);


/* tablas intermedias */
create table superPers(
    idPersonatge int(255),
    idSuperAtaque int(255),
    FOREIGN KEY (idPersonatge) REFERENCES personatge(idPersonatge),
    FOREIGN KEY (idSuperAtaque) REFERENCES SuperAtaque(idSuperAtaque)
);

create table superDesventajas(
    idDesventajas int(255),
    idSuperAtaque int(255),
    FOREIGN KEY (idDesventajas) REFERENCES desventajas(idDesventajas),
    FOREIGN KEY (idSuperAtaque) REFERENCES SuperAtaque(idSuperAtaque) 
);

create table sinPers(
    idSinergias int(255),
    idPersonatge int(255),
    FOREIGN KEY (idPersonatge) REFERENCES personatge(idPersonatge),
    FOREIGN KEY (idSinergias) REFERENCES sinergias(idSinergias) 
);

insert into personatge(Nom)
values ("Hercules"),("Capitana_Marvel"),("Warlock");

insert into caracteristiques(stars,hp,atk,rango,lvl,clase)
VALUES ("4/6",16463,1461,"5/5",50,"Cosmico"),("4/6",16651,1213,"5/5",50,"Mistico"),("4/6",15407,1213,"5/5",50,"Tecno");

insert into descripcio_pers(descripcioPers)
values ("Nacido en la antigua Grecia, Hercules es un semidios nacido de Zeus, el rey de los dioses olimpicos, y Alcmena, una mujer de Tebas. Hercules fue cuidado por su madrastra Hera, reina de los dioses olimpicos, y recibio sus bendiciones. Estas bendiciones elevaron aun mas su fisiologia de semidios a alturas casi divinas, brindandole una inmensa fuerza, resistencia, inmortalidad y casi invulnerabilidad."),("Despues de un aterrizaje forzoso en la Tierra sin ningun recuerdo de su pasado, la piloto de la Fuerza Aerea, Carol Danvers, descubre lentamente los eventos de su pasado. Rescatada por los Kree y renacida como una noble guerrera Kree, Carol aprende a controlar sus nuevos poderes bajo la guia de Mar-Vell, comandante de Starforce. Cuando se encuentra de nuevo en la Tierra, Carol Danvers se convierte en uno de los heroes mas poderosos del universo cuando la Tierra se ve atrapada en medio de una guerra galactica entre dos razas alienigenas."),("Greetings <entity-designateSummoner>! Self is referred to as Warlock. Self is capable of many wondrous feats, including changing shape and making jokes! Transmode virus also used to transfer lifeglow from <entity-designateOpponents>. Self will not harm any in the <Champion_Contest>! Hilarious falsehood! Much harm will come to any who attempt to harm Self or SelfFriends. <HumorComplete>");

insert into pasiva(descripcioPasiva)
values ("Hercules pasiva"),("Capitana pasiva"),("Warlock pasiva");

insert into SuperAtaque(TipoSuper,DejaDesventajas)
values ("Super 1: mele H",false),("Super 2: mele H",true),("Super 3: mele H",false),("Super 1: Rayo a distancia C",false),("Super 2: Empieza mele, acaba a distancia C",true),("Super 3: mele C",false);

insert into superPers(idPersonatge,idSuperAtaque)
values (1,1),(1,2),(1,3),(2,4),(2,5),(2,6);


insert into personatge(Nom)
values ("");

insert into caracteristiques(stars,hp,atk,rango,lvl,clase)
VALUES ("4/6",16463,1461,"5/5",50,"Cosmico");

insert into descripcio_pers(descripcioPers)
values ("");

insert into pasiva(descripcioPasiva)
values ("");

/*Per cada personatge es seu super ataque*/
select personatge.Nom,SuperAtaque.TipoSuper from personatge,SuperAtaque,superPers where personatge.idPersonatge = superPers.idPersonatge AND superPers.idSuperAtaque = SuperAtaque.idSuperAtaque;
/*Per cada personatge sa seva descripció*/
select personatge.Nom, descripcio_pers.descripcio from personatge,descripcio_pers where personatge.idPersonatge = descripcioPers.idDescripcio;

/*Tota la informació de tots els personatges*/
select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte limit 2;
/*Tota la informació d'un personatge especific'*/
select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte AND personatge.Nom = "Hercules";