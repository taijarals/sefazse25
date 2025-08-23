import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date, datetime

st.set_page_config(page_title="Plano de Voo: Auditor TI SEFAZ/SE", layout="wide")

# ======= HEADER =======
st.title("🚀 Plano de Voo: SEFAZ/SE")
st.markdown("Foco, força e fé na sua aprovação!")

# ======= PAINEL =======
st.header("📊 Painel de Controle")

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
    st.write(f"{st.session_state.progress}% concluído")

# Foco do dia
with col3:
    st.subheader("Foco do Dia")
    st.info("📌 Direito Tributário")

# ======= ANÁLISE =======
st.header("📈 Análise Estratégica do Edital")

exam_data = {
    "Prova": ["Conhecimentos Específicos II (TI - P3)", "Prova Discursiva (TI - P4)", "Conhecimentos Específicos I (P2)", "Conhecimentos Gerais (P1)"],
    "Peso": [90, 80, 100, 10]
}
df_exam = pd.DataFrame(exam_data)
fig = px.pie(df_exam, names="Prova", values="Peso", title="Distribuição de Pontos no Concurso")
st.plotly_chart(fig, use_container_width=True)

# ======= CRONOGRAMA =======
st.header("📅 Cronograma de Estudos")

schedule = {
    "Segunda": ["Português", "Raciocínio Lógico", "Exercícios"],
    "Terça": ["Constitucional", "Contabilidade", "Admin"],
    "Quarta": ["Custos", "Exercícios", "Empresarial"],
    "Quinta": ["AFO", "Exercícios", "Sergipe"],
    "Sexta": ["Revisão", "Exercícios", "Tributário"],
}
df_schedule = pd.DataFrame(schedule, index=["Manhã", "Tarde", "Noite"])
st.dataframe(df_schedule)

# ======= EDITAL =======
st.header("📖 Edital Verticalizado")

import pandas as pd
import streamlit as st

if "syllabus" not in st.session_state:
    #st.session_state.syllabus = pd.read_csv("syllabus.txt")
    st.session_state.syllabus = pd.read_csv("syllabus.csv", sep="|")


#if "syllabus" not in st.session_state:
#    st.session_state.syllabus = pd.DataFrame([
#        
#    ])

# --- FILTROS ---
st.subheader("Filtrar por:")
areas = st.multiselect("Área", options=st.session_state.syllabus["Área"].unique(), default=st.session_state.syllabus["Área"].unique())
grupos = st.multiselect("Grupo", options=st.session_state.syllabus["Grupo"].unique(), default=st.session_state.syllabus["Grupo"].unique())

# Aplica filtros
filtered_df = st.session_state.syllabus[
    (st.session_state.syllabus["area"].isin(areas)) &
    (st.session_state.syllabus["Grupo"].isin(grupos))
]

# Exibe editor com filtro aplicado
edited_df = st.data_editor(filtered_df, num_rows="dynamic", use_container_width=True)

# Atualiza o session_state mantendo os dados completos
for idx in edited_df.index:
    st.session_state.syllabus.loc[idx] = edited_df.loc[idx]

# Resumo
concluidos = edited_df["Concluído"].sum()
total = len(edited_df)
st.success(f"📌 Você concluiu {concluidos}/{total} tópicos do edital!")
