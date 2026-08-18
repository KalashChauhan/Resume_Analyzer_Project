# Resume Analyzer
Resume Screening App With Python and Machine Learning 
React frontend and Flask API for the original resume-category classifier. The preprocessing and prediction sequence remains unchanged: clean text, TF-IDF transform, SVC prediction, then label decoding.

## Run it

1. Put `clf.pkl` (the trained SVC model) in the project root.
2. Start the API:
   ```powershell
   cd backend
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python app.py
   ```
3. In another terminal, start React:
   ```powershell
   cd frontend
   npm install
   npm run dev
   ```
