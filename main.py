import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian","Mexican","Italian","Arabic","American","Chinese","Japanese","Korean"))

if cuisine:
        response = langchain_helper.generate_name(cuisine)
        st.header(response['restaurant_name'].strip())
        menu_items = response["menu_items"].strip().split("\n")
        st.write("**Menu Items**")
        for item in menu_items:
            st.write(item)