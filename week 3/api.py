import requests

def get_post_title():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )
    return response.json()["title"]
