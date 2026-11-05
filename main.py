from fastapi import FastAPI 
app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from Nikhil's rag-app!"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/about")
def about():
    return {"name":"Nikhil","day": 1,"project": "Rag App", "learning": "FastAPI Setup"}