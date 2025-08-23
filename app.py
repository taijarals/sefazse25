import streamlit as st
import pandas as pd
from datetime import datetime

# Título
st.title("📚 Acompanhamento de Estudos")

# Sessão para adicionar estudo
st.header("➕ Adicionar registro de estudo")
with st.form("form_estudo"):
    materia = st.text_input("Matéria/Assunto")
    tempo = st.number_input("Tempo de estudo (em horas)", min_value=0.5, step=0.5)
    data = st.date_input("Data", datetime.today())
    submit = st.form_submit_button("Salvar")

# Inicializa histórico na sessão
if "historico" not in st.session_state:
    st.session_state["historico"] = []

# Salva registro
if submit and materia and tempo:
    st.session_state["historico"].append({
        "Matéria": materia,
        "Tempo (h)": tempo,
        "Data": data.strftime("%d/%m/%Y")
    })
    st.success("✅ Registro adicionado!")

# Mostra histórico
st.header("📊 Histórico de Estudos")
if st.session_state["historico"]:
    df = pd.DataFrame(st.session_state["historico"])
    st.dataframe(df)

    # Estatísticas
    total_horas = df["Tempo (h)"].sum()
    st.metric("Total de horas estudadas", f"{total_horas:.1f}h")
else:
    st.info("Nenhum estudo registrado ainda.")
