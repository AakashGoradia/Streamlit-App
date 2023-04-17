import streamlit as st

st.title("Fill Your Details")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

with st.form("my_form"):
   st.write("Basic Details")
   
   slider_val = st.slider("Input your Age")
   
   option = st.selectbox('Your Gender Please',('Male', 'Female', 'Other'))
   st.write('You selected:', option)
   
   checkbox_val = st.checkbox("I agree")
   
   submitted = st.form_submit_button("Submit")
#    if submitted:
#        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
