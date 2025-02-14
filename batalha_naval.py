import streamlit as st
import pandas as pd

# Configuração inicial
st.title("⚓ Batalha Naval de Vendas 🚀")
st.subheader("Acompanhe as vendas e veja qual equipe vencerá a batalha!")

# Inicializar pontuação
if "pontos_azul" not in st.session_state:
    st.session_state.pontos_azul = 90  # Alterado para 90
if "pontos_vermelho" not in st.session_state:
    st.session_state.pontos_vermelho = 90  # Alterado para 90

# Escolha entre Administrador e Usuário Comum
user_type = st.sidebar.radio("Selecione o modo de acesso:", ["Usuário", "Administrador"])

if user_type == "Administrador":
    admin_code = st.sidebar.text_input("🔑 Código de Administrador", type="password")
    if admin_code == "secreto123":  # Altere para o código que quiser
        st.sidebar.subheader("⚙️ Painel do Administrador")
        
        # Botão para resetar o jogo
        if st.sidebar.button("🔄 Resetar Pontos"):
            st.session_state.pontos_azul = 90
            st.session_state.pontos_vermelho = 90
            st.success("🔥 O jogo foi resetado!")

        # Ajustar manualmente os pontos
        pontos_azul = st.sidebar.number_input("Ajustar pontos do Time Azul", 0, 1000, st.session_state.pontos_azul)
        pontos_vermelho = st.sidebar.number_input("Ajustar pontos do Time Vermelho", 0, 1000, st.session_state.pontos_vermelho)
        
        if st.sidebar.button("💾 Atualizar Pontos"):
            st.session_state.pontos_azul = pontos_azul
            st.session_state.pontos_vermelho = pontos_vermelho
            st.success("✅ Pontos atualizados com sucesso!")
    else:
        st.warning("Código de Administrador incorreto!")

else:
    # Input para registrar vendas (Usuários Comuns)
    st.sidebar.header("Registrar Venda")
    vendedor = st.sidebar.text_input("Nome do Vendedor")
    equipe = st.sidebar.selectbox("Equipe", ["Azul", "Vermelho"])
    tipo_venda = st.sidebar.selectbox("Tipo de Venda", ["Pequena (1 ponto)", "Média (2 pontos)", "Grande (3 pontos)"])

    # Mapeamento de pontos
    pontos_map = {"Pequena (1 ponto)": 1, "Média (2 pontos)": 2, "Grande (3 pontos)": 3}

    if st.sidebar.button("Registrar Venda"):
        if vendedor and equipe:
            pontos_remover = pontos_map[tipo_venda]
            
            if equipe == "Azul":
                st.session_state.pontos_vermelho -= pontos_remover
            else:
                st.session_state.pontos_azul -= pontos_remover
            
            st.success(f"Venda registrada! {equipe} causou {pontos_remover} de dano!")
        else:
            st.warning("Preencha todos os campos para registrar a venda!")

# Exibir placar
st.header("Placar Atual")
st.write(f"### 🌊 Time Azul: {st.session_state.pontos_azul} pontos")
st.write(f"### 🔥 Time Vermelho: {st.session_state.pontos_vermelho} pontos")

# Verificar se algum time venceu
if st.session_state.pontos_azul <= 0:
    st.success("🔥 Time Vermelho venceu a batalha! 🎉")
    st.session_state.pontos_azul = 90
    st.session_state.pontos_vermelho = 90
elif st.session_state.pontos_vermelho <= 0:
    st.success("🌊 Time Azul venceu a batalha! 🎉")
    st.session_state.pontos_azul = 90
    st.session_state.pontos_vermelho = 90
