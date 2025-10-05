# Deployment & Testing Guide

## Overview
This document provides step-by-step instructions to **deploy** and **test** the `achareh-assistant` project using Docker.

---

## 📦 Project Structure

```
achareh-assistant/
├── app/
│   ├── main.py
│   ├── services.py
│   ├── conversation.py
│   └── database.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Deployment Instructions

### 1. Build the Docker image
Run the following command inside the `achareh-assistant` directory:

```bash
sudo docker build -t achareh-assistant .
```

---

### 2. Run the container
To start the application:

```bash
sudo docker run -it -p 8000:8000 achareh-assistant
```

If you want to persist the SQLite database on your host system:

```bash
sudo mkdir -p $(pwd)/data
sudo docker run -it -p 8000:8000 -v $(pwd)/data:/app/data achareh-assistant
```

The application will automatically create or use the database inside `/app/data` within the container.

---

### 3. Verify the service
After running the container, the API should be available at:

```
http://localhost:8000/
```

If you're testing with `curl`:

```bash
curl -X POST http://localhost:8000/conversation -H "Content-Type: application/json" -d '{"message": "Hello"}'
```

---

## 🧪 Testing

You can run the service locally without Docker as well:

```bash
cd app
pip install -r ../requirements.txt
python3 main.py
```

By default, the server runs on port `8000`.

---

## 🗂 Database

The SQLite database file (`conversations.db`) is automatically created when the app runs for the first time.  
To inspect the database:

```bash
sqlite3 conversations.db
.tables
```

---

## 🧹 Clean Up

To stop and remove containers:

```bash
sudo docker ps
sudo docker stop <container_id>
sudo docker rm <container_id>
```

To remove the image:

```bash
sudo docker rmi achareh-assistant
```

---

## ✅ Summary

| Task | Command |
|------|----------|
| Build image | `sudo docker build -t achareh-assistant .` |
| Run container | `sudo docker run -it -p 8000:8000 achareh-assistant` |
| Run with volume | `sudo docker run -it -p 8000:8000 -v $(pwd)/data:/app/data achareh-assistant` |
| Local run | `python3 app/main.py` |

---

**Author:** [Your Name]  
**Project:** Achareh Assistant  
**Version:** 1.0.0  
