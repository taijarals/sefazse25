import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
from services.supabase_client import supabase

# Configuração da página
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

# ======= CARREGAR DADOS DO BANCO =======

@st.cache_data(ttl=600)
def load_syllabus():
    response = supabase.table("assuntos_estudo").select("*").execute()
    data = response.data if response.data else []

    if len(data) == 0:
        return pd.DataFrame(columns=[
            "id","codigo","grupo","area","subarea","assunto","concluido"
        ])

    return pd.DataFrame(data)


if "syllabus" not in st.session_state:
    st.session_state.syllabus = load_syllabus()

df = st.session_state.syllabus

# ======= PROGRESSO =======

total = len(df)
concluidos = df["concluido"].sum() if total > 0 else 0
progress = int((concluidos / total) * 100) if total > 0 else 0

with col2:
    st.subheader("Progresso Geral")
    st.progress(progress / 100)
    st.write(f"{progress}% concluído")

# Foco do dia
with col3:
    st.subheader("Foco do Dia")
    st.info("📌 Direito Tributário")

# ======= ANÁLISE =======

st.header("📈 Análise Estratégica do Edital")

exam_data = {
    "Prova": [
        "Conhecimentos Específicos II (TI - P3)",
        "Prova Discursiva (TI - P4)",
        "Conhecimentos Específicos I (P2)",
        "Conhecimentos Gerais (P1)"
    ],
    "Peso": [90, 80, 100, 10]
}

df_exam = pd.DataFrame(exam_data)

fig = px.pie(
    df_exam,
    names="Prova",
    values="Peso",
    title="Distribuição de Pontos no Concurso"
)

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

# ----- FILTROS -----

st.subheader("Filtrar por:")

areas = st.multiselect(
    "Área",
    options=df["area"].unique(),
    default=df["area"].unique()
)

grupos = st.multiselect(
    "Grupo",
    options=df["grupo"].unique(),
    default=df["grupo"].unique()
)

filtered_df = df[
    (df["area"].isin(areas)) &
    (df["grupo"].isin(grupos))
]

# ======= EDITOR =======

edited_df = st.data_editor(
    filtered_df,
    num_rows="dynamic",
    use_container_width=True,
    key="editor"
)

# ======= SALVAR ALTERAÇÕES =======

if st.button("💾 Salvar progresso"):
    
    for _, row in edited_df.iterrows():

        supabase.table("assuntos_estudo").update({
            "concluido": row["concluido"]
        }).eq("id", row["id"]).execute()

    st.success("Progresso salvo no banco!")

    st.cache_data.clear()
    st.session_state.syllabus = load_syllabus()

# ======= RESUMO =======

concluidos = edited_df["concluido"].sum()
total = len(edited_df)

st.success(f"📌 Você concluiu {concluidos}/{total} tópicos do edital!")