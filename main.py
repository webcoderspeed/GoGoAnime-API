# main.py (or latest_episodes_module.py, keep the function here)

import requests
from bs4 import BeautifulSoup as bs


def latestepisodes():
    """
    Retrieves the latest released anime episodes from gogoanime.

    Returns:
        list: A list of dictionaries, where each dictionary represents an anime episode
              and contains the title, image URL, and episode URL.
    """
    animesjson = []
    types = [1, 2, 3]  # Different types of releases

    for type_num in types:
        url = f'https://ajax.gogo-load.com/ajax/page-recent-release.html?page=1&type={type_num}'
        try:
            r = requests.get(url)
            r.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            soup = bs(r.text, "html.parser")
            animes = soup.find("ul", {"class": "items"}).find_all("li")

            for anime in animes:
                title = anime.find("p", {"class": "name"}).find("a").text.strip()
                episode = anime.find("p", {"class": "episode"}).text.strip()
                image = anime.find("div", {"class": "img"}).find("img").attrs['src']
                if type_num == 1:
                    base_url = "https://gogoanime.pe"
                else:
                    base_url = "https://gogoanime.by"

                url_anime = base_url + anime.find("div", {"class": "img"}).find("a").attrs['href']
                
                item = {
                    'title': f"{title} {episode}",
                    'image': image,
                    'url': url_anime,
                }
                animesjson.append(item)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
        except AttributeError as e:
            print(f"Error parsing data from {url}: {e}")
            print(f"Response text: {r.text if 'r' in locals() else 'No response'}") # debug
    return animesjson
