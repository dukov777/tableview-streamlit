import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "command": ["ls -l", "pwd", "echo Hello"]
})

st.title("Simple Table with Row Selection")

# Show the table with index and enable selection
event = st.dataframe(df, use_container_width=True, 
                    height=200, selection_mode="multi-row",
                    on_select="rerun")

# Check if rows are selected and display their indices
if event.selection and event.selection.rows:
    selected_indices = event.selection.rows
    st.write("Selected row indices:", selected_indices)

    # If you want to access the data of selected rows
    selected_data = df.iloc[selected_indices]
    st.write("Selected data:")
    st.write(selected_data)
