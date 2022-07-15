const express = require('express');
const morgan = require('morgan');
const exphbs = require('express-handlebars');
const path = require('path');
function create(){

}

//inicializar
const app = express();

//ajustes
app.set('port', process.env.PORT || 4000);
app.set('views', path.join(__dirname, 'views'));
app.engine('.hbs', exphbs.engine({
    defaultLayout: 'main',
    layoutsDir: path.join(app.get('views'),'layouts'),
    partialsDir: path.join(app.get('views'),'partials'),
    extname: '.hbs',
    helpers: require('./lib/handlebars')
})); // tot lo que requereix es servidor per funcionar
app.set('view engine', '.hbs');

//veure ses peticions a nes servidor des clients (moddlewares)
app.use(morgan('dev')); // per controlar ses peticions
app.use(express.urlencoded({extended: false})); // aixo es perque es clients nomes puguin enviar textos i no fotos ni videos

//Variables locals
app.use((req,res,next) =>{
    next();
});

// Rutes
app.use(require('./routes')); 
app.use(require('./routes/links')); 
// carpetas publicas

app.use(express.static(path.join(__dirname,'public')));

// iniciar server
app.listen(app.get('port'), ()=>{
    console.log('Servidor a nes port',app.get('port'));
});