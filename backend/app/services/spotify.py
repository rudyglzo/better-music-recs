import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import current_app

class SpotifyService:
    def __init__(self):
        self.sp_oauth = SpotifyOAuth(
            client_id=current_app.config['SPOTIFY_CLIENT_ID'],
            client_secret=current_app.config['SPOTIFY_CLIENT_SECRET'],
            redirect_uri=current_app.config['SPOTIFY_REDIRECT_URI'],
            scope='user-library-read playlist-modify-public user-top-read'
        )
    
    def get_auth_url(self):
        return self.sp_oauth.get_authorize_url()
    
    def handle_callback(self, code):
        token_info = self.sp_oauth.get_access_token(code)
        return token_info
