import streamlit as st

def main():
    # open colour image
    st.title('Model Output')
    st.markdown("<h2 style='text-align: center; color: violet;'>Report Generation!</h2>", unsafe_allow_html=True)
    

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("[![Foo](https://media.giphy.com/media/RqxdeXRrOiGic/giphy.gif)")
    
    with col2:
        text_input = st.text_input("Enter some text 👇")

        if text_input:
            st.write("You entered: ", text_input)
            

if __name__ == "__main__":
    main()
