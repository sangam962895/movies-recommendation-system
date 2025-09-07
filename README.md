# 🎬 Movie Recommendation System

A user-friendly **Streamlit** app that recommends movies using a precomputed similarity matrix and fetches posters, IMDb ratings, and genres dynamically via APIs.

🚀 **Live Demo**: [Click here to try the app](https://movies-recommendation-system-286f.onrender.com)  
*(hosted on Render)*

---

## ✨ Features

- 📥 **On-demand resources**: Automatically downloads `movies.pkl` and `similarity.pkl` from Google Drive.  
- 🎯 **Similarity-based recommendations**: Finds top 5 movies using cosine similarity.  
- 🖼️ **Rich metadata**: Shows posters, IMDb ratings, and genres using TMDB & OMDb APIs.  
- 🖥️ **Interactive UI**: Built with Streamlit for an intuitive and responsive experience.  

---

## 🛠️ Setup (Run Locally)

### 1. Clone the repo
```bash
git clone https://github.com/sangam962895/movies-recommendation-system.git
cd movies-recommendation-system
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
streamlit run app.py
```

App will open at `http://localhost:8501`.

---

## 🌍 Deployment (Render)

This project is already deployed on **Render**.

For your own deployment:
1. Push your repo to GitHub.  
2. Connect GitHub repo to [Render](https://render.com/).  
3. Use these settings:  

   - **Build Command**:  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:  
     ```bash
     streamlit run app.py --server.port $PORT --server.address 0.0.0.0
     ```

---

## 📂 Project Structure

```
movies-recommendation-system/
│
├── app.py             ← Main Streamlit application
├── requirements.txt   ← Required Python packages
└── README.md          ← Project overview & instructions
```

---

## 🔑 Notes

- Make sure `movies.pkl` & `similarity.pkl` Google Drive files are set to  
  **"Anyone with the link → Viewer"**.  
- Replace with your own **API keys** if required:  
  - TMDB API key  
  - OMDb API key  

---
## 📸 Screenshot

<img width="1657" height="843" alt="Screenshot 2025-09-07 143053" src="https://github.com/user-attachments/assets/3f996059-7956-48c8-bc98-7c7fb7dc4682" />

<img width="1503" height="813" alt="Screenshot 2025-09-07 143159" src="https://github.com/user-attachments/assets/a1bc123f-8df8-4fa2-917d-db42bc4a61c3" />
<img width="1799" height="783" alt="Screenshot 2025-09-07 142949" src="https://github.com/user-attachments/assets/424c2b65-f487-4654-862f-d63cc8d6c84e" />




## 🚀 Future Improvements

- Add **personalized recommendations** (collaborative filtering).  
- Improve UI with search suggestions and genre filters.  
- Allow users to rate movies and get tailored recommendations.  

---

## 🙌 Credits

Developed by [Sangam Kumar Gupt](https://github.com/sangam962895)  
Inspired by machine learning recommendation systems and enhanced with live metadata.
