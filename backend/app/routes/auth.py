from flask import Blueprint, request, jsonify
from app.services.spotify import SpotifyService

auth_bp = Blueprint('auth', __name__)
spotify_service = SpotifyService()

@auth_bp.route('/spotify')
def spotify_auth():
    return spotify_service.get_auth_url()

@auth_bp.route('/spotify/callback')
def spotify_callback():
    code = request.args.get('code')
    return spotify_service.handle_callback(code)