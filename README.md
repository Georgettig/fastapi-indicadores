# 📊 API de Indicadores Automáticos com FastAPI

Esta API, desenvolvida em **FastAPI**, permite o **upload de arquivos CSV** e retorna **indicadores calculados automaticamente**, como ticket médio, faturamento total, percentuais ou outros KPIs definidos.  
É ideal para automação de relatórios, dashboards e análises de desempenho a partir de planilhas corporativas.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** — Framework para APIs rápidas e modernas
- **Uvicorn** — Servidor ASGI de alto desempenho
- **Pandas** — Manipulação e análise de dados em Excel
- **Pydantic** — Validação de dados

---

## ⚙️ Funcionalidades

✅ Upload de planilhas Excel (`.xlsx`)  
✅ Processamento automático de dados com **Pandas**  
✅ Cálculo de indicadores e estatísticas  
✅ Retorno em formato **JSON**  
✅ Endpoint interativo em `/docs` (Swagger UI)  

---

## ▶️ Como rodar
Clone este repositório:
```bash
git clone https://github.com/Georgettig/fastapi-indicadores.git
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

