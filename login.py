# login.py
import streamlit as st
from firebase_config import auth


def login():
    st.subheader("Inicio de Sesión")

    email = st.text_input("Correo Electrónico", key="login_email")
    password = st.text_input("Contraseña", type="password", key="login_password")

    if st.button("Iniciar Sesión"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Inicio de sesión exitoso")
            return user
        except:
            st.error("Correo o contraseña incorrectos")

    return None


def logout():
    if st.button("Cerrar Sesión"):
        st.session_state.pop('user', None)
        st.success("Sesión cerrada")


def register():
    st.subheader("Registro de Usuario")

    email = st.text_input("Correo Electrónico", key="register_email")
    password = st.text_input("Contraseña", type="password", key="register_password")
    password_confirm = st.text_input("Confirmar Contraseña", type="password", key="register_password_confirm")

    if st.button("Registrarse"):
        if password != password_confirm:
            st.error("Las contraseñas no coinciden")
        else:
            try:
                user = auth.create_user_with_email_and_password(email, password)
                st.success("Registro exitoso, por favor inicie sesión")
                return user
            except:
                st.error("Error en el registro, por favor intente de nuevo")
    return None