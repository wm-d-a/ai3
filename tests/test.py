from tests.conftest import client


def test_regular(client):
    response = client.get(
        "/correct_your_text",
        query_string={
            'text': 'When I grow up, I start to understand what he said is quite right.',
        }
    )
    assert response.status_code == 200
    assert response.json == {
        'corrected_text': 'When I grow up, I will start to understand what he said is quite right.'}


def test_empty(client):
    response = client.get(
        "/correct_your_text",
        query_string={
            'text': '',
        }
    )
    assert response.status_code == 404

# python -m pytest app/tests/test.py

def test_lang(client):
    response = client.get(
        "/correct_your_text",
        query_string={
            'text': 'тест',
        }
    )
    assert response.status_code == 404
    assert response.json == {
           'corrected_text': 'INPUT_ENGLISH_TEXT'}
