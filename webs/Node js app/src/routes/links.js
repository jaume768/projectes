const express = require('express');
const router = express.Router();

const db = require('../database');

router.get('/menu1', (req,res) =>{
    res.render('links/menu1.hbs');
});

module.exports = router;