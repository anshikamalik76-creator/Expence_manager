
import streamlit as st


st.title("🏧 Simple ATM Simulator")
st.write("Welcome to our ATM!")


if "balance" not in st.session_state:
    st.session_state.balance = 5000

if "history" not in st.session_state:
    st.session_state.history = []


choice = st.selectbox(
    "Choose an operation",
    ["Check Balance", "Deposit Money", "Withdraw Money"]
)


if choice == "Check Balance":
    st.subheader("Account Balance")
    st.success(f"Your balance is ₹{st.session_state.balance}")


elif choice == "Deposit Money":
    st.subheader("Deposit Money")

    amount = st.number_input(
        "Enter deposit amount",
        min_value=0,
        step=100
    )

    if st.button("Deposit"):
        if amount > 0:
            st.session_state.balance += amount
            st.session_state.history.append(
                f"Deposited ₹{amount}"
            )
            st.success("Money deposited successfully!")
            st.rerun()
        else:
            st.error("Please enter an amount greater than zero.")


elif choice == "Withdraw Money":
    st.subheader("Withdraw Money")

    amount = st.number_input(
        "Enter withdrawal amount",
        min_value=0,
        step=100
    )

    if st.button("Withdraw"):
        if amount <= 0:
            st.error("Please enter an amount greater than zero.")
        elif amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.session_state.history.append(
                f"Withdrawn ₹{amount}"
            )
            st.success("Please collect your money!")
            st.rerun()
        else:
            st.error("Insufficient balance!")


st.subheader("📋 Transaction History")

if st.session_state.history:
    for transaction in st.session_state.history:
        st.write("•", transaction)
else:
    st.info("No transactions yet.")


st.metric("Current Balance", f"₹{st.session_state.balance}")
