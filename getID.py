import requests
import json
ombd_api = "342bef19"

def get_data(movie_title, release_year):
    req_url = f"http://www.omdbapi.com/?t={movie_title}&y={release_year}&apikey={ombd_api}&"
    try:
        r = requests.get(req_url)
        res = r.json()
        return res["imdbID"]
    except:
        raise AssertionError("Error getting data")


print(get_data("Mela", 1948))