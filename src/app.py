import sys

sys.dont_write_bytecode = True

import streamlit as st

from user_interface import UserInterface
from feature_package.text_image_generator import TextImageGenerator


st.set_page_config(
    page_title="MKWii Text Generator",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "https://github.com/NOKKY726/mkwii-text-generator",
    },
)

if "color" not in st.session_state:
    st.session_state.color = "#ff0000"
    st.session_state.colors = ["#ffffff" for _ in range(10**4)]
    st.session_state.gradient_radio = {"orientation": "Vertical", "mode": "RGB"}
    st.session_state.gradient_color = {"top": "#00ff00", "btm": "#0000ff"}

user_interface = UserInterface()

text_image_generator = TextImageGenerator(user_interface)
MKWii_text = text_image_generator.run()

if not user_interface.mobile:
    st.image(MKWii_text)
else:
    st.sidebar.image(MKWii_text)
