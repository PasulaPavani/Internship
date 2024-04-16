from openai import  OpenAI

import streamlit as st
import base64
            # Set background image
@st.cache_data
def get_img_as_base64(file):
        with open(file, "rb") as f:
           data = f.read()
        return base64.b64encode(data).decode()
img = get_img_as_base64("python1.png")
        # data:image/png;base64,{img}
bg_image = f"""
        <style>
        [data-testid="stAppViewContainer"]  {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100% 100%;
         background-repeat: no-repeat;
         background-position : cover;
            }}
        </style>
        """      
st.markdown(bg_image, unsafe_allow_html=True) 
# Use CSS to change the text color

###
st.title("CodeCompanion")
##
f=open(r"C:/Users/LENOVO/Downloads/open.txt")
key = f.read().strip()
client = OpenAI(api_key=key)

prompt=st.text_area("Enter your python code... 🐍")

if st.button("Generate")==True:
    st.spinner("Please wait...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Give the bugs is exists in the code with a side heading and Give the correct code for the given code"},
            {"role": "user", "content": prompt}
        ]
    )

    st.header("Review of your code goes here ..")
    st.write(response.choices[0].message.content)