import requests
from spotifytokens import spotify_token


def spot_get_tracklist(album_id):
    """
    Make a request for the tracks on an album and put the tracks into a list.
    """
    url = 'https://api.spotify.com/v1/albums/{}/tracks'.format(album_id)
    header_info = {"Content-Type": "applicatoin/json", "Authorization": "Bearer {}".format(spotify_token)}
    params_info = {"limit": "30"}
    response = requests.get(url, params = params_info, headers = header_info)
    response_json = response.json()['items']
    tracklist = []
    for i in range(response.json()['total']):
        tracklist.append(response_json[i]['name'])
    return tracklist
    