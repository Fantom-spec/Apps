def my_func():
    import streamlit as st
    st.header("English")
    st.write("-----------------------------------------")
    st.title("Select Chapter:- ")
    st.write('')
    st.write('' )
    st.title("FLAMINGO")
    prose=["THE LAST LESSON","LOST SPRING","DEEP WATER","THE RATTRAP","INDIGO","POETS AND PANCAKES","THE INTERVIEW","GOING PLACES"]
    poem=["MY MOTHER AT SIXTY-SIX","AN ELEMENTARY SCHOOL CLASSROOM IN A SLUM","KEEPING QUIET","A THING OF BEAUTY","A ROADSIDE STAND","AUNT JENNIFER’S TIGERS"]
    st.subheader("Prose")
    prose_choose=st.selectbox("Chapters",("Select Chapter",prose[0],prose[1],prose[2],prose[3],prose[4],prose[5],prose[6],prose[7]))
    if prose_choose==prose[0]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[1]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[2]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[3]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[4]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[5]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[6]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==prose[7]:
        st.write("Will be updates when the topic is taught in class.")
    st.subheader("Poem")
    poem_choose=st.selectbox("Chapters",("Select Chapter",poem[0],poem[1],poem[2],poem[3],poem[4],poem[5]))
    if prose_choose==poem[0]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==poem[1]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==poem[2]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==poem[3]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==poem[4]:
        st.write("Will be updates when the topic is taught in class.")
    elif prose_choose==poem[5]:
        st.write("Will be updates when the topic is taught in class.")
    
    
    
    
