Some thought process information before starting...

# Requirements:

## Two Pages

### Homepage
Gets the first article from content_api with tag "slug=10-promise"
Contains 3 random articles


`function getArticles(slug: string) -> [Article]`
(Type of Article TBD)

### Article
Reuse `getArticles`
Filled with content, quotes, and comments


Add a comment as anonymous user
I'll need a model for comments
- text
- id
? Anything else ?

Latest Headlines
[
  { headlineText, headlineHref }
]



Button that shuffles the order of the stock quotes



## Data
### content
I made json schema to make parsing this less tedious
### quotes
I made json schema to make parsing this less tedious

## Other notes
I used JSONSchema to infer the schema of both json files
I'll treat the content (content_api and quotes) as a request to another service
I will type hint my Python code using Python3
I'll use the basic flake8 configuration to make sure I'm not shooting myself in the foot with any silly errors


## Testing

I will use pytest for all backend testing
I will not include e2e tests, although I may include some broad integration tests.
