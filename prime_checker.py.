import streamlit as st

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    st.title("Prime Number Checker")
    user_input = st.number_input("Enter a number:")
    if st.button("Check"):
        if is_prime(user_input):
            st.write(f"{user_input} is a prime number.")
        else:
            st.write(f"{user_input} is a composite number.")

if _name_ == "_main_":
    main()
