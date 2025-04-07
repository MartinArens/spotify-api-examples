import requests
import base64

CLIENT_ID = ""
CLIENT_SECRET = ""

#https://open.spotify.com/playlist/5bbuQsCbePqMZuwT5jWAip?si=ad7a7c873c1a43f3
PLAYLIST_ID = "2BpzCM8JxmpTyg72UKqI4q?si=co6yqsa2SluPwMkwvX1DEg&pi=U-LAVMxtRzyse"

def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

def get_playlist_tracks(playlist_id, access_token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {"Authorization": f"Bearer {access_token}"}

    tracks = []

    while url:
        response = requests.get(url, headers=headers)
        data = response.json()

        for track in data.get("tracks", {}).get("items", []):
            artists = []
            for artist in track.get("track", []).get("artists", []):
                artists.append(artist['name'])
                artists_clean = ", ".join(artists)
            if track:
                tracks.append(f"{track['track']['name']} - {artists_clean}")


        url = data.get("next")

    return tracks


token = get_access_token(CLIENT_ID, CLIENT_SECRET)

playlists = [
'0hPKtHZE7RmSztVM02AESj?si=24ce6b9fade84c6e',
'2BpzCM8JxmpTyg72UKqI4q?si=co6yqsa2SluPwMkwvX1DEg&pi=U-LAVMxtRzyse',
'0IJ5IvG65OmJ77LkWJ4x3s?si=nn6WOhnxSpCT9UmhNCr-ug&pi=NMH7MVU0R16-y',
'1CvyCFsXa9P4IlzMEMmRX4?si=_3FeqF4zTkSV0FVt7tQv9Q&pi=I-bobYIUReSvV',
'1zPhIaORo2DOQSo0R4UMRV?si=OM-sGBZbTOSK1ahr1UefAQ',
'2AYd9OdMhGqxM8AtwMnm03?si=FTJR16vUQsCBLKQ_Fnxm6A&pi=TZrkhLPyT5msK',
'7gEwxTTNVSd64dvWrJkZsA?si=8097aa6d13f64f81',
'7bYGnVZRH5l3CrjSMImUeY?si=4144af6347c340cb',
'1Aaze74fm58N1tOR7iPXoP?si=69c36e2339ff4674',
'7BNQdaLkNKxs9cyAEQekKN?si=j2XALNv_Sje5VmJr39qj1w&pi=ju11swKbSuumK',
'1cI1J9YIwQtNnc3XCaUySp?si=a54b1bb9e87d4a41',
'1aXLTMyy4oWtKdG8NfyYa8?si=07b63585716a4626',
'4NcwXq6G2xjJiHfTrtIF3X?si=435edcd5d13d4c5a',
'6PJemI2kup7lH6OLzfuBfi?si=e437f51ca4144ae3&pt=0e5bb62a77ee072b6372e4bf6318d4f3',
'4pjZITEOKq7HcONfl0Ahgg?si=6NoS4sGwTpCewYM7vAbRbA',
'3uJBh4GRjh5UOKgsLxsI9m?si=Gc0LzcwuQ0SQiK8TTjTqOA&pi=__xkySqcQaWMw',
'0gPuOm11KV4KKy87iGkDmB?si=_9xLaioeTfeA3gwCipC6qw&pi=CYtzS7xoTYeta',
'3FQGMQFA9YUsbyEfc5m05I?si=66i3wK_zRUywTvk3s77dCg',
'15eL50TNl0bA6huNYVnbl3?si=KcLOc1IdRbCh3hlRsDkDjQ&pi=hUnT1I0oTIeKi',
'7yrOVubHwE0Tq8z5sxg6IQ?si=24ab52df83d94d0b',
'63sncnrawcLa63nBagsRXE?si=a66b9027c1ad4e93',
'605Ql3Hhf4SlOLpDePAtyH?si=5bfd831842364c02',
'3o3fA7Bf2HpPmJTPTRtu5f?si=fbb677bca41e4c2a',
'5bbuQsCbePqMZuwT5jWAip?si=ad7a7c873c1a43f3',
'3TsdSbVYWbmAblU3VQ1JZX?si=IcvR8J5BTpavk7ymcV_vMA&pi=CNhGfjf_ToWRl',
'26AsQwVD0TSkpVvbAdXTGR?si=ntSZPXDWQQmrC8rIV8UyaQ&pi=56vDFMzjRJOGS',
]

for playlist in playlists:
    playlist_tracks = get_playlist_tracks(playlist, token)

    for track in playlist_tracks:
        print(f"{playlist}, {track}")
