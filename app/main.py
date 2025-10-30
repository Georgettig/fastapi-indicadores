from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from app.utils import calcular_indicadores

app = FastAPI(
    title = "API de Indicadores de Vendas",
    description = "Envie um arquivo CSV para visualizar os KPI's automaticamente"
)

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="O arquivo precisa ser CSV.")

    df = pd.read_csv(file.file)

    colunas_necessarias = {"Produto","Categoria","Preço","Vendedor"}
    if not colunas_necessarias.issubset(df.columns):
        raise HTTPException(status_code=400, detail=f"O arquivo precisa conter as colunas: {', '.join(colunas_necessarias)}")

    indicadores = calcular_indicadores(df)
    return {"indicadores":indicadores}

@app.get("/")
def home():
    return {"mensagem":"API de Indicadores de Vendas - envie um arquivo CSV em /upload"}