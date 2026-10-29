
import streamlit as st


st.title("Unit Converter")
st.write("Convert different units easily!")


def km_to_miles(km):
    return km * 0.621371


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def kg_to_pounds(kg):
    return kg * 2.20462


choice = st.selectbox(
    "Select a conversion",
    [
        "Kilometer to Miles",
        "Celsius to Fahrenheit",
        "Kilograms to Pounds"
    ]
)


value = st.number_input(
    "Enter the value",
    value=0.0
)


if choice == "Kilometer to Miles":
    result = km_to_miles(value)
    st.success(f"Result: {result:.2f} miles")

elif choice == "Celsius to Fahrenheit":
    result = celsius_to_fahrenheit(value)
    st.success(f"Result: {result:.2f} °F")

elif choice == "Kilograms to Pounds":
    result = kg_to_pounds(value)
    st.success(f"Result: {result:.2f} pounds")
