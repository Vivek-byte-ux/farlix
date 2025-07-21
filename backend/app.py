from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # allow frontend access

videos = [
    {
        "id": 1,
        "title": "Free Movie 1",
        "description": "Watch now!",
        "url": "https://www.youtube.com/embed/dQw4w9WgXcQ"
    },
    {
        "id": 2,
        "title": "Free Movie 2",
        "description": "Enjoy this show.",
        "url": "https://www.youtube.com/embed/3JZ_D3ELwOQ"
    }
]

@app.route('/videos')
def get_videos():
    return jsonify(videos)

if _name_ == '_main_':
    app.run(debug=True)
