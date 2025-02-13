import streamlit as st

# 设置网页标题
st.title("简单计算器")

# 数字输入
num1 = st.number_input("请输入第一个数字", value=0.0)
num2 = st.number_input("请输入第二个数字", value=0.0)

# 选择计算方式
operation = st.selectbox("选择运算类型", ["加法", "减法", "乘法", "除法"])

# 计算按钮
if st.button("计算"):
    if operation == "加法":
        result = num1 + num2
    elif operation == "减法":
        result = num1 - num2
    elif operation == "乘法":
        result = num1 * num2
    elif operation == "除法":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "错误：除数不能为零！"
    
    # 显示结果
    st.success(f"计算结果: {result}")