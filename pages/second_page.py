import streamlit as st
import spacy=="3.7.2"

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
                    

       ########
            nlp = spacy.load('en_core_web_sm')

            # Create a Doc object
            doc = nlp(text_input)
            # Generate list of lemmas
            lemmas = [token.lemma_ for token in doc]
            st.write("You entered: ", lemmas)

            # Remove tokens that are not alphabetic
            a_lemmas = [lemma for lemma in lemmas
            if lemma.isalpha() or lemma == '-PRON-']
            # Print string after text cleaning
            st.write("You entered: ", a_lemmas)
            st.write("You entered: ", (' '.join(a_lemmas)))
            # Generate list of tokens and pos tags
            pos = [(token.text, token.pos_) for token in doc]
            st.write("You entered: ", pos)
            

if __name__ == "__main__":
    main()
