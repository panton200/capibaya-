import streamlit as st

# Configura el título de la pestaña del navegador
st.set_page_config(page_title="Para mi capibaya", page_icon="❤️")

# Título principal con diseño
st.title("❤️ te amo mucho")

st.write("Hola, quería recordarte lo mucho que significas para mí.. 🥰")

# --- SECCIÓN INTERACTIVA ---
st.subheader("¿Me concedes una pregunta?")
respuesta = st.radio("¿Quieres salir conmigo este  domingo hacer mash y mancharme de rojo  puchaino?", ["Selecciona una opción...", "¡Sí, me encantaría!", "¡Por supuesto que sí!"])

if respuesta != "Selecciona una opción...":
    # ¡Esto lanza globos flotando por toda la pantalla!
    st.balloons()
    
    st.success("¡Sabía que dirías que sí! 🥳 Prepárate para tu pisada de nuca .")
    
    # Un cuadro con una nota bonita
    st.info("💡 **Nota de amor:** Cada día a tu lado es mi momento favorito . ¡Te amo!")