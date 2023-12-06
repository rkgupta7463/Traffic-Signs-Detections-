import streamlit as st

## some important function
def prediction_func(image):
    return "Predicted your images!!!!"


st.title("Traffic Signals Detection using YOLOv8 Model")



# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How you want to detect?",
    ("Kindly select the type of data!","with File", "with streaming data"),
)

uploaded=None
s=None
t=None
# Using "with" notation
with st.sidebar:
    # st.write(add_selectbox)
    if add_selectbox=="with File":
        uploaded=st.file_uploader(label="upload your images")

    elif add_selectbox=="with streaming data":
        s=st.button("Click for Streaming")
    else:
        t=True
        st.write("select some things from the select boxes")

if t:
    st.image("images/Traffic-Signal-Lights.jpg")

if s:
    st.camera_input("Streaming your data with camera!")
    if s:
        c=st.button("Cancel streaming")
        if c:
            st.camera_input(disabled=True,label="Streaming your data with camera!")

if uploaded is not None:
    st.write("File has uploaded")
    i=st.image(uploaded)
    result=prediction_func(uploaded)
    st.write(result)    
    

