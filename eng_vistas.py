def my_func():
    import streamlit as st
    st.write('')
    st.write('')
    st.title("VISTAS")
    chap=["The Third Level","The Tiger King","Journey to the end of the Earth","The Enemy","Should Wizard hit Mommy","On the face of it","Evans Tries an O-Level","Memories of Childhood"]
    chap_choose=st.selectbox("Chapters",("Select Chapter",chap[0],chap[1],chap[2],chap[3],chap[4],chap[5],chap[6],chap[7]))
    if chap_choose==chap[0]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[1]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[2]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[3]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[4]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[5]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[6]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap_choose==chap[7]:
        st.write("Will be updates when the topic is taught in class.")
