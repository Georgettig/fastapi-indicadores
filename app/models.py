from pydantic import BaseModel, Field
from typing import Dict

class Indicadores(BaseModel):
    faturamento_total: str = Field(..., example="R$ 10.000,00")
    ticket_medio: str = Field(..., example="R$ 100,00")
    receita_vendedor: Dict[str,str] = Field(...,example={"Fulano":"R$ 1.000,00", "Siclano":"R$ 2.000,00"})
    receita_categoria: Dict[str,str] = Field(...,example={"Celular":"R$ 1.000,00", "Notebook":"R$ 2.000,00"})

class IndicadoresResposne(BaseModel):
    indicadores: Indicadores