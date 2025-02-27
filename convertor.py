import streamlit as st
st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")
# Title and description
st.markdown("<h1 class='main-title'> Unit Converter</h1>", unsafe_allow_html=True)
st.write("<p class='description'>Convert units of length, weight, and temperature effortlessly with a sleek interface.</p>", unsafe_allow_html=True)

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

# Conversion options
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Inches", "Yards"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Feet", "Inches", "Yards"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
# Length conversion:
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,  # Base unit
        "Kilometers": 1000,  # 1 km = 1000 meters
        "Centimeters": 100,  # 1 meter = 100 centimeters
        "Millimeters": 1000,  # 1 meter = 1000 millimeters
        "Miles": 1609.34,  # 1 mile = 1609.34 meters
        "Feet": 0.3048,  # 1 foot = 0.3048 meters
        "Inches": 0.0254,  # 1 inch = 0.0254 meters
        "Yards": 0.9144,  # 1 yard = 0.9144 meters
    }
    return (value / length_units[from_unit] * length_units[to_unit])

# Weight conversion:
def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / weight_units[from_unit] * weight_units[to_unit])

# Temperature conversion:
def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9 / 5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5 / 9 if to_unit == "Celsius" else (value - 32) * 5 / 9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273) * 9 / 5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Button to perform conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Created with ♡ by Rida Fatima</div>", unsafe_allow_html=True)

# Additional CSS styling for gray theme and result box
st.markdown("""
    <style>
    /* Gray theme styling */
    .main-title {
        font-size: 30px;
        color: #808080;  /* Gray color for the title */
        text-align: center;
        margin-bottom: 10px;
    }
    .description {
        font-size: 16px;
        color: #808080;  /* Gray color for the description */
        text-align: center;
        margin-bottom: 30px;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        color: #808080;  /* Gray color for result */
        margin-top: 20px;
        text-align: center;
    }
    .footer {
        font-size: 12px;
        text-align: center;
        color: #808080;  /* Gray color for footer */
        margin-top: 30px;
    }

    .stSelectbox, .stNumberInput {
        color: #808080;  /* Gray color for selectboxes and input fields */
    }
    </style>
""", unsafe_allow_html=True)
