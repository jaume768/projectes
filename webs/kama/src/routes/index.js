const express = require('express');
const pool = require('../database');
const router = express.Router();

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

router.get('/', (req,res) =>{ 
    res.render('layouts/principal.hbs'); 
});

router.get('/facil', async (req,res) =>{ 
    const PosicionesFaciles = await pool.query(`select * from posiciones,dificultad,dificultad_posiciones where posiciones.idPosicio = dificultad_posiciones.idPosicio AND dificultad_posiciones.idDificultad = dificultad.idDificultad AND dificultad_posiciones.idDificultad = 1 AND posiciones.idPosicio = ${getRandomInt(16) + 1};`);
    res.render('partials/posicions.hbs', {PosicionesFaciles}); 
});

router.get('/normal', async (req,res) =>{ 
    const PosicionesFaciles = await pool.query(`select * from posiciones,dificultad,dificultad_posiciones where posiciones.idPosicio = dificultad_posiciones.idPosicio AND dificultad_posiciones.idDificultad = dificultad.idDificultad AND dificultad_posiciones.idDificultad = 2 AND posiciones.idPosicio = ${getRandomInt(15) + 17};`);
    res.render('partials/posicions.hbs', {PosicionesFaciles}); 
});

router.get('/dificil', async (req,res) =>{ 
    const PosicionesFaciles = await pool.query(`select * from posiciones,dificultad,dificultad_posiciones where posiciones.idPosicio = dificultad_posiciones.idPosicio AND dificultad_posiciones.idDificultad = dificultad.idDificultad AND dificultad_posiciones.idDificultad = 3 AND posiciones.idPosicio = ${getRandomInt(3) + 31};`);
    res.render('partials/posicions.hbs', {PosicionesFaciles}); 
});

module.exports = router;