import streamlit as st

# Adding a title to the app
st.title("My First Streamlit App")

st.write("Hello, world!")
st.write("This is my first Streamlit app.")
st.write("I am excited to learn more about Streamlit and build amazing applications.")

# user input
number=st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {number}")
st.write("This is a simple slider to select a number between 0 and 100.")

#add a button
if st.button("Click me!"):
    st.write("Button clicked!")
    st.write("You can use buttons to trigger actions in your app.")

#add radio button with options
options = ["Option 1", "Option 2", "Option 3"]
selected_option = st.radio("Select an option", options)
st.write(f"You selected: {selected_option}")
st.write("Radio buttons are useful for selecting one option from a list.")

#add a dropdown list on th left sidebar
st.sidebar.selectbox("How would you like to be contacted?",("Email","Mobile Phone","Home Phone" ))

#add your whatsapp number
st.sidebar.text_input("Enter your WhatsApp number", "e.g. +1234567890")

# add a file uploader
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "txt"])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)
    st.write("You can upload files to your app using the file uploader.")

