@app.route("/import/google-drive", methods=["POST"])
def import_google_drive():
    data = request.get_json()
    folder_url = data.get("folder_url")

    images = [
        {
            "name": "image1.jpg",
            "google_drive_id": "abc123",
            "size": 102400,
            "mime_type": "image/jpeg",
            "storage_path": "https://s3.amazonaws.com/bucket/image1.jpg"
        },
        {
            "name": "image2.png",
            "google_drive_id": "def456",
            "size": 204800,
            "mime_type": "image/png",
            "storage_path": "https://s3.amazonaws.com/bucket/image2.png"
        }
    ]

    for img in images:
        new_request = ImportRequest(
            folder_url=folder_url,
            name=img["name"],
            google_drive_id=img["google_drive_id"],
            size=img["size"],
            mime_type=img["mime_type"],
            storage_path=img["storage_path"]
        )
        db.session.add(new_request)

    db.session.commit()

    return jsonify({
        "message": "Images saved to database",
        "folder_url": folder_url,
        "imported_count": len(images)
    })
