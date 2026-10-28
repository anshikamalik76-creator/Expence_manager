
import streamlit as st
from datetime import datetime

# Initial ATM data
if "balance" not in st.session_state:
    st.session_state.balance = 10000.0
    st.session_state.pin = "1234"
    st.session_state.logged_in = False
    st.session_state.history = []

st.title("🏧 ATM Management System")
st.write("Welcome to the ATM")

# PIN verification
if not st.session_state.logged_in:
    pin = st.text_input("Enter your 4-digit ATM PIN", type="password")

    if st.button("Login"):
        if pin == st.session_state.pin:
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Incorrect PIN. Try again.")

else:
    st.success("You are logged in successfully!")

    st.subheader("ATM Menu")

    option = st.selectbox(
        "Choose an operation",
        [
            "Check Balance",
            "Withdraw Cash",
            "Deposit Cash",
            "Transaction History"
        ]
    )

    if option == "Check Balance":
        st.metric("Available Balance", f"₹{st.session_state.balance:.2f}")

    elif option == "Withdraw Cash":
        amount = st.number_input(
            "Enter withdrawal amount (₹)",
            min_value=0.0,
            step=500.0
        )

        if st.button("Withdraw"):
            if amount <= 0:
                st.error("Enter a valid amount.")
            elif amount > st.session_state.balance:
                st.error("Insufficient balance.")
            else:
                st.session_state.balance -= amount
                st.session_state.history.append({
                    "Date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "Transaction": "Withdrawal",
                    "Amount": amount,
                    "Balance": st.session_state.balance
                })
                st.success(f"₹{amount:.2f} withdrawn successfully!")

    elif option == "Deposit Cash":
        amount = st.number_input(
            "Enter deposit amount (₹)",
            min_value=0.0,
            step=500.0
        )

        if st.button("Deposit"):
            if amount <= 0:
                st.error("Enter a valid amount.")
            else:
                st.session_state.balance += amount
                st.session_state.history.append({
                    "Date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "Transaction": "Deposit",
                    "Amount": amount,
                    "Balance": st.session_state.balance
                })
                st.success(f"₹{amount:.2f} deposited successfully!")

    elif option == "Transaction History":
        if st.session_state.history:
            st.dataframe(st.session_state.history)
        else:
            st.info("No transactions yet.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
