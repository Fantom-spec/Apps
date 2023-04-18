import streamlit as st
import streamlit_option_menu as option_menu
import eng_flamingo
import eng_vistas
import physics
import chem
import maths
import cs
st.set_page_config(page_title="School Notes",page_icon=":books:",layout="wide")
with st.sidebar:
    choose = option_menu("Menu", ["Home", "English", "Physics", "Chemistry", "Mathematics","Computer Science"],
                         icons=['house', 'book','book','book','book','book'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "orange", "font-size": "16px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "lime"}})
if choose =="Home":
    st.title("Notes Chaplo")
    st.subheader("For Notes, Select Chapter in Menu")
    with st.container():
        st.write("--------")
        left_column, right_column =st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("#")
        st.write("sdads")
elif choose == "English":
    eng_flamingo.my_func()
    eng_vistas.my_func()
elif choose == "Physics":
    physics.my_func()
elif choose =="Chemistry":
    chem.my_func()
elif choose =="Mathematics":
    maths.my_func()
elif choose =="Computer Science":
    cs.my_func()
    

    
