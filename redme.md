http://127.0.0.1:8000
http://127.0.0.1:8000/docs

cd wikipedia-summarizer-api
source venv/bin/activate
uvicorn main:app --reload
