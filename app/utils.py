import pandas as pd

def formatar_reais(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",","X").replace(".",",").replace("X",".")

def calcular_indicadores(df: pd.DataFrame):
    faturamento_total = df["Preço"].sum()
    total_vendas = len(df)
    ticket_medio = faturamento_total / total_vendas if total_vendas > 0 else 0
    receita_vendedor = df.groupby("Vendedor")["Preço"].sum().sort_values(ascending=False).to_dict()
    receita_categoria = df.groupby("Categoria")["Preço"].sum().sort_values(ascending=False).to_dict()

    receita_vendedor_formatada = {vendedor: formatar_reais(valor) for vendedor, valor in receita_vendedor.items()}
    receita_categoria_formatada = {categoria: formatar_reais(valor) for categoria, valor in receita_categoria.items()}

    return {
        "faturamento_total": formatar_reais(faturamento_total),
        "total_vendas": formatar_reais(total_vendas),
        "ticket_medio": formatar_reais(ticket_medio),
        "top_vendedores": receita_vendedor_formatada,
        "receita_por_categoria": receita_categoria_formatada,
    }