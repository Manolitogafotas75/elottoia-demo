import streamlit as st
import random

st.set_page_config(page_title="ElottoIA DEMO", layout="centered")

st.title("🎰 ElottoIA - Versión Demo")
st.markdown("Bienvenido a la versión de prueba de ElottoIA.")
st.markdown("**En esta demo solo está disponible el modo de generación Aleatorio.**")

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

# Botón justo debajo de la explicación del modo aleatorio
if st.button(t["generate"]):
    numeros = sorted(random.sample(range(1, 51), 5))
    estrellas = sorted(random.sample(range(1, 13), 2))
    st.success(f'{t["result"]}')
    st.write("🔢 Números:", ", ".join(map(str, numeros)))
    st.write("⭐ Estrellas:", ", ".join(map(str, estrellas)))

st.markdown("---")

st.markdown("""
💡 **¿Quieres más funciones, inteligencia artificial y estadísticas avanzadas?**

Disfruta de la versión completa de ElottoIA por solo **4,99 €** y accede a:
- Modos de generación por Frecuencia e IA Híbrida
- Análisis estadístico completo
- Filtros avanzados
- Exportación y guardado de combinaciones
""")

st.markdown("")
st.markdown("⬇️ Haz clic aquí para acceder a la versión completa:")

# Botón verde con redirección
if st.button("🌟 Ir a la Versión Completa (Premium)", type="primary"):
    st.markdown(
        """<meta http-equiv="refresh" content="0; url='https://manolitogafotas75.github.io/elottoia-premium-login/'">""",
        unsafe_allow_html=True
    )

