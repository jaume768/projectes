create database kama;

use kama;

create table posiciones(    
    idPosicio int(255) not null auto_increment,
    Nom varchar(30) not null,
    link text,
    primary key(idPosicio)
);

create table dificultad(    
    idDificultad int(255) not null auto_increment,
    Tipo text not null,
    primary key(idDificultad)
);

create table dificultad_posiciones(
    idPosicio int(255),
    idDificultad int(255),
    FOREIGN KEY (idPosicio) REFERENCES posiciones(idPosicio),
    FOREIGN KEY (idDificultad) REFERENCES dificultad(idDificultad)
);

/* selects */

/* treure totes les posicions facils */

select posiciones.Nom from posiciones,dificultad,dificultad_posiciones where posiciones.idPosicio = dificultad_posiciones.idPosicio AND dificultad_posiciones.idDificultad = dificultad.idDificultad AND dificultad_posiciones.idDificultad = 1;

/* información 

insert into posiciones(Nom,link)
values ("","");

insert into dificultad_posiciones(idPosicio,idDificultad)
values(1,1);

*/

/*Facils*/
insert into posiciones(Nom,link)
values ("Heredero al trono","https://media.theobjective.com/app/uploads/2022/05/124410/sexo-oral-5-500x390.jpg"),("69","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/03/10_7.png"),("mecanico","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_18.png");

insert into posiciones(Nom,link)
values ("Valedictorio","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_17.png"),("Hambre","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_16.png"),("compliment","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_37.png"),("Garganta profunda","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/18_87.png"),("Superheroe","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/11_22_5.png"),("Zeus","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/04/12_19.png"),("Virgo","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/04/11_32_3.png"),("Martillo neumatico","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/04/12_17_3.png"),("Piscis","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/04/11_24_2.png");

insert into posiciones(Nom,link)
values ("Valedictorio","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/03/11_20_2.png"),("Diosa","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/03/11_17_2.png"),("Espejismo","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/03/12_10_2.png"),("Horizonte","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/03/12_9.png");


/* Normals */

insert into posiciones(Nom,link)
values ("chibi","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_33.png"),("catapult","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_43.png"),("jugoso","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_35.png"),("Caballero","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_23.png"),("Lucha","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_22.png"),("comodo","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_27.png"),("Riverside","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_19.png"),("Tornillo","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_15.png"),("Cautividad","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_12.png"),("Fusion","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_6.png"),("Perrito en el borde","https://sexpositions.club/es/wp-content/uploads/sites/2/2019/06/19_28.png");

insert into posiciones(Nom,link)
values ("Tijera","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/04/13_28.png"),("Unicornio","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/04/13_27_3.png"),("Sprout","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/02/6_4.png"),("Lanzadera","https://sexpositions.club/es/wp-content/uploads/sites/2/2016/02/1_3_3.png");

/* Dificultats */
insert into dificultad(Tipo)
values ("facil"),("normal"),("dificil");

/* intermitges */

insert into dificultad_posiciones(idPosicio,idDificultad)
values(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(14,1),(15,1),(16,1),(13,1),(17,2),(18,2),(19,2),(20,2),(21,2),(22,2),(23,2),(24,2),(25,2),(26,2),(27,2),(28,2),(29,2),(30,2),(31,2);