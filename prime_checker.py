import streamlit as st

def main():
    st.title("Simple Calculator")

    # Function to perform addition
    def add(num1, num2):
        return num1 + num2

    # Function to perform subtraction
    def subtract(num1, num2):
        return num1 - num2

    # Function to perform multiplication
    def multiply(num1, num2):
        return num1 * num2

    # Function to perform division
    def divide(num1, num2):
        if num2 == 0:
            return "Cannot divide by zero!"
        else:
            return num1 / num2

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    operation = st.radio("Select Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
            st.success(f"The result of {num1} + {num2} = {result}")
        elif operation == "Subtraction":
            result = subtract(num1, num2)
            st.success(f"The result of {num1} - {num2} = {result}")
        elif operation == "Multiplication":
            result = multiply(num1, num2)
            st.success(f"The result of {num1} * {num2} = {result}")
        elif operation == "Division":
            result = divide(num1, num2)
            st.success(f"The result of {num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
