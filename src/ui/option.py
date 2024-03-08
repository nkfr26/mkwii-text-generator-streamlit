import streamlit as st


class Single:
    def __init__(self):
        st.session_state.single_state = st.session_state.color
        st.sidebar.color_picker(
            "Color", key="single_state", on_change=self.set_color
        )

    def set_color(self):
        st.session_state.color = st.session_state.single_state


class Multi:
    def __init__(self, master):
        left, right = st.sidebar.columns((1, 2))
        with right:
            index = st.selectbox(  # インデックスの取得
                "Character", range(len(master.file_names)),
                format_func=lambda x: master.file_names[x]
            )
        with left:
            st.session_state.multi_state = st.session_state.colors[index]
            st.color_picker(
                "Color", key="multi_state",
                on_change=self.set_colors, args=(index, )
            )

    def set_colors(self, index):
        st.session_state.colors[index] = st.session_state.multi_state


class Gradient:
    def __init__(self):
        upper_left, upper_right = st.sidebar.columns(2)
        with upper_left:
            st.session_state.orientation_state = st.session_state.gradient_radio["orientation"]
            st.radio(
                "Orientation", ("Vertical", "Horizontal"),
                key="orientation_state", on_change=self.set_orientation
            )
        with upper_right:
            st.session_state.mode_state = st.session_state.gradient_radio["mode"]
            st.radio(
                "Mode", ("RGB", "HSL"),
                key="mode_state", on_change=self.set_mode
            )

        lower_left, lower_right = st.sidebar.columns(2)
        with lower_left:
            st.session_state.top_state = st.session_state.gradient_color["top"]
            st.color_picker(
                "Top" if st.session_state.gradient_radio["orientation"] == "Vertical" else "Left",
                key="top_state", on_change=self.set_top_color
            )
        with lower_right:
            st.session_state.btm_state = st.session_state.gradient_color["btm"]
            st.color_picker(
                "Bottom" if st.session_state.gradient_radio["orientation"] == "Vertical" else "Right",
                key="btm_state", on_change=self.set_btm_color
            )

    def set_orientation(self):
        st.session_state.gradient_radio["orientation"] = st.session_state.orientation_state

    def set_mode(self):
        st.session_state.gradient_radio["mode"] = st.session_state.mode_state

    def set_top_color(self):
        st.session_state.gradient_color["top"] = st.session_state.top_state

    def set_btm_color(self):
        st.session_state.gradient_color["btm"] = st.session_state.btm_state
