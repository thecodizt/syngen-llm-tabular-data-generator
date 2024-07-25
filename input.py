import streamlit as st

def ui_input():

    st.subheader("Configurations")
    
    model = st.selectbox(label="Model", options=['mistral', 'vicuna'])
    
    base_context = st.text_input(
        "Provide a detailed description of the data to be generated",
    )
    
    num_records = st.number_input(
        label="Enter the number of records to be generated",
        min_value=1,
        step=1    
    )
    
    num_columns = st.number_input(
        label="Enter the number of columns in the expected data",
        min_value=1,
        step=1,
    )
    
    column_info = dict()
    
    # TODO: Do it in two columns
    
    for i in range(num_columns): 
        st.subheader(f"Column {i+1}")
        col_name = st.text_input(f"Enter name of column {i+1}", key=f"col_input_{i}")
        col_desc = st.text_input(f"Enter detailed description of column {i+1}", key=f"col_input_desc_{i}")
        is_primary = st.checkbox(f"Primary Key", key=f"primary_key_col_{i}")
        is_numeric = st.checkbox("Numeric Column", key=f"numeric_{i}")
        
        type = 'str'
        if is_numeric:
            type = "float"
        
        column_info[i] = {
            "col_name": col_name, 
            "col_desc": col_desc,
            "is_primary": is_primary,
            "type": type,
        }

    config = dict()
    config["llm_model"] = model
    config["base_context"] = base_context
    config["num_records"] = num_records
    config["num_columns"] = num_columns
    config["column_info"] = column_info
    
    return config