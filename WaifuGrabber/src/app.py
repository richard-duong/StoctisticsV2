from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import nekos
import json
import requests
import ipdb

app = Flask(__name__)


@app.route("/get_waifu_image/<string:gender>/<int:age>")
def get_waifu_image(gender: str, age: int):
    """Response format
    response = {
        "content": [items: list, count]
    }

    item = {
        ['id', 'id_v2', 'image_url', 'sample_url', 'image_size', 'image_width', 'image_height',
        'sample_size', 'sample_width', 'sample_height', 'source', 'source_id', 'rating', 'verification',
        'hash_md5', 'hash_perceptual', 'color_dominant', 'color_palette', 'duration', 'is_original', 'is_screenshot',
        'is_flagged', 'is_animated', 'artist', 'characters', 'tags', 'created_at', 'updated_at']
    }
    """
    if not age or age < 18:
        """Age must be 18 or greater"""
        age = 18
    if gender not in {"male", "female"}:
        gender = "female"
    try:
        response = requests.get(f"https://api.nekosapi.com/v3/images/random?gender={gender}&age={age}&limit=1")
        content = json.loads(response.content)
        image_url = content["items"][0]["image_url"]
        image_id = content["items"][0]["id"]
        return jsonify({"image_url": image_url, "image_id": image_id})
        # TODO rotate images
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    # Test API first
    app.run(debug=True)
