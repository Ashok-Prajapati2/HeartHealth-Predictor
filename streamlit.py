import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Inject custom CSS
custom_css = """
<style>
/* Change the background color of the entire app */
body {
    background-color:rgb(71, 14, 14);
}

/* Style the header */
header {
    font-family: 'Arial', sans-serif;
    font-size: 24px;
    color: #333333;
    text-align: center;
    margin-bottom: 20px;
}

/* Customize buttons */
button {
    background-color:rgb(22, 135, 255);
    color: white;
    font-size: 16px;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

/* Customize input boxes */
input, textarea {
    border: 2px solid #cccccc;
    padding: 10px;
    border-radius: 5px;
}

/* Highlight primary buttons */
.stButton>button {
    background-color:rgb(77, 58, 216);
    color: white;
    border-radius: 10px;
    font-size: 16px;
}
markdown {
    background-color: rgb(249, 0, 0);
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}
</style>
"""

# Apply CSS using st.markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit app content
st.title("Custom CSS in Streamlit")
st.button("Click Me")
st.text_input("Enter text:")
st.text_area("Enter multiline text:")


st.title('This is the movie recommendation website')
st.header("This is header")
st.markdown("This is markdown")
st.success("This is success")
st.info("This is info")
st.warning("This is warning")
st.error("This is error")
st.write("This is write tag text")

from PIL import Image
img = Image.open("ashok.png")
st.image(img, width=50 , caption="Ashok")
if st.checkbox("show/Hide"):
    st.text("Show")

#radio Button 
status = st.radio("select Any",("A","B","C"))
if status == "A":
    st.success("A")
elif status == "B":
    st.info("B")
else:   
    st.error("C")

#selectbox
selectbox = st.selectbox("select",["A","B","C"])

#multiselect box 
multiselect = st.multiselect("select",["A","B","C"])

# #Button 
# if st.button("Submit"):
#     st.success("Submit")

#text input
name = st.text_input("Enter Name","Type Here..")
if st.button("Submit"):
    st.success(name)

#slider 

age = st.slider("Enter Age",1,100)
st.write("Your Age is ",age)

#file upload
file = st.file_uploader("Upload File")
if file is not None:
    df = pd.read_csv(file)
    # st.write(df)
    st.write(df.head(3))
    plt.figure(figsize=(10,5))
    plt.xlabel('Popularity')
    plt.ylabel('Budget')
    plt.scatter(df['popularity']/100,df['budget']/10000000,c='r',s=10,marker='*')
    plt.title('Popularity vs Budget')
    # st.pyplot()
    st.pyplot(plt)


#dataframe
df = pd.read_csv("data_movies.csv")
st.dataframe(df.head())    
#custom charts
df = pd.read_csv("data_movies.csv")
st.bar_chart(df['budget'])
st.line_chart(df['budget'])
st.area_chart(df['budget'])
st.scatter_chart(df['budget'])

#table
st.table(df.head(1))

#expander
with st.expander("Show"):
    st.write("Hello")

#columns
col1,col2 = st.columns(2)
col1.write("Hello")
col2.write("World")

#json
st.json({"Name":"Ashok","Age":24})

#plot
# df = pd.read_csv("data_movies.csv")
# fig, ax = plt.subplots()
# ax.bar(df['budget'],6)
# st.pyplot(fig)

#custom css 

st.markdown("""
<h1 style='color:red'>Hello World</h1>
<h2 style='color:blue'>Hello World</h2>
<h3 style='color:green'>Hello World</h3>
<label style='color:orange;font-size:50px'>Hello World</label><hr style='color:yellow'>
<input style='outline: 5px solid white; border-radius: 10px; color : blue'></input>

""",unsafe_allow_html=True)
