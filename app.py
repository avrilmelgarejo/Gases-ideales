import streamlit as st
st.image("ley-de-los-gases-ideales-768x432-1.png")
# Constante universal de los gases
R = 0.0821  # L·atm/mol·K

st.title("Calculadora de la Ecuación de Gases Ideales")
st.write("Usa la ecuación PV = nRT para resolver una variable faltante.")

# Selección de la variable a calcular
opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    V = st.number_input("Ingresa el volumen (L)", min_value=0.01)
    n = st.number_input("Ingresa el número de moles (mol)", min_value=0.01)
    T = st.number_input("Ingresa la temperatura (K)", min_value=0.01)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es: {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Ingresa la presión (atm)", min_value=0.01)
    n = st.number_input("Ingresa el número de moles (mol)", min_value=0.01)
    T = st.number_input("Ingresa la temperatura (K)", min_value=0.01)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es: {V:.3f} L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Ingresa la presión (atm)", min_value=0.01)
    V = st.number_input("Ingresa el volumen (L)", min_value=0.01)
    n = st.number_input("Ingresa el número de moles (mol)", min_value=0.01)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es: {T:.3f} K")

elif opcion == "Número de moles (n)":
    P = st.number_input("Ingresa la presión (atm)", min_value=0.01)
    V = st.number_input("Ingresa el volumen (L)", min_value=0.01)
    T = st.number_input("Ingresa la temperatura (K)", min_value=0.01)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es: {n:.3f} mol")
