def my_func():
    import streamlit as st
    st.header("Mathematics")
    st.write("-----------------------------------------")
    st.title("Part I")
    st.write('')
    st.write('' )
    chap=["RELATIONS AND FUNCTIONS","INVERSE TRIGONOMETRI FUNCTIONS","MATRICES","DETERMINANTS","CONTINUITY AND DIFFERENTIBILITY","APPLICATIONS OF DERIVATIVE"]
    chap_choose=st.selectbox("Chapters",("Select Chapter",chap[0],chap[1],chap[2],chap[3],chap[4],chap[5]))
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
    st.write('')
    st.write('' )
    st.title("Part II")
    st.write('')
    st.write('')
    chap1=["INTEGRALS","APPLICATION OF INTEGRALS","DIFFERENTIAL EQUATION","VECTOR ALGEBRA","THREE DIMENSIONAL GEOMETERY","LINEAR PROGRAMMING","PROBABILITY"]
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
