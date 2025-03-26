import streamlit as st

st.title("BMI 🧭 Calculator")

weight = st.number_input("Enter your weight in kilograme (KG):", min_value=0.0, step=0.1)
height = st.number_input("Enter your height in meters (M):", min_value=0.0, step=0.1)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is:{bmi:.2f}")
        
        if bmi < 18.5:
            st.info("you are underweight.")
            
        elif  18.5 <= bmi <24.9:
            st.success("You have a normal weight")
        elif 25 <= bmi < 29.9:
            st.success("You are overweight")
        else: 
            st.error("You are obese")            
    else:
        st.error("Please enter a valid height greater then zero")
        
