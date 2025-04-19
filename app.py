import streamlit as st
import pandas as pd

# Initialize DataFrame in session_state if not present
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(
        {"name": ["Alice", "Bob", "Charlie"], "command": ["ls -l", "pwd", "echo Hello"]}
    )

if "textinput" not in st.session_state:
    st.session_state.textinput = ""

if "should_clear_selection" not in st.session_state:
    st.session_state.should_clear_selection = False


# Function to clear all inputs
def on_button_send():
    # If there is user_text, add it to the DataFrame
    if st.session_state.textinput.strip():
        # Add with placeholder name
        st.session_state.df = pd.concat(
            [
                st.session_state.df,
                pd.DataFrame({"name": ["User Input"], "command": [st.session_state.textinput]}),
            ],
            ignore_index=True,
        )
    st.session_state.should_clear_selection = not st.session_state.should_clear_selection
    st.session_state.textinput = ""


df = st.session_state.df

st.title("Simple Table with Row Selection")

st.text_area("Enter some text:", key="textinput")


# Generate a dynamic key based on the clear selection flag
dataframe_key = f"dataframe_{st.session_state.should_clear_selection}"

def on_select():
    event = st.session_state[dataframe_key]
    # Check if rows are selected and display their indices
    if event.selection and event.selection.rows:
        selected_indices = event.selection.rows
        # st.write("Selected row indices:", selected_indices)

        # If you want to access the data of selected rows
        selected_data = df.iloc[selected_indices]
        # st.write("Selected data:")
        # st.write(selected_data)


st.dataframe(
    st.session_state.df,
    use_container_width=True,
    height=200,
    selection_mode="multi-row",
    on_select=on_select,
    key=dataframe_key,
)


def delete_rows():
    event = st.session_state[dataframe_key]
    if event.selection and event.selection.rows:
        selected_indices = event.selection.rows
        st.session_state.df = st.session_state.df.drop(selected_indices).reset_index(
            drop=True
        )


# Add a button to send input
st.button("Send", on_click=on_button_send)

# button to delete selected row in the table
st.button("Delete Row", on_click=delete_rows)
