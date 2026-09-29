
import os
import tempfile

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent

def save_uploadedfile(uploaded_file):

    temp_dir = tempfile.mkdtemp()

    file_path = os.path.join(
        temp_dir,
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def generate_response(file_path, prompt):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0
    )

    plt.close("all")

    agent = create_csv_agent(
        llm,
        file_path,
        verbose=True,
        allow_dangerous_code=True
    )

    response = agent.invoke(prompt)
    figures = []

    for figure_number in plt.get_fignums():
        figure = plt.figure(figure_number)
        figures.append(figure)
    return response["output"], figures

def plot_exists(output, figures):

    if figures:

        for figure in figures:
            st.pyplot(figure)

        return output

    return output


def main():
    load_dotenv()
    API_KEY = os.environ["GOOGLE_API_KEY"]
    st.set_page_config(
        page_title="DATALENS")
    st.header("DATALENS")

    uploaded_file = st.file_uploader(
        "Upload a CSV file",type=["csv"]
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        path = save_uploadedfile(uploaded_file)
        st.dataframe(df)
        prompt = st.text_input("Enter your question:")
        if prompt:
            result, figures = generate_response(path,prompt)
            st.write( plot_exists(result,figures)
            )


if __name__ == "__main__":
    main()
