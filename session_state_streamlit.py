import streamlit as st

# Nếu chưa có biến "count" thì tạo và gán = 0
if "count" not in st.session_state:
    st.session_state["count"] = 0

# Hiển thị giá trị hiện tại
st.write("Giá trị count hiện tại:", st.session_state["count"])

# Nút tăng
if st.button("Tăng"):
    st.session_state["count"] += 1

# Nút giảm
if st.button("Giảm"):
    st.session_state["count"] -= 1
