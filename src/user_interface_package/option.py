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
    def __init__(self):
        upper_left, upper_right = st.sidebar.columns(2)
        with upper_left:
            st.session_state.orientation_radio = st.session_state.orientation
            st.radio(
                "Orientation", ("Vertical", "Horizontal"),
                key="orientation_radio", on_change=self.set_orientation,
            )
        with upper_right:
            st.session_state.mode_radio = st.session_state.mode
            st.radio(
                "Mode", ("RGB", "HSL"),
                key="mode_radio", on_change=self.set_mode,
            )

        lower_left, lower_right = st.sidebar.columns(2)
        with lower_left:
            st.session_state.top_picker = st.session_state.top_color
            st.color_picker(
                "Top" if st.session_state.orientation == "Vertical" else "Left",
                key="top_picker", on_change=self.set_top_color,
            )
        with lower_right:
            st.session_state.btm_picker = st.session_state.btm_color
            st.color_picker(
                "Bottom" if st.session_state.orientation == "Vertical" else "Right",
                key="btm_picker", on_change=self.set_btm_color,
            )

    def set_orientation(self):
        st.session_state.orientation = st.session_state.orientation_radio

    def set_mode(self):
        st.session_state.mode = st.session_state.mode_radio

    def set_top_color(self):
        st.session_state.top_color = st.session_state.top_picker

    def set_btm_color(self):
        st.session_state.btm_color = st.session_state.btm_picker
