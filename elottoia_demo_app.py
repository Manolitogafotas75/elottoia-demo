import streamlit as st
import random

st.set_page_config(page_title="ElottoIA DEMO", layout="centered")

st.title("🎰 ElottoIA - Versión Demo")
st.markdown("Bienvenido a la versión de prueba de ElottoIA.")
st.markdown("**Solo está disponible el modo de generación Aleatorio.**")
st.markdown("")

st.markdown(("> 🧪 **Si quieres disfrutar de todas las ventajas que ofrece nuestra versión extendida y mejorada, prueba la versión web completa por tan solo 4,99 € en el Botón Verde de versión completa.
Pulsa aqui para volver a la página anterior (https://elottoia-landing.onrender.com//)**")

# Idioma
lang = st.selectbox("🌐 Idioma / Language", ["Español", "English"])

# Traducciones simples
texts = {
    "Español": {
        "generate": "Generar combinación",
        "result": "Combinación generada:"
    },
    "English": {
        "generate": "Generate combination",
        "result": "Generated combination:"
    }
}

t = texts[lang]

# Generar combinación aleatoria
if st.button(t["generate"]):
    numeros = sorted(random.sample(range(1, 51), 5))
    estrellas = sorted(random.sample(range(1, 13), 2))
    st.success(f'{t["result"]}')
    st.write("🔢 Números:", ", ".join(map(str, numeros)))
    st.write("⭐ Estrellas:", ", ".join(map(str, estrellas)))
