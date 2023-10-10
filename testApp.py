import streamlit as st
import pandas as pd
import os
# from langchain.agents import create_csv_agent
# from langchain.llms import OpenAI

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

st.title('File Interpreter App')

#upload file tab 
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt", "xlsx","pdf"])

if uploaded_file is not None:
    st.write(" Uploaded format is " + uploaded_file.type)
    if "csv" in uploaded_file.type :
        st.write(" Uploaded file is csv ")
        with open(os.path.join("temp", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.read())
        # Read the CSV file
        df = pd.read_csv(os.path.join("temp", uploaded_file.name))
        st.write(" Error is here")
        st.write(df.head())

#create an agent
# agent = create_csv_agent(OpenAI(temperature=0), uploaded_file.name , verbose=True, max_iterations=30)



# if uploaded_file is not None:
#     # Display some information about the uploaded file
#     st.write("File details:")
#     st.write(f"Filename: {uploaded_file.name}")
#     st.write(f"File type: {uploaded_file.type}")
#     st.write(f"File size (bytes): {uploaded_file.size}")

#     # You can also read and display the contents of the file
#     st.write("File contents:")
    
#     st.write(data)
