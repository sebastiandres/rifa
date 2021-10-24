import streamlit as st
import random

def carton_aleatorio():
    i = st.session_state.i
    st.session_state.carton[i] = random.randint(1, N_cartones)
    return 

def numero_aleatorio():
    i = st.session_state.i
    st.session_state.numero[i] = random.randint(1, N_numeros)
    return 

def asignar_premio():
    i = st.session_state.i
    st.session_state.premio[i] = st.session_state.premio_i
    return 

def asignar_ganador():
    i = st.session_state.i
    st.session_state.ganador[i] = "**"+st.session_state.ganador_i+"**"
    st.balloons()
    return 

# Set wide display
st.set_page_config(layout="wide")

# Settings
N_cartones = 2 # Cantidad de cartones en juego
N_numeros = 20 # Números por cada cartón
N_premios = 16 # Cantidad total de premios

if 'i' not in st.session_state:
    st.session_state.i = 1
if 'premio_i' not in st.session_state:
    st.session_state.premio_i = ""
if 'ganador_i' not in st.session_state:
    st.session_state.ganador_i = ""
if 'premio' not in st.session_state:
    st.session_state.premio = ["" for i in range(N_premios)]
if 'carton' not in st.session_state:
    st.session_state.carton = ["" for i in range(N_premios)]
if 'numero' not in st.session_state:
    st.session_state.numero = ["" for i in range(N_premios)]
if 'ganador' not in st.session_state:
    st.session_state.ganador = ["" for i in range(N_premios)]

# Title
c1, c2 = st.columns([10,2])
c1.title("Rifa - Sudamericano Gimnasia")
c1.subheader("Eloísa Campos - 24 Noviembre 2021")
c2.image("eloprogimnasta.png", width=100)
c2.caption("instagram: @eloprogimnasta")
# Configuration
c1, c2, c3 = st.columns([1, 3, 3])
i = int(c1.number_input("Sorteo", value=1, min_value=1, max_value=N_premios)) - 1
st.session_state.i = i
st.session_state.premio_i = c2.text_input("Premio", value=st.session_state.premio[i])
st.session_state.ganador_i = c3.text_input("Ganador", value=st.session_state.ganador[i])

# Buttons
_, c1, c2, c3, c4 = st.columns([1, 1, 1, 1, 3])
c1.button("Definir Premio", on_click=asignar_premio)
c2.button("Rifa Ganadora", on_click=carton_aleatorio)
c3.button("Número Ganador", on_click=numero_aleatorio)
c4.button("Asignar Nombre del Ganador", on_click=asignar_ganador)


# Content
for n in range(0, N_premios):
    c1, c2, c3, c4 = st.columns([2, 1, 1, 3])
    c1.write(f"Premio número {n+1:02d}: {st.session_state.premio[n]}")
    c2.write(f"Rifa: {st.session_state.carton[n]}")
    c3.write(f"Número: {st.session_state.numero[n]}")
    c4.write(f"Nombre del Ganador: {st.session_state.ganador[n]}")

