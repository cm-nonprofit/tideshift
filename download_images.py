import os, json, urllib.request, urllib.parse, ssl, random

UNSPLASH_API_KEY = 'buhc7QncQ0ZMcCjMWpJhQ-NIiIjmoNeFYE4IyOiCbVA'
ASSETS = 'assets'

ssl_ctx = ssl.create_default_context()


def download_image(query, filename, orientation='landscape'):
    os.makedirs(ASSETS, exist_ok=True)
    try:
        params = urllib.parse.urlencode({'query': query, 'per_page': 10, 'orientation': orientation})
        url = f'https://api.unsplash.com/search/photos?{params}'
        req = urllib.request.Request(url, headers={'Authorization': f'Client-ID {UNSPLASH_API_KEY}'})
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        if data.get('results'):
            pick = random.choice(data['results'])
            image_url = pick['urls']['regular']
            with urllib.request.urlopen(image_url, context=ssl_ctx, timeout=15) as img_resp:
                img_data = img_resp.read()
            path = os.path.join(ASSETS, filename)
            with open(path, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded: {filename} (query: {query})")
            return True
    except Exception as e:
        print(f"Failed {filename} ({query}): {e}")
    return False


# Ocean health nonprofit — coastal California, beach cleanups, marine education
download_image('beach cleanup volunteers california', 'program1.jpg')
download_image('marine biology classroom students', 'program2.jpg')
download_image('plastic pollution ocean shore', 'program3.jpg')
download_image('children tidepool learning', 'program4.jpg')
download_image('california pacific coastline aerial', 'hero-bg.jpg')
download_image('sea turtle underwater conservation', 'impact1.jpg')
download_image('kelp forest underwater california', 'impact2.jpg')

print("Done.")
