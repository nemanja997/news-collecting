const getArticles = require('./TechCrunch');

const url = 'https://techcrunch.com/';
let articles  = [];

getArticles(url).then( (response) => {
    articles = response;
    console.log(articles);
}).catch( (error) => {
    console.log(error);
});

