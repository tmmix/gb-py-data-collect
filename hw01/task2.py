import requests

url = 'http://ws.audioscrobbler.com/2.0/'
api_key = '6203e92b28a50f2ccf9999543d90636c'
method = 'chart.getTopArtists'

resp = requests.get(url + '?method=' + method + '&api_key=' + api_key)

with open('last_fm_top_artists.xml', 'w', encoding='UTF-8') as f:
    f.write(resp.text)
