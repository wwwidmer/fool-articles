
def serialize_article(article):
    return {
        "headline": article.headline,
        "tags": article.tags,
        "authors": article.authors,
        "links": article.links,
        "recommendations": article.recommendations
    }
