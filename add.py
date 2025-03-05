import streamlit as st

st.title("📇 Gestion des Contacts")
st.write("Bienvenue dans votre application de gestion des contacts !")

# Ajout d'un contact
nom = st.text_input("Nom du contact")
if st.button("Ajouter"):
    st.success(f"✅ {nom} ajouté avec succès !")
