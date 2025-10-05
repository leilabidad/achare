# 🧠 Achareh Assistant — Deployment & Testing Guide

## 1. Prerequisites  
Make sure the following are installed on your system:  
- **Docker**
- **Docker Compose** (optional)
- Internet connection (required for the first image build)

---

## 2. Build and Run the Service  

### Build the Docker image:
```bash
sudo docker build -t achareh-assistant .
```

### Run the container:
```bash
sudo docker run -d -p 8000:8000 -v $(pwd)/data:/app/data achareh-assistant
```

🗂 The SQLite database will be automatically created at `./data/conversations.db`.  
If the `data/` directory does not exist, create it first:
```bash
mkdir data
```

---

## 3. Testing the Service  

### 3.1. Send a sample message to the assistant:
```bash
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"user_id": 1, "message": "I need home cleaning service"}'
```

#### Sample Response:
```json
{
  "response": "The home cleaning service is available in your city. Would you like to see the pricing details?",
  "service_slug": "home-cleaning"
}
```

---

### 3.2. View stored conversations:
```bash
sudo apt install sqlite3
sqlite3 data/conversations.db
```

Inside the SQLite shell, run:
```sql
.tables;
SELECT * FROM conversations;
```

---

## 4. Project Structure  

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

## 5. Logs and Maintenance  

### View container logs:
```bash
sudo docker logs -f <container_id>
```

### Access the container shell:
```bash
sudo docker exec -it <container_id> /bin/bash
```

### Stop and remove the container:
```bash
sudo docker stop <container_id>
sudo docker rm <container_id>
```

---

## 6. Notes  

- The SQLite database is stored at `/app/data/conversations.db` and mapped to the host machine using Docker volume.  
- The project is designed with a simple, scalable, and modular architecture for easy extension.  
- New endpoints can be added easily to handle additional Achareh services.  

---

✅ **The project is now ready for deployment and testing.**
