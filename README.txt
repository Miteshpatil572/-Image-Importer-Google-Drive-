# FotoOwl Backend Assignment – Scalable Image Import System

## 🔹 Project Overview
This project is a backend system that imports images from a Google Drive folder URL (simulated),
stores image metadata in a SQL database, and exposes APIs to retrieve the imported images.
A simple frontend is provided to interact with the backend APIs.

The system is designed with scalability and modularity in mind.

---

## 🔹 Tech Stack
- Backend: Python, Flask
- Database: SQLite (SQL)
- Frontend: HTML, CSS, JavaScript
- APIs: REST
- Containerization: Docker (optional)

---

## 🔹 Features
- Import images using Google Drive folder URL (simulated)
- Store image metadata in database
- Fetch all imported images via API
- Simple frontend to trigger import and view images
- CORS enabled for frontend-backend communication

---

## 🔹 API Endpoints

### POST /import/google-drive
**Request Body**
```json
{
  "folder_url": "https://drive.google.com/your-folder-url"
}
