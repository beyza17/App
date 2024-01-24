import streamlit as st
from streamlit_option_menu import option_menu   
from streamlit_extras.colored_header import colored_header

def main():
    ##st.markdown("<h2 style='text-align: center; color: blue;'>Smart Chest-Xray Analysis and Report Generation!</h2>", unsafe_allow_html=True)
    """
    Main function to run the application.
    """
    
    # sidebar: used option_menu just for asthetics
    with st.sidebar:
        choice = option_menu("main", ["second_page"], 
            icons=['house', 'fire'], menu_icon="cast", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#262730"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#3739b5"},
        "nav-link-selected": {"background-color": "#1f8ff6"},})  

    # navigations 
    if choice == "Try out!":
        colored_header(
        label="CHEST-INSIGHT: Smart Chest-Xray Analysis and Report Generation! ",
        description="Use the tabs below to tryout our dedicated tools",
        color_name="violet-70",)
        features()
 
 
        


if __name__ == "__main__":
    main()
