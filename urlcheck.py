import requests

urls = [
    'https://www.example.com',
    'https://www.example.com/page1',
    'https://www.example.com/page2',
    'https://www.example.com/page3',
    'https://www.example.com/page4',
]

for url in urls:
    response = requests.get(url)
    if response.history:
        print(f"{url} redirects to {response.url}")
    else:
        print(f"{url} does not redirect")
