import streamlit as st

st.title("hey bb~")
st.subheader(
    "i just started so this page doesn't have much and is pretty lame")
st.write("u good?")


def clicked_yes():
    st.write("yay! ♡ almost the end of the week liao, last push bb")


def clicked_no():
    st.write("jy 我的爱 ♡ you are smart af and you got this okay")


yes_button = st.button("yes", on_click=clicked_yes)
no_button = st.button("no", on_click=clicked_no)

st.image("bishan.png", caption="some bishan amk park scenery to motivate you")



