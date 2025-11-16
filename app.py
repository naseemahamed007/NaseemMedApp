import streamlit as st

# BMI advice dictionary
bmi_advice = {
    'Underweight': {
        'remedy': 'Increase calorie intake with nutrient-dense foods, incorporate strength training, eat frequently.',
        'tablet': 'Consult a nutritionist for supplements or a doctor for appetite stimulants.',
        'color': 'BLUE'
    },
    'Normal weight': {
        'remedy': 'Maintain balanced diet, regular physical activity (150 mins/week).',
        'tablet': 'No specific medication recommended.',
        'color': 'GREEN'
    },
    'Overweight': {
        'remedy': 'Reduce calorie intake, focus on cardio and strength training, avoid sugary foods.',
        'tablet': 'Consult a nutritionist or doctor for guidance.',
        'color': 'ORANGE'
    },
    'Obese': {
        'remedy': 'Strict diet control, intensive physical activity, seek professional help.',
        'tablet': 'Consult a doctor for medical intervention.',
        'color': 'RED'
    }
}

# App title
st.title("BMI Advice App")

# User input
bmi = st.number_input("Enter your BMI:", min_value=0.0, max_value=100.0, step=0.1)

# Determine category
if bmi < 18.5:
    category = 'Underweight'
elif 18.5 <= bmi < 25:
    category = 'Normal weight'
elif 25 <= bmi < 30:
    category = 'Ove
