import pandas as pd
import streamlit as st

# Tải dữ liệu từ file Excel
data = pd.read_excel("Danh mục Model.xlsx")

# Làm sạch dữ liệu
data.columns = data.columns.str.strip()
data['Model'] = data['Model'].astype(str).str.strip()

# Giao diện Streamlit
st.title("🔍 Chatbot Tra cứu Thiết bị")

query = st.text_input("Nhập câu hỏi (ví dụ: 5520A của hãng nào?)")

if query:
    found = False
    for idx, row in data.iterrows():
        if row['Model'].lower() in query.lower():
            st.success(f"Thiết bị: {row['Tên thiết bị']}")
            st.info(f"Model: {row['Model']}")
            st.warning(f"Nhà sản xuất: {row['Nhà sản xuất']}")
            found = True
            break
    if not found:
        st.error("❌ Không tìm thấy model trong cơ sở dữ liệu.")
