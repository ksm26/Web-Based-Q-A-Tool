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

