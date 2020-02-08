
from articles.views import index


def test_index(rf):
    request = rf.get("/")
    response = index(request)

    assert 'This is the index' in str(response.content)
