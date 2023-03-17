
import json


def test_post_url(client):

    response = client.post(
        "/url/shortener/", json={"url": "www.fakesite.com/long/url"})

    data = json.loads(response.data)
    assert response.status_code == 200
    assert data.get('message') == "success"


def test_post_url_fail(client):

    response = client.post(
        "/url/shortener/", json={})

    data = json.loads(response.data)
    assert response.status_code == 400
    assert data.get("errors")


def test_post_url_http_fail(client):

    response = client.post(
        "/url/shortener/", json={"url": "http://www.google.com"})

    data = json.loads(response.data)
    assert response.status_code == 400
    assert data.get('error') == "url cant contains http:// or https://"


def test_get_url(client):

    post = client.post(
        "/url/shortener/", json={"url": "www.fakesite.com/long/url"})
    data_post = json.loads(post.data)
    url = data_post.get("short_url")

    get = client.get(f'/url/shortener/?url={url.replace("https://","")}')
    data_get = json.loads(get.data)

    assert get.status_code == 200
    assert data_get.get('url') == "www.fakesite.com/long/url"


def test_get_url_not_found(client):

    get = client.get(f'/url/shortener/?url=www.short.com/1234567')
    data_get = json.loads(get.data)

    assert get.status_code == 404


def test_get_url_http_fail(client):

    post = client.post(
        "/url/shortener/", json={"url": "www.fakesite.com/long/url"})
    data_post = json.loads(post.data)
    url = data_post.get("short_url")

    get = client.get(f'/url/shortener/?url=https://{url}')
    data_get = json.loads(get.data)

    assert get.status_code == 400
    assert data_get.get('error') == "url cant contains http:// or https://"


def test_get_not_url_fail(client):

    post = client.post(
        "/url/shortener/", json={"url": "www.fakesite.com/long/url"})
    data_post = json.loads(post.data)
    url = data_post.get("short_url")

    get = client.get(f'/url/shortener/')
    data_get = json.loads(get.data)

    assert get.status_code == 400
    assert data_get.get('error') == "url parameter is required"


def test_get_not_valid_url_fail(client):

    get = client.get(f'/url/shortener/?url=www.google.com')
    data_get = json.loads(get.data)

    assert get.status_code == 400
