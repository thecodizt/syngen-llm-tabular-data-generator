import streamlit as st

from input import ui_input
from generate import generate

def few_shot():
    st.title("LLM Based Tabular Data Generator")
    st.subheader("Few Shot Inference")
    
    config = ui_input()
    
    with st.expander("Configuration"):
        st.write(config)
    
    isStartGenerate = st.button("Generate")
    
    if isStartGenerate:
        response = generate(config)
        
        if len(response) > 0:
            st.header("Generated Data")
            response.reset_index(drop=True, inplace=True)
            st.dataframe(response)
            
            payload = response.to_csv(index=False).encode('utf-8')
            
            st.download_button(label="Download", data=payload, file_name="generated_data.csv")
            
if __name__ == "__main__":
    few_shot()