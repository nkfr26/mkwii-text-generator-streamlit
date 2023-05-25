import streamlit as st


class Single:
    def __init__(self):
        st.session_state.single_picker = st.session_state.color
        st.sidebar.color_picker(
            "Color", key="single_picker", on_change=self.set_color
        )

    def set_color(self):
        st.session_state.color = st.session_state.single_picker


class Multi:
    def __init__(self, master):
        left, right = st.sidebar.columns((1, 2))
        with right:
            index = st.selectbox(  # インデックスの取得
                "Character",
                range(len(master.file_names)),
                format_func=lambda x: master.file_names[x],
            )
        with left:
            st.session_state.multi_picker = st.session_state.colors[index]
            st.color_picker(
                "Color", key="multi_picker",
                on_change=self.set_colors, args=(index, ),
            )

    def set_colors(self, index):
        st.session_state.colors[index] = st.session_state.multi_picker


class Gradient:
    def __init__(self, master):
        upper_left, upper_right = st.sidebar.columns(2)
        options = {"orientation": ("Vertical", "Horizontal"), "mode": ("RGB", "HSL")}
        with upper_left:
            master.orientation = st.radio(
                "Orientation", options["orientation"], st.session_state.index["orientation"]
            )
            st.session_state.index["orientation"] = options["orientation"].index(master.orientation)
        with upper_right:
            master.mode = st.radio(
                "Mode", options["mode"], st.session_state.index["mode"]
            )
            st.session_state.index["mode"] = options["mode"].index(master.mode)

        lower_left, lower_right = st.sidebar.columns(2)
        with lower_left:
            st.session_state.top_picker = st.session_state.top_color
            st.color_picker(
                "Top" if master.orientation == "Vertical" else "Left",
                key="top_picker", on_change=self.set_top_color,
            )
        with lower_right:
            st.session_state.btm_picker = st.session_state.btm_color
            st.color_picker(
                "Bottom" if master.orientation == "Vertical" else "Right",
                key="btm_picker", on_change=self.set_btm_color,
            )

    def set_top_color(self):
        st.session_state.top_color = st.session_state.top_picker

    def set_btm_color(self):
        st.session_state.btm_color = st.session_state.btm_picker
