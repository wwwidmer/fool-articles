
def serialize_article(article):
    return {
        "uuid": article.uuid,
        "headline": article.headline,
        "tags": article.tags,
        "authors": article.authors,
        "links": article.links,
        "recommendations": article.recommendations,
        "images": article.images,
        "body": article.body,
        "promo": article.promo
    }


def serialize_comment(comment):
    return {
        "text": comment.text,
        "username": comment.username,
        "created_at": comment.created_at
    }
