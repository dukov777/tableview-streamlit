import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {"name": ["Alice", "Bob", "Charlie"], "command": ["ls -l", "pwd", "echo Hello"]}
)

st.title("Simple Table with Row Selection")

# Add a flag to session state to track if we should clear selection
if "should_clear_selection" not in st.session_state:
    st.session_state.should_clear_selection = False

# Add a button to clear selection
if st.button("Clear Selection"):
    # toggle the flag
    st.session_state.should_clear_selection = not st.session_state.should_clear_selection
    st.rerun()

# Generate a dynamic key based on the clear selection flag
dataframe_key = f"dataframe_{st.session_state.should_clear_selection}"

event = st.dataframe(
    df,
    use_container_width=True,
    height=200,
    selection_mode="multi-row",
    on_select="rerun",
    key=dataframe_key,
)

# Check if rows are selected and display their indices
if event.selection and event.selection.rows:
    selected_indices = event.selection.rows
    st.write("Selected row indices:", selected_indices)

    # If you want to access the data of selected rows
    selected_data = df.iloc[selected_indices]
    st.write("Selected data:")
    st.write(selected_data)
