from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Database config
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(BASE_DIR, "data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database model
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    folder_url = db.Column(db.String(500))
    name = db.Column(db.String(200))
    google_drive_id = db.Column(db.String(200))
    size = db.Column(db.Integer)
    mime_type = db.Column(db.String(100))
    storage_path = db.Column(db.String(500))

# Create tables
with app.app_context():
    db.create_all()

# ✅ HOME ROUTE (THIS FIXES 404)
@app.route("/")
def home():
    return {"message": "Backend is running successfully"}

# Import route
@app.route("/import/google-drive", methods=["POST"])
def import_google_drive():
    data = request.get_json()
    folder_url = data.get("folder_url")

    image = Image(
        folder_url=folder_url,
        name="sample.jpg",
        google_drive_id="dummy_id",
        size=12345,
        mime_type="image/jpeg",
        storage_path="s3://dummy/sample.jpg"
    )

    db.session.add(image)
    db.session.commit()

    return jsonify({"message": "Saved to database"})

# Get images
@app.route("/images", methods=["GET"])
def get_images():
    images = Image.query.all()
    result = []

    for img in images:
        result.append({
            "id": img.id,
            "folder_url": img.folder_url,
            "name": img.name,
            "google_drive_id": img.google_drive_id,
            "size": img.size,
            "mime_type": img.mime_type,
            "storage_path": img.storage_path
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
