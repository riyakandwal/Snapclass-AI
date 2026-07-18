import streamlit as st

from src.database.db import create_subject


@st.dialog("Create new subject")
def create_subject_dialog(teacher_id):
    st.write("enter the details of new subject")
    sub_id=st.text_input("subject code",placeholder='CS101')
    sub_name=st.text_input("subject name",placeholder='Introduction to computer science')
    sub_section=st.text_input("section",placeholder='A')


    if st.button('Create subject now',type='primary',width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject created successfully!!")
                st.rerun()

            except Exception as e:
                st.error(f"Error : {str(e)}")
        else:
            st.warning("Please fill all the fields")