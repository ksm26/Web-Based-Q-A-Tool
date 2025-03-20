# 🌐 Web-Based Q&A Tool

A simple web application that allows users to:  
✅ **Ingest website content** by providing URLs.  
✅ **Ask questions** based strictly on the ingested content.  
✅ **Get concise, AI-generated answers** without using external knowledge.

---

## 🚀 Features

- **Web Scraping**: Extracts text content from webpages.
- **Embeddings & Retrieval**: Uses FAISS for fast search.
- **Local LLM Support**: Runs AI-based Q&A without OpenAI API.
- **Minimal UI**: Built with React for easy interaction.

---

## 📂 Project Structure

web_based_QA/

│── backend/                 # FastAPI backend  
│   ├── app.py               # Main API  
│   ├── scraper.py           # Web scraping logic  
│   ├── embeddings.py        # FAISS index & text embeddings  
│   ├── model.py             # Local LLM for Q&A  
│   ├── requirements.txt     # Backend dependencies  
│── frontend/                # React frontend  
│   ├── src/  
│   │   ├── App.js           # Main UI component  
│   │   ├── api.js           # Axios API calls  
│   │   ├── index.css        # Minimal UI styles  
│   ├── package.json         # Frontend dependencies  
│── README.md                # Documentation  

---

## 🛠️ Tech Stack  

| Component  | Technology Used  |
|------------|----------------|
| **Backend** | FastAPI, FAISS, Sentence Transformers, Llama.cpp |
| **Frontend** | React, Axios, JavaScript |
| **Scraping** | BeautifulSoup, Requests, Selenium (for JS-heavy pages) |
| **LLM** | TinyLlama-1.1B (GGUF format) |

---

## 🚀 Setup Instructions  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/web_based_QA.git
cd web_based_QA
```

### **2️⃣ Install Dependencies**  
```sh
cd backend
pip install -r requirements.txt
```

### **3️⃣ Download a Local LLM Model (TinyLlama)**  
```sh
mkdir -p models
cd models
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```

### **4️⃣ Start the Backend**  
```sh
cd backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## 🎨 Frontend Setup (React)

### **5️⃣  Install Dependencies**  
```sh
cd frontend
npm install
```

### **6️⃣ Start the React App**  
```sh
npm start
```

## 🌍 Usage
### **7️⃣ Ingest a Webpage**  
```sh
curl -X POST "http://127.0.0.1:8000/ingest" \
     -H "Content-Type: application/json" \
     -d '{"url": "https://www.un.org/en/observances/international-nowruz-day"}'
```
📌 Expected Response:
```sh
{"message": "Content ingested successfully!"}
```

### **8️⃣ Ask a Question**  
```sh
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is International Nowruz Day?"}'

```
📌 Expected Response:
```sh
{"answer": "International Nowruz Day celebrates the Persian New Year, observed on March 21st..."}

```

## 🚀 Deployment

### Backend Deployment
```sh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```

### Frontend Production Build
```sh
cd frontend
npm run build

```
