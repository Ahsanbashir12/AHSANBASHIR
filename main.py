import streamlit as st
with st.form('form'):
    st.write('please fill the form')
    name=st.text_input('name')
    collage_name=st.text_input('your collage name')
    percentage=st.number_input('your percentage')
    working=st.checkbox('are your working')
    submitted=st.form_submit_button('submit')
    if submitted:
        st.write('name:',name)
        st.write('collage_name:',collage_name)
        st.write('percentage:',percentage)
        st.write('are u working',working)
