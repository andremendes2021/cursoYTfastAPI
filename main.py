from fastapi import FastAPI
import random

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco": 4, "qt": 5},
    2: {"item": "garrafa", "preco": 2, "qt": 3},
    3: {"item": "latinha", "preco": 3, "qt": 1},
}

@app.get("/")
async def root():
    return {"Vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda:int):
    if id_venda in vendas:
        return vendas[id_venda]
    else:
        return {"Erro": "Venda inexistente."}
    
@app.get("/random")
async def get_random():
    rn = random.randint(0, 100)
    return {"Random": rn, "Limit": 100}

@app.get("/random/{limit}")
async def get_random(limit:int):
    rn = random.randint(0, limit)
    return {"Random": rn, "Limit": limit}