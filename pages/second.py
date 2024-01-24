import streamlit as st

def display_chat(chat_messages):
    # Display chat messages
    for sender, message in chat_messages:
        a = ":smiley:"
        if sender == 'user':
            # Apply CSS styling for user response
            st.write(
                f'<div style="display:flex; align-items:center; flex-direction:row-reverse;">'
                f'<div style="margin-right: 10px;">'
                f'👤'  # User emoji
                f'</div>'
                f'<div style="background-color:#25D366; padding:10px; border-radius:10px;">'
                f'{message}'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )
        else:
            # Apply CSS styling for bot response
            st.write(
                f'<div style="display:flex; align-items:center;">'
                f'<div style="margin-right: 10px;">'
                f'🤖'  # Bot emoji
                f'</div>'
                f'<div style="background-color:#075E54; padding:10px; border-radius:10px;">'
                f'{message}'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

