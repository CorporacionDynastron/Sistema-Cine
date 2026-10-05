import urllib.request
import urllib.parse
import re

movies = [
    'Avengers Doomsday poster',
    'El corazon de la bestia poster',
    'Resident evil noche cero poster',
    'Coyote vs Acme poster'
]

for movie in movies:
    query = urllib.parse.quote(movie)
    url = f'https://html.duckduckgo.com/html/?q={query}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'href=\"(https?://[^\"]+\.(?:jpg|jpeg|png))\"', html, re.I)
        if match:
            print(f'{movie}: {match.group(1)}')
        else:
            print(f'{movie}: Not found')
    except Exception as e:
        print(f'{movie}: Error {e}')
