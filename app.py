import streamlit as st

# ---------------- Page config & theme ----------------
st.set_page_config(page_title="Naseem's Medical App - Detailed Advice", page_icon="🩺", layout="centered")

st.markdown(
    """
    <style>
    body { background-color: #071428; color: #E9F2FF; }
    .stApp { background-color: #071428; }
    h1, h2, h3, p, label, div { color: #E9F2FF !important; }
    .card { background-color: #0b3350; padding: 14px; border-radius: 10px; margin-bottom: 12px; }
    .badge-good { color: #063; font-weight:700; }
    .badge-warn { color: #e69500; font-weight:700; }
    .badge-bad  { color: #c42a2a; font-weight:700; }
    .badge-crit { color: #ff0000; font-weight:900; }
    .muted { color: #bcd6ff; }
    .small { font-size:14px; }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<h1 style='text-align:center; color:#72b3ff;'>🩺 Naseem's Med App — Detailed Remedies</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#BFE1FF;'>Professional-style advice (informational only)</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- Dictionaries (professional text) ----------------
PROFESSIONAL_ADVICE = {
    # BMI Advice
    'Underweight': {
        'remedy': 'Structured high-calorie diet focused on nutrient-dense foods (nuts, dairy, lean red meat, whole eggs) and progressive resistance training to increase muscle mass.',
        'physical': 'Eat 5–6 small meals/day, add protein shakes between meals, start 3×/week strength training (bodyweight → weights). Track calories with an app.',
        'tablet': 'Consult Registered Dietitian and physician. Investigate underlying causes; appetite stimulants may be considered by a doctor if indicated.'
    },
    'Normal weight': {
        'remedy': 'Maintain balanced intake with adequate protein and 150 minutes/week of moderate aerobic activity.',
        'physical': 'Continue regular activity (walking, cycling); strength training 2×/week for maintenance.',
        'tablet': 'No pharmacological therapy indicated; routine health monitoring.'
    },
    'Overweight': {
        'remedy': 'Create a moderate calorie deficit (500 kcal/day), prioritise whole foods, increase daily activity and structured cardio sessions.',
        'physical': 'Target 150–300 min/week of moderate activity; add resistance training to preserve lean mass. Avoid sugary drinks and refined carbs.',
        'tablet': 'If lifestyle measures fail, discuss anti-obesity medication options with your physician for long-term management.'
    },
    'Obese': {
        'remedy': 'Intensive lifestyle program with dietary counseling and supervised exercise; consider specialist referral for weight management.',
        'physical': 'Structured multi-disciplinary program, higher volume exercise as tolerated, close follow-up, consider pre-surgical evaluation if criteria met.',
        'tablet': 'Urgent medical evaluation; pharmacotherapy or bariatric surgery may be appropriate under specialist care.'
    },

    # BP Advice
    'Normal BP': {
        'remedy': 'Maintain a low sodium diet (<1,500 mg/day target if hypertensive risk), maintain healthy weight and regular exercise.',
        'physical': 'Daily moderate physical activity, reduced alcohol, stress-management (meditation, sleep hygiene).',
        'tablet': 'No antihypertensive needed; continue routine BP monitoring.'
    },
    'Elevated BP': {
        'remedy': 'Reduce sodium and alcohol, increase potassium-rich foods, begin structured stress reduction.',
        'physical': 'Start brisk walking 30 min/day, reduce caffeine before measurements, home BP monitoring.',
        'tablet': 'No immediate medication typically; re-evaluate frequently and intensify lifestyle measures.'
    },
    'Stage 1 HTN': {
        'remedy': 'Adopt the DASH eating plan (vegetables, fruit, low-fat dairy), weight loss, and regular aerobic exercise.',
        'physical': 'Aim 30–45 min aerobic exercise most days, quit smoking, limit alcohol intake.',
        'tablet': 'Medical review required; may need a single antihypertensive agent (e.g., ACE inhibitor, ARB or thiazide) depending on risk profile.'
    },
    'Stage 2 HTN': {
        'remedy': 'Strict heart-healthy diet with rapid lifestyle changes and urgent follow-up.',
        'physical': 'Intensify exercise safely under supervision; rapid BP control strategy needed.',
        'tablet': 'Often requires immediate pharmacologic therapy, frequently dual-agent therapy — consult a clinician urgently.'
    },

    # Sugar Advice (Fasting)
    'Normal Sugar': {
        'remedy': 'Low-glycemic diet, portion control, regular meals and hydration.',
        'physical': 'At least 150 min/week of moderate exercise; avoid prolonged sedentary time.',
        'tablet': 'No glucose-lowering medication indicated; routine monitoring.'
    },
    'Pre-Diabetes': {
        'remedy': 'Intensive weight loss goal of 5–7% body weight, reduce refined carbs and sugary beverages.',
        'physical': '150–300 min/week physical activity, resistance + aerobic training.',
        'tablet': 'Discuss Metformin with physician as preventative therapy in some cases.'
    },
    'Diabetes': {
        'remedy': 'Carbohydrate-controlled diet, regular glucose self-monitoring, and preventive foot/eye care.',
        'physical': 'Structured exercise program, blood glucose monitoring and education for hypoglycaemia prevention.',
        'tablet': 'Immediate medical consultation for individualized pharmacologic therapy (Metformin, insulin, SGLT2 inhibitors, etc) as decided by a physician.'
    }
}

RISK_STATUS = {
    'Underweight': ('WARNING', 'badge-warn'),
    'Normal weight': ('GOOD', 'badge-good'),
    'Overweight': ('BAD', 'badge-bad'),
    'Obese': ('CRITICAL', 'badge-crit'),
    'Normal BP': ('GOOD', 'badge-good'),
    'Elevated BP': ('WARNING', 'badge-warn'),
    'Stage 1 HTN': ('BAD', 'badge-bad'),
    'Stage 2 HTN': ('CRITICAL', 'badge-crit'),
    'Normal Sugar': ('GOOD', 'badge-good'),
    'Pre-Diabetes': ('WARNING', 'badge-warn'),
    'Diabetes': ('CRITICAL', 'badge-crit'),
}

# ---------------- Helper functions ----------------
def calculate_bmi(weight_kg, height_cm):
    h_m = height_cm / 100
    if h_m <= 0:
        return None, None
    bmi = weight_kg / (h_m * h_m)
    bmi_val = round(bmi, 1)
    if bmi < 18.5:
        cat = 'Underweight'
    elif bmi < 25:
        cat = 'Normal weight'
    elif bmi < 30:
        cat = 'Overweight'
    else:
        cat = 'Obese'
    return bmi_val, cat

def get_bp_category(systolic, diastolic):
    if systolic >= 140 or diastolic >= 90:
        return f"{int(systolic)}/{int(diastolic)} mmHg", 'Stage 2 HTN'
    elif systolic >= 130 or diastolic >= 80:
        return f"{int(systolic)}/{int(diastolic)} mmHg", 'Stage 1 HTN'
    elif 120 <= systolic < 130 and diastolic < 80:
        return f"{int(systolic)}/{int(diastolic)} mmHg", 'Elevated BP'
    else:
        return f"{int(systolic)}/{int(diastolic)} mmHg", 'Normal BP'

def get_sugar_category(fasting_mgdl):
    if fasting_mgdl >= 126:
        return f"{int(fasting_mgdl)} mg/dL", 'Diabetes'
    elif 100 <= fasting_mgdl <= 125:
        return f"{int(fasting_mgdl)} mg/dL", 'Pre-Diabetes'
    else:
        return f"{int(fasting_mgdl)} mg/dL", 'Normal Sugar'

def badge_html(text, cls):
    return f"<span class='{cls}' style='font-size:14px'>{text}</span>"

# ---------------- Inputs ----------------
st.markdown("## 🔎 Enter patient data")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age (years)", min_value=1, max_value=120, value=25, step=1)
    height = st.number_input("Height (cm)", min_value=50, max_value=230, value=170, step=1)
with col2:
    weight = st.number_input("Weight (kg)", min_value=1, max_value=300, value=70, step=1)
    st.write("")  # spacing

col3, col4 = st.columns(2)
with col3:
    systolic = st.number_input("Systolic BP (mmHg)", min_value=50, max_value=250, value=120, step=1)
with col4:
    diastolic = st.number_input("Diastolic BP (mmHg)", min_value=30, max_value=150, value=80, step=1)

fasting = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=40, max_value=600, value=90, step=1)

st.markdown("---")

# ---------------- Generate report ----------------
if st.button("📄 Generate Detailed Report"):
    # BMI
    bmi_val, bmi_cat = calculate_bmi(weight, height)
    bp_score, bp_cat = get_bp_category(systolic, diastolic)
    sugar_score, sugar_cat = get_sugar_category(fasting)

    # Display summary top
    st.markdown("### 📊 Clinical Summary")
    st.markdown(f"<div class='card'><b>Age:</b> {age} yrs &nbsp;&nbsp; <b>Height:</b> {height} cm &nbsp;&nbsp; <b>Weight:</b> {weight} kg</div>", unsafe_allow_html=True)

    # BMI block
    bstatus, bcls = RISK_STATUS[bmi_cat]
    st.markdown(f"<div class='card'><b>Body Mass Index (BMI):</b> {bmi_val} — <b>{bmi_cat}</b> &nbsp; {badge_html(bstatus, bcls)}</div>", unsafe_allow_html=True)
    with st.expander("View detailed BMI advice"):
        st.markdown(f"**Lifestyle / Dietary Remedy:**<br>{PROFESSIONAL_ADVICE[bmi_cat]['remedy']}", unsafe_allow_html=True)
        st.markdown(f"**Physical / Behavioral Measures:**<br>{PROFESSIONAL_ADVICE[bmi_cat]['physical']}", unsafe_allow_html=True)
        st.markdown(f"**Medical / Tablet note:**<br>{PROFESSIONAL_ADVICE[bmi_cat]['tablet']}", unsafe_allow_html=True)

    # BP block
    pstatus, pcls = RISK_STATUS[bp_cat]
    st.markdown(f"<div class='card'><b>Blood Pressure:</b> {bp_score} — <b>{bp_cat}</b> &nbsp; {badge_html(pstatus, pcls)}</div>", unsafe_allow_html=True)
    with st.expander("View detailed BP advice"):
        st.markdown(f"**Lifestyle / Dietary Remedy:**<br>{PROFESSIONAL_ADVICE[bp_cat]['remedy']}", unsafe_allow_html=True)
        st.markdown(f"**Physical / Monitoring Measures:**<br>{PROFESSIONAL_ADVICE[bp_cat]['physical']}", unsafe_allow_html=True)
        st.markdown(f"**Medical / Tablet note:**<br>{PROFESSIONAL_ADVICE[bp_cat]['tablet']}", unsafe_allow_html=True)

    # Sugar block
    sstatus, scls = RISK_STATUS[sugar_cat]
    st.markdown(f"<div class='card'><b>Fasting Blood Glucose:</b> {sugar_score} — <b>{sugar_cat}</b> &nbsp; {badge_html(sstatus, scls)}</div>", unsafe_allow_html=True)
    with st.expander("View detailed Sugar advice"):
        st.markdown(f"**Lifestyle / Dietary Remedy:**<br>{PROFESSIONAL_ADVICE[sugar_cat]['remedy']}", unsafe_allow_html=True)
        st.markdown(f"**Physical / Self-care Measures:**<br>{PROFESSIONAL_ADVICE[sugar_cat]['physical']}", unsafe_allow_html=True)
        st.markdown(f"**Medical / Tablet note:**<br>{PROFESSIONAL_ADVICE[sugar_cat]['tablet']}", unsafe_allow_html=True)

    # Actionable next steps
    st.markdown("---")
    st.markdown("### ✅ Actionable Next Steps (what to do now)")
    st.markdown("- If any category is **CRITICAL / BAD**, contact a physician urgently.")
    st.markdown("- Start the recommended physical measures immediately (walk, reduce sugar/salt).")
    st.markdown("- Keep a log of BP and glucose for 1–2 weeks and show to your doctor.")
    st.markdown("- This tool is **informational only**. Do not start or stop medications without medical advice.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p class='muted small'>Report created by <b>Naseem Ahamed</b> • For educational/informational use only.</p>", unsafe_allow_html=True)
    st.balloons()

# ---------------- Footer / disclaimer ----------------
st.markdown("---")
st.markdown("<p class='muted small'><b>Clinical disclaimer:</b> This app provides generalized guidance based on standard clinical categories. It is NOT a diagnostic tool. Always consult a licensed physician for diagnosis, medication, and treatment decisions.</p>", unsafe_allow_html=True)

