import streamlit as st
from pymongo import MongoClient

import validateEmail as validateEmail
import hash as hash

client = MongoClient('localhost', 27017)
db = client['predict-covid']
collection = db['user-data']


def main():

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Passwrod", type="password")
    if st.button("SignUp"):
        if username and email and password:
            if collection.find_one({'Email': email}):
                st.error('This email is taken, please try again with a different email')

            if validateEmail.validateEmail(email):
                st.info("Valid Email")

                haheshPassword = hash.make_hashes(password)
                collection.insert_one({'username': username, 'email': email, 'password':haheshPassword})
                st.info('Signed Up, please login from the sidebar')


if __name__ == "__main__":
    main()