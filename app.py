import streamlit as st

# Distance Converter Function
def distance_converter(from_units, to_units, value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    result = value * units[from_units] / units[to_units]
    return result

# Temperature Converter Function
def temperature_converter(from_units, to_units, value):
    if from_units == "Celsius" and to_units == "Fahrenheit":
        result = (value * 9/5) + 32
    elif from_units == "Fahrenheit" and to_units == "Celsius":
        result = (value - 32) * 5/9
    else:
        result = value  # No conversion needed if both units are the same
    return result

# Weight Converter Function
def weight_converter(from_units, to_units, value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    result = value * units[from_units] / units[to_units]
    return result

# Pressure Converter Function
def pressure_converter(from_units, to_units, value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,  
        "Kilopascals": 1000,  
        "Bars": 100000,       
    }
    result = value * units[from_units] / units[to_units]
    return result

# Streamlit UI
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

# Distance Conversion UI
if category == "Distance":
    from_units = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles"])
    to_units = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value")

    if st.button("Convert"):
        result = distance_converter(from_units, to_units, value)
        st.success(f"{value} {from_units} = {result:.2f} {to_units}")

# Temperature Conversion UI
if category == "Temperature":
    from_units = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_units = st.selectbox("To", ["Celsius", "Fahrenheit"])
    value = st.number_input("Enter Value")

    if st.button("Convert"):
        result = temperature_converter(from_units, to_units, value)
        st.success(f"{value} {from_units} = {result:.2f} {to_units}")

# Weight Conversion UI
if category == "Weight":
    from_units = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_units = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    value = st.number_input("Enter Value")

    if st.button("Convert"):
        result = weight_converter(from_units, to_units, value)
        st.success(f"{value} {from_units} = {result:.2f} {to_units}")

# Pressure Conversion UI
if category == "Pressure":
    from_units = st.selectbox("From", ["Pascals", "Hectopascals", "Kilopascals", "Bars"])
    to_units = st.selectbox("To", ["Pascals", "Hectopascals", "Kilopascals", "Bars"])
    value = st.number_input("Enter Value")

    if st.button("Convert"):
        result = pressure_converter(from_units, to_units, value)
        st.success(f"{value} {from_units} = {result:.2f} {to_units}")
