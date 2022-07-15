const express = require('express');
const pool = require('../database');
const router = express.Router();

//const DadesPersonatges = await pool.query(`select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte ORDER BY idPersonatge asc limit ${limit}`);

router.get('/', async (req,res) =>{ 
    const Personatges = await pool.query(`select Nom from personatge`);  
    res.render('layouts/principal.hbs',{ Personatges }); 
});

router.get('/formulari',  (req,res) =>{  
    res.render('layouts/formulari.hbs'); 
});

router.post('/formulari', async (req,res) =>{  
    const {Nom} = req.body;
    const NomPersonatge = {Nom};
    const {descripcioPers} = req.body;
    const DescripcioPersonatge = {descripcioPers};
    const {pasivaPers} = req.body;
    const PasivaPersonatge = {pasivaPers};
    await pool.query(`INSERT INTO personatge set ?`, [NomPersonatge]);
    await pool.query(`INSERT INTO descripcio_pers set ?`, [DescripcioPersonatge]);
    await pool.query(`INSERT INTO pasiva set ?`, [PasivaPersonatge]);
    res.render('layouts/formulari.hbs');
});

router.get('/Hercules', async (req,res) =>{   
    const DadesPersonatges = await pool.query(`select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte AND personatge.Nom = "Hercules"`);
    res.render('layouts/Tarjetes.hbs',{ DadesPersonatges }); 
});

router.get('/Capitana_Marvel', async (req,res) =>{   
    const DadesPersonatges = await pool.query(`select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte AND personatge.Nom = "Capitana_Marvel"`);
    res.render('layouts/Tarjetes.hbs',{ DadesPersonatges }); 
});

router.get('/Warlock', async (req,res) =>{   
    const DadesPersonatges = await pool.query(`select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte AND personatge.Nom = "Warlock"`);
    res.render('layouts/Tarjetes.hbs',{ DadesPersonatges }); 
});

router.get('/fran', async (req,res) =>{   
    const DadesPersonatges = await pool.query(`select * from personatge,descripcio_pers,pasiva, caracteristiques where personatge.idPersonatge = descripcio_pers.idDescripcio AND personatge.idPersonatge = pasiva.idPasiva AND personatge.idPersonatge = caracteristiques.idCaracte AND personatge.Nom = "fran"`);
    res.render('layouts/Tarjetes.hbs',{ DadesPersonatges }); 
});

module.exports = router;