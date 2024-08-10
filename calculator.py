import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0, step=1e-1, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, step=1e-1, format="%.2f")

# Dropdown for selecting operation
operation = st.selectbox("Choose the operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is: {result}")
        else:
            st.error("Division by zero is not allowed.")
