import streamlit as st

pages ={
    "Pages":
 [ 
    st.Page("pages/sleep.py", title="Mental Health"),
    st.Page("pages/stress.py", title="Stress"),
 ]
}
pg = st.navigation(pages)
pg.run()