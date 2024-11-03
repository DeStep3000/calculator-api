from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в API калькулятора"}

@app.get("/add")
async def add(x: float, y: float):
    return {"result": x + y}

@app.get("/subtract")
async def subtract(x: float, y: float):
    return {"result": x - y}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Деление на ноль запрещено")
    return {"result": a / b}
#бу