from flask import Blueprint, request, jsonify
from app.services.recommendations import RecommendationEngine

recommendations_bp = Blueprint('recommendations', __name__)
recommendation_engine = RecommendationEngine()

@recommendations_bp.route('/')
def get_recommendations():
    user_id = request.args.get('user_id')
    count = request.args.get('count', default=10, type=int)
    return jsonify(recommendation_engine.get_recommendations(user_id, count))