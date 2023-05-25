import re

import streamlit as st

from user_interface_package.option import Single, Multi, Gradient


class UserInterface:
    def __init__(self) -> None:
        self.file_names = self.to_file_names(
            st.sidebar.text_area("text_area", label_visibility="collapsed")
        )

        left, right = st.sidebar.columns((3, 2), gap="medium")
        with left:
            self.slider = st.slider("Brightness", -20, 100, 0, 5) / 50 + 1
        with right:
            with st.container():
                st.write("Stroke")
                self.should_invert = st.checkbox("White")

        self.selectbox = st.sidebar.selectbox(
            "selectbox",
            ("Yellow", "White", "Single Color", "Multi Color", "Gradient"),
            label_visibility="collapsed",
        )

        self.orientation, self.mode = "Vertical", "RGB"
        self.set_widget_by_selectbox()

        left, right = st.sidebar.columns(2)
        with left:
            link1 = "[Developer's Twitter](https://twitter.com/nkfrom_mkw/)"
            st.markdown(link1, True)
        with right:
            link2 = "[README](https://github.com/NOKKY726/mkwii-text-generator/)"
            st.markdown(link2, True)

        self.mobile = st.sidebar.checkbox("Mobile")

    def to_file_names(self, text_area) -> list:
        replace_dict = {
            ":": "COLON", ".": "PERIOD", "/": "SLASH", " ": "SPACE", "<": "LEFT", ">": "RIGHT"
        }
        file_names = [replace_dict.get(char, char) for char in text_area.upper()]

        count, need_replace = 0, False  # 「"」間の文字を置換
        for i, file_name in enumerate(file_names):
            if file_name == '"' and count < file_names.count('"') // 2:
                if not need_replace:
                    need_replace = True
                else:
                    need_replace = False
                    count += 1
            elif need_replace and file_name in [*map(str, range(10)), "-", "SLASH", "SPACE"]:
                file_names[i] += "_"

        # 使用できない文字がないか検証
        file_names = [
            file_name
            for file_name in file_names
            if re.sub("[^-+0-9A-Z<>\n]", "", file_name)
        ]
        # 右側の空白と改行を削除
        while file_names and file_names[-1] in ["SPACE", "SPACE_", "\n", "LEFT", "RIGHT"]:
            del file_names[-1]

        return file_names

    def set_widget_by_selectbox(self) -> None:
        match self.selectbox:
            case "Single Color":
                Single()
            case "Multi Color" if self.file_names:
                Multi(self)
            case "Gradient":
                Gradient(self)
            case _:
                pass
