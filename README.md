# Mastodon-API-272-HW
Creating an app to interact with Mastodon API to perform CRUD Operations


# 🦣 Mastodon API Web UI

A simple Flask-based CRUD application that interacts with Mastodon API.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/bhusalashish/Mastodon-API-272-HW.git
 cd Mastodon-API-272-HW.git
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
 python -m venv .venv
 source .venv/bin/activate
```

### 3️⃣ Install Dependencies 📦
```sh
 pip3 install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables 🔑
Create a `.env` file and add your Mastodon API credentials:
```sh
 MASTODON_ACCESS_TOKEN=your_access_token
 MASTODON_API_BASE_URL=https://mastodon.instance.url
```

---

## 🏃‍♂️ Running the Server
```sh
 flask run
```
Open your browser and navigate to:
```sh
 http://127.0.0.1:5000
```

---

## 🧪 Running Tests
```sh
 python3 test.py
```

---

## 📡 API Endpoints
- `POST /post` → Create a new Mastodon post.
- `POST /retrieve` → Retrieve a post by status ID.
- `POST /delete` → Delete a post by status ID.

---

## 🛠️ Troubleshooting
### ❌ Flask not found?
Try installing it manually:
```sh
 pip3 install Flask
```
### ❌ Issues with `.env` file?
Make sure to load environment variables using:
```sh
 pip3 install python-dotenv
```

---

🔥 **Happy Coding!** 🚀
