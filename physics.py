def my_func():
    import streamlit as st
    st.header("Physics")
    st.write("-----------------------------------------")
    st.title("Part I")
    st.write('')
    st.write('' )
    chap=["ELECTRIC CHARGES AND FIELDS","ELECTROSTATIC POTENTIAL AND CAPACITANCE","CURRENT ELECTRICITY","MOVING CHARGES AND MAGNETISM","MAGNETISM AND MATTER","ELECTROMAGNETIC INDUCTION","ALTERNATING CURRENT ","ELECTROMAGNETIC WAVES"]
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
    st.write('')
    st.write('' )
    st.title("Part II")
    st.write('')
    st.write('')
    chap1=["RAY OPTICS AND OPTICAL INSTRUMENTS","WAVE OPTICS","DUAL NATURE OF RADIATION AND MATTER","ATOMS","NUCLEI","SEMICONDUCTOR ELECTRONICS: MATERIALS, DEVICES AND SIMPLE CIRCUITS"]
    chap1_choose=st.selectbox("Chapters",("Select Chapter",chap[0],chap[1],chap[2],chap[3],chap[4],chap[5]))
    if chap1_choose==chap[0]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap1_choose==chap[1]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap1_choose==chap[2]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap1_choose==chap[3]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap1_choose==chap[4]:
        st.write("Will be updates when the topic is taught in class.")
    elif chap1_choose==chap[5]:
        st.write("Will be updates when the topic is taught in class.")
