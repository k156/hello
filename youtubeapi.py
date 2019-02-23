from apiclient.discovery import build
from pprint import pprint

API_KEY = "AIzaSyBFu4isdWKC_nD25c_u0Zx2NA2ODkwDVZI"

def search_ytb():
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    search_res = youtube.search().list(
        part='snippet',
        q='파이썬',
        type='video'
        maxResults = 50
    ).execute()



    for item in search_res['items']:
        pprint(item)
