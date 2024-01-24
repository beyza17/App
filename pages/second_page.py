import streamlit as st


def main():
    # open colour image
    st.title('Model Output')
    st.markdown("<h2 style='text-align: center; color: violet;'>Report Generation!</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    image_file = st.file_uploader("Upload the image", type=['jpg', 'png', 'jpeg'])
    if image_file is not None:
        img = plt.imread(image_file)
        col1.image(image_file, caption='Uploaded Image', use_column_width=True)
    with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )
   


if __name__ == "__main__":
    main()
