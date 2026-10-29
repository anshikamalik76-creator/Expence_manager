from datetime import date

import streamlit as st
import os
import pandas as pd


File_Name = "expenses.csv"


def  load_expences():
    if os.path.exists(File_Name):
        df = pd.read_csv(File_Name)
        return df.to_dict('records')
    return[]


def  save_expences(expences):
    df = pd.DataFrame(expences)
    df.to_csv(File_Name, index=False)



st.title("Daily expences manager")
st.write("This is a simple app to manage your daily expenses. You can add your expenses, view them, and analyze your spending habits.")


if 'expenses' not in st.session_state:
    st.session_state.expenses = load_expences()



st.subheader("Add a new expense")

with st.form("expense_form"):
    expence_name = st.text_input("Expense Name")
    amount = st.number_input(
        "Amount (Rupees)", min_value=0, step=10
    )


    categories = st.selectbox(

    "category",

     ["Food", "Transport", "Entertainment", "Utilities", "Other"]
    )


    expense_date = st.date_input(
    'Expense Date',
    value=date.today()
    )

    submitted = st.form_submit_button("Add Expense")


if submitted:
    if expence_name.strip():
        expence ={
            'Date': expense_date,
            "Expence Name": expence_name,
            "Amount": amount,
            "Category": categories
        }

        st.session_state.expenses.append(expence)
        save_expences(st.session_state.expenses)

        st.success("Expense added successfully!")
    else:
        st.error("Please enter a valid expense name.")


st.subheader("All Expenses")

expenses = st.session_state.expenses



# if expenses:
#     df = pd.DataFrame(expenses)
#     total = sum(float(expense["Amount"]) for expense in expenses)
