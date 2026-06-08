from fastapi import FastAPI

app = FastAPI(
    title="Backend Livros",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "API FastAPI funcionando no Kubernetes!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/livros")
def listar_livros():
    return [
        {
            "id": 1,
            "titulo": "Clean Code",
            "autor": "Robert C. Martin"
        },
        {
            "id": 2,
            "titulo": "Python Fluente",
            "autor": "Luciano Ramalho"
        }
    ]