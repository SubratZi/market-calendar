from fastapi import FastAPI
app = FastAPI (
    title = "Market-Calendar API",
    description = "Discover and verify ongoing and upcoming crypto catalysts.",
    version = "0.1.0",
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "market-calendar",
    }

@app.get("/")
def root():
    return{
        "message": "Welcome to Market-Calendar API",
        "docs": "/docs",
    }