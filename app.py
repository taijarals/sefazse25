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

if "syllabus" not in st.session_state:
    st.session_state.syllabus = pd.DataFrame([
        # ---- LÍNGUA PORTUGUESA ----
        {"Código": "1", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Compreensão e interpretação de textos de gêneros variados", "Assunto": "-", "Concluído": False},
        {"Código": "2", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Reconhecimento de tipos e gêneros textuais", "Assunto": "-", "Concluído": False},
        {"Código": "3", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da ortografia oficial", "Assunto": "-", "Concluído": False},
        {"Código": "4", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio dos mecanismos de coesão textual", "Assunto": "Emprego de elementos de referenciação, substituição e repetição, de conectores e de outros elementos de sequenciação textual", "Concluído": False},
        {"Código": "4.2", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio dos mecanismos de coesão textual", "Assunto": "Emprego de tempos e modos verbais", "Concluído": False},
        {"Código": "5", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "-", "Concluído": False},
        {"Código": "5.1", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Emprego das classes de palavras", "Concluído": False},
        {"Código": "5.2", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Relações de coordenação entre orações e entre termos da oração", "Concluído": False},
        {"Código": "5.3", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Relações de subordinação entre orações e entre termos da oração", "Concluído": False},
        {"Código": "5.4", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Emprego dos sinais de pontuação", "Concluído": False},
        {"Código": "5.5", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Concordância verbal e nominal", "Concluído": False},
        {"Código": "5.6", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Regência verbal e nominal", "Concluído": False},
        {"Código": "5.7", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Emprego do sinal indicativo de crase", "Concluído": False},
        {"Código": "5.8", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Domínio da estrutura morfossintática do período", "Assunto": "Colocação dos pronomes átonos", "Concluído": False},
        {"Código": "6", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Reescrita de frases e parágrafos do texto", "Assunto": "-", "Concluído": False},
        {"Código": "6.1", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Reescrita de frases e parágrafos do texto", "Assunto": "Significação das palavras", "Concluído": False},
        {"Código": "6.2", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Reescrita de frases e parágrafos do texto", "Assunto": "Substituição de palavras ou de trechos de texto", "Concluído": False},
        {"Código": "6.3", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Reescrita de frases e parágrafos do texto", "Assunto": "Reorganização da estrutura de orações e de períodos do texto", "Concluído": False},
        {"Código": "6.4", "Grupo": "Geral", "Área": "LÍNGUA PORTUGUESA", "Subárea": "Reescrita de frases e parágrafos do texto", "Assunto": "Reescrita de textos de diferentes gêneros e níveis de formalidade", "Concluído": False},

        # ---- CONHECIMENTOS SOBRE O ESTADO DE SERGIPE ----
        {"Código": "1", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Indígenas em Sergipe", "Assunto": "-", "Concluído": False},
        {"Código": "2", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Processo de ocupação e povoamento do território sergipano", "Assunto": "-", "Concluído": False},
        {"Código": "3", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Economias fundadoras", "Assunto": "-", "Concluído": False},
        {"Código": "4", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Regiões geoeconômicas", "Assunto": "-", "Concluído": False},
        {"Código": "5", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Estrutura do poder e a sociedade colonial sergipana", "Assunto": "-", "Concluído": False},
        {"Código": "6", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Sergipe nas sucessivas fases da República Brasileira", "Assunto": "-", "Concluído": False},
        {"Código": "7", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Condicionantes geoambientais (clima, recursos minerais, relevo e solo, recursos hídricos, vegetação)", "Assunto": "-", "Concluído": False},
        {"Código": "8", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Dinâmica populacional", "Assunto": "-", "Concluído": False},
        {"Código": "9", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Rede urbana e organização do espaço", "Assunto": "-", "Concluído": False},
        {"Código": "10", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Formação metropolitana de Aracaju", "Assunto": "-", "Concluído": False},
        {"Código": "11", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Política, sociedade e economia no Sergipe contemporâneo", "Assunto": "-", "Concluído": False},
        {"Código": "12", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Potencialidades e perspectivas para o desenvolvimento econômico e social", "Assunto": "-", "Concluído": False},
        {"Código": "13", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Formação e expressão da cultura sergipana", "Assunto": "-", "Concluído": False},
        {"Código": "14", "Grupo": "Geral", "Área": "CONHECIMENTOS SOBRE O ESTADO DE SERGIPE", "Subárea": "Educação em Sergipe", "Assunto": "-", "Concluído": False},
    ])


edited_df = st.data_editor(st.session_state.syllabus, num_rows="dynamic", use_container_width=True)
st.session_state.syllabus = edited_df

# Resumo
concluidos = edited_df["Concluído"].sum()
total = len(edited_df)
st.success(f"📌 Você concluiu {concluidos}/{total} tópicos do edital!")
