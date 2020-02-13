const rp = require('request-promise');
const $ = require('cheerio');

async function getArticle (url) {
    let html = await rp(url);
    let title =  $('.article__title',html).text();
    let author = $('.article__byline > a',html).text().trim();
    let content = $('.article-content',html).text().trim();
    let imageUrl = $(html).find('img').attr('src');
    let article = {
        title,
        author,
        content,
        imageUrl
    };
    return article;
}

async function getLinks (url) {
    let html = await rp(url);
    let links = [];
    let elements = $('.post-block__title__link',html);

    for(let i = 0; i < elements.length; i++){
        let link = elements[i].attribs.href;
        if ( !link.includes('/video/') ) {
            links.push(link);
        }
    }
    return links;
}

module.exports = async function getArticles (url) {
    let articles = [];
    let links = await getLinks(url);
    for(let i = 0; i < links.length; i++){
        let article = await getArticle(links[i]);
        articles.push(article);
    }
    return articles;
}
