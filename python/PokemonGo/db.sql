create table usuaris(
    id int(255) not null auto_increment,
    Mac text,
    ipUsuari text,
    primary key(id)
);

create table claus(
    id int(255) not null auto_increment,
    id_usuaris int(255),
    clau text not null,
    premium BOOLEAN,
    enviada BOOLEAN,
    gmail text,
    Nom text,
    primary key(id),
    FOREIGN KEY (id_usuaris) REFERENCES usuaris(id)
);

insert into claus(clau,id_usuaris,premium,enviada)
VALUES ("clau2",2,FALSE,TRUE);

insert into usuaris(Mac)
VALUES ("prova");