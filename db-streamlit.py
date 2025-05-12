import streamlit as st
import pandas as pd
from sqlalchemy import text
from datetime import timedelta


conn = st.connection('example', type='sql', ttl=1)
pet_owners = conn.query("SELECT * FROM users", ttl=1)
st.dataframe(pet_owners)

def add_data():
    name = st.session_state.name
    with conn.session as s:
        email = f"{name}@vmvmvm.com"
        s.execute(text("INSERT INTO users (name, email) VALUES (:name, :email) ON CONFLICT (email) DO NOTHING"), {"name": name, "email": email})
        s.commit()

st.text_input("name", key="name", on_change=add_data)
