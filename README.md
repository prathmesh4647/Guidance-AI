# 🚀 Guidance.AI  
### A Smart Application for Academic Project Management  

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![AI](https://img.shields.io/badge/AI-Gemini%20%2B%20NLP-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

🌐 **Live Demo:** https://guidanceai.me  
📂 **GitHub Repo:** https://github.com/prathmesh4647/Guidance-AI  

---

## 📌 Overview

**Guidance.AI** is an AI-powered centralized academic project management system designed to streamline the entire lifecycle of Project-Based Learning (PBL).

It helps students generate innovative ideas, prevents plagiarism using semantic similarity detection, and enables faculty to evaluate projects efficiently using a structured digital system.

---

## 🎯 Key Features

### 🤖 AI Idea Generation
- Powered by **Google Gemini API**
- Generates unique, innovative project ideas
- Helps students overcome creative blocks

### 🔍 Semantic Similarity Detection
- Uses **Sentence Transformers (all-MiniLM-L6-v2)**
- Converts project descriptions into embeddings
- Detects conceptual plagiarism using **cosine similarity + pgvector**

### 👨‍🎓 Student Portal
- Submit up to 3 project ideas
- Track approval status
- Upload screenshots, PPT, and source code
- Maintain SDLC progress using Digital Workbook

### 👩‍🏫 Faculty Portal
- Review and approve/reject ideas
- View similarity score
- Evaluate projects using structured marking system
- Monitor student progress

### 📊 Evaluation System
- Criteria-based grading
- Automatic score calculation
- Transparent and standardized evaluation

### 🏆 Leaderboard & Showcase
- Displays top projects
- Public gallery with likes/upvotes
- Encourages innovation and competition

---

## 🛠️ Tech Stack

| Category        | Technology |
|----------------|-----------|
| Backend        | Django (Python) |
| Frontend       | HTML, CSS, JavaScript |
| Database       | PostgreSQL |
| Vector Search  | pgvector |
| AI/NLP         | Sentence Transformers (PyTorch-based) |
| AI API         | Google Gemini |
| Deployment     | Docker, Nginx |
| Testing        | Locust |

---

## ⚡ Performance Highlights

- 🚀 100% requests handled under **10ms**
- 📉 0 request failures during load testing
- ⚡ Fast vector similarity search using pgvector
- 📊 Stable performance under concurrent users

---

## 🔐 Authentication & Roles

- Student Login
- Faculty Login
- Role-based access control
- Secure authentication system

---

## 📂 Project Modules

- Authentication System
- AI Idea Generator
- Project Submission & Tracking
- Faculty Evaluation Dashboard
- Digital Workbook (SDLC Tracking)
- Project Showcase & Leaderboard
- File Upload System (Screenshots, PPT, Code)

---

## 🧠 How AI Works

1. Student submits project idea  
2. Sentence Transformer converts text → vector embedding  
3. Embedding stored in PostgreSQL (pgvector)  
4. Cosine similarity calculated  
5. Faculty sees similarity score to detect plagiarism  

