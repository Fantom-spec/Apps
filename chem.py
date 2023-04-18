def my_func():
    import streamlit as st
    st.header("Chemistry")
    st.write("-----------------------------------------")
    st.title("Part I")
    st.write('')
    st.write('' )
    chap=["THE SOLID STATE","SOLUTIONS","ELECTROCHEMISTRY","CHEMICAL KINETICS","SURFACE CHEMISTRY","GENERAL PRINCIPLES AND PROCESSES OF ISOLATION OF ELEMENTS","THE p-BLOCK ELEMENTS","THE d-AND f-BLOCK ELEMENTS","COORDINATION COMPOUNDS"]
    chap_choose=st.selectbox("Chapters",("Select Chapter",chap[0],chap[1],chap[2],chap[3],chap[4],chap[5],chap[6],chap[7],chap[8]))
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
    elif chap_choose==chap[8]:
        st.write("Will be updates when the topic is taught in class.")
    st.write('')
    st.write('' )
    st.title("Part II")
    st.write('')
    st.write('')
    chap1=["Haloalkanes and Haloarenes","Alcohols, Phenols and Ethers","Aldehydes, Ketones and Carboxylic Acids","Amines","Biomolecules","Polymers","Chemistry in Everyday Life"]
    chap1_choose=st.selectbox("Chapters",("Select Chapter",chap[0],chap[1],chap[2],chap[3],chap[4],chap[5],chap[6]))
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
    elif chap1_choose==chap[6]:
        st.write("Will be updates when the topic is taught in class.")
