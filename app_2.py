import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, datetime
from pymongo import MongoClient  # <- adicione este import

st.set_page_config(page_title="Plano de Voo: Auditor TI SEFAZ/SE", layout="wide")

# =======================
# Conexão com MongoDB
# =======================
MONGO_URI = st.secrets["MONGO_URI"]
client = MongoClient(MONGO_URI)
db = client["syllabus_db"]
collection = db["syllabus"]

# =======================
# HEADER
# =======================
st.title("🚀 Plano de Voo: SEFAZ/SE")
st.markdown("Foco, força e fé na sua aprovação!")

# =======================
# PAINEL DE CONTROLE
# =======================
col1, col2, col3 = st.columns(3)

# Contagem regressiva
exam_date = date(2025, 9, 28)
days_left = (exam_date - date.today()).days
with col1:
    st.subheader("Contagem Regressiva")
    st.metric("Dias até a prova", f"{days_left} dias")

# Progresso geral
if "progress" not in st.session_state:
    st.session_state.progress = 0
with col2:
    st.subheader("Progresso Geral")
    st.progress(st.session_state.progress / 100)
    st.write(f"{st.session_state.progress}% concluido")

# Foco do dia
with col3:
    st.subheader("Foco do Dia")
    st.info("📌 Direito Tributário")

# =======================
# ANÁLISE E CRONOGRAMA
# =======================
# (mesmo código que você já tinha...)

# =======================
# EDITAL VERTICALIZADO (substituindo CSV pelo MongoDB)
# =======================
st.header("📖 Edital Verticalizado")

if "syllabus" not in st.session_state:
    # Busca dados do MongoDB
    data = list(collection.find({}, {"_id": 0}))  # ignora o _id do MongoDB
    if data:
        st.session_state.syllabus = pd.DataFrame(data)
    else:
        st.session_state.syllabus = pd.DataFrame(columns=["area", "grupo", "assunto", "concluido"])

# --- FILTROS ---
st.subheader("Filtrar por:")
areas = st.multiselect(
    "area", options=st.session_state.syllabus["area"].unique(), 
    default=st.session_state.syllabus["area"].unique()
)
grupos = st.multiselect(
    "grupo", options=st.session_state.syllabus["grupo"].unique(), 
    default=st.session_state.syllabus["grupo"].unique()
)

filtered_df = st.session_state.syllabus[
    (st.session_state.syllabus["area"].isin(areas)) &
    (st.session_state.syllabus["grupo"].isin(grupos))
]

edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True)

# Atualiza o session_state e o MongoDB
for idx in edited_df.index:
    st.session_state.syllabus.loc[idx] = edited_df.loc[idx]
    collection.update_one(
        {"assunto": edited_df.loc[idx, "assunto"]}, 
        {"$set": edited_df.loc[idx].to_dict()},
        upsert=True
    )

# Resumo
concluidos = edited_df["concluido"].sum()
total = len(edited_df)
st.success(f"📌 Você concluiu {concluidos}/{total} tópicos do edital!")
