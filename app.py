import os
from datetime import datetime

import streamlit as st
from PIL import Image

from utils import (
    calculate_bmi,
    calculate_water,
    calculate_calories,
)

from ai_model import get_ai_plan


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="🏋 AI FITNESS Buddy",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:2rem;
}

.main-title{
font-size:48px;
font-weight:800;
text-align:center;
color:#0F62FE;
}

.sub-title{
font-size:20px;
text-align:center;
color:#666666;
margin-bottom:25px;
}

.section-title{
font-size:28px;
font-weight:bold;
color:#0F62FE;
margin-top:30px;
margin-bottom:15px;
}

.metric-card{
background:#F4F4F4;
padding:20px;
border-radius:15px;
box-shadow:0px 3px 10px rgba(0,0,0,0.15);
text-align:center;
}

.plan-box{
background:#FAFAFA;
padding:20px;
border-radius:15px;
border-left:8px solid #0F62FE;
}

div.stButton > button{
width:100%;
height:60px;
font-size:22px;
font-weight:bold;
border-radius:12px;
background:#0F62FE;
color:white;
}

div.stButton > button:hover{
background:#0353E9;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    logo = "assets/logo.png"

    if os.path.exists(logo):
        st.image(logo, width=130)

    st.title("🏋️ Fitness Buddy")

    st.markdown("---")

    st.success("Powered by IBM watsonx.ai")

    st.write("### Features")

    st.write("✅ BMI Calculator")
    st.write("✅ Calories Calculator")
    st.write("✅ Water Intake Calculator")
    st.write("✅ AI Workout Planner")
    st.write("✅ AI Diet Planner")
    st.write("✅ Download Report")

    st.markdown("---")

    st.info("""
AI-powered Fitness Assistant

Technologies

• IBM watsonx.ai

• Granite Foundation Model

• Streamlit

• Python
""")
# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------

banner = "assets/fitness_banner.png"

if os.path.exists(banner):
    image = Image.open(banner)
    st.image(image, use_container_width=True)

st.markdown(
    """
    <div class='main-title'>
        🏋️ AI FITNESS Buddy
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='sub-title'>
        Your Personal AI Health Coach
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "🏆 Developed using IBM watsonx.ai | Granite Foundation Model | Streamlit | Python"
)
st.markdown("""
### 👋 Welcome!

Get your personalized **AI-powered fitness plan** in just a few seconds.

Our intelligent assistant analyzes your health metrics and generates:

✔ Personalized Workout Plan

✔ Healthy Diet Plan

✔ Daily Calorie Recommendation

✔ Water Intake Recommendation

✔ Motivational Health Tips
""")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🏋️\n\n**1000+**\nFitness Plans")

with col2:
    st.success("🤖\n\n**IBM AI**\nPowered")

with col3:
    st.warning("📊\n\n**Instant**\nHealth Analysis")

with col4:
    st.error("⚡\n\n**24/7**\nAI Coach")
st.markdown(
"""
Generate personalized fitness recommendations using Artificial Intelligence.

The application analyzes your BMI, daily calorie requirements,
water intake, and fitness goals to generate a customized
workout and diet plan using IBM watsonx.ai.
"""
)

st.divider()
col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
### 📊 Health Analysis

✔ BMI Calculator

✔ Calories Calculator

✔ Water Intake
""")

with col2:

    st.info("""
### 🤖 AI Coach

✔ Personalized Workout

✔ Healthy Diet

✔ Daily Motivation
""")

with col3:

    st.warning("""
### ☁ IBM Cloud

✔ IBM watsonx.ai

✔ Granite LLM

✔ Streamlit
""")

st.divider()
# ---------------------------------------------------------
# USER INPUT SECTION
# ---------------------------------------------------------

st.markdown(
    """
    <div class='section-title'>
        👤 Personal Information
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    "Fill in your details below to generate your personalized AI fitness plan."
)

left, right = st.columns(2)

# ---------------- LEFT COLUMN ----------------

with left:

    name = st.text_input(
        "👤 Full Name",
        placeholder="Enter your full name"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=10,
        max_value=100,
        value=20,
        step=1
    )

    gender = st.selectbox(
        "🚻 Gender",
        [
            "Male",
            "Female"
        ]
    )

# ---------------- RIGHT COLUMN ----------------

with right:

    height = st.number_input(
        "📏 Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

    weight = st.number_input(
        "⚖ Weight (kg)",
        min_value=20,
        max_value=200,
        value=65
    )

    goal = st.selectbox(
        "🎯 Fitness Goal",
        [
            "Stay Fit",
            "Lose Weight",
            "Gain Muscle"
        ]
    )

st.info(
    "💡 Tip: Accurate height and weight values help generate better AI recommendations."
)

st.write("")

generate = st.button(
    "🚀 Generate My AI Fitness Plan",
    use_container_width=True
)
if not generate:

    st.markdown("### 🌟 What You'll Get")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("📊 BMI Analysis", "Instant")

    with c2:
        st.metric("🤖 AI Plan", "Personalized")

    with c3:
        st.metric("📥 Report", "Downloadable")
       # ---------------------------------------------------------
# GENERATE FITNESS PLAN
# ---------------------------------------------------------

if generate:

    # Validate input
    if not name.strip():
        st.warning("⚠ Please enter your name.")
        st.stop()

    # -------------------------------
    # Calculate Health Metrics
    # -------------------------------

    bmi, category = calculate_bmi(weight, height)
    water = calculate_water(weight)
    calories = calculate_calories(weight, height, age, gender)

    st.divider()

    st.markdown(
        """
        <div class='section-title'>
            📊 Health Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📈 BMI",
            bmi
        )

    with c2:
        st.metric(
            "❤️ Category",
            category
        )

    with c3:
        st.metric(
            "💧 Water Intake",
            f"{water} L"
        )

    with c4:
        st.metric(
            "🔥 Calories",
            f"{calories} kcal"
        )

    st.write("")

    # -------------------------------
    # BMI Status
    # -------------------------------

    if category == "Normal Weight":
        st.success("✅ Great! Your BMI is within the healthy range.")

    elif category == "Underweight":
        st.warning("⚠ You are underweight. Consider a balanced diet and strength training.")

    elif category == "Overweight":
        st.warning("⚠ You are overweight. Regular exercise and a healthy diet are recommended.")

    else:
        st.error("❌ Your BMI indicates obesity. Please consult a healthcare professional.")

    st.write("")

    # -------------------------------
    # Water Progress
    # -------------------------------

    st.subheader("💧 Daily Water Goal")

    target_water = 3.0

    progress = min(water / target_water, 1.0)

    st.progress(progress)

    st.caption(f"{water} L of {target_water} L recommended")

    st.write("")

    # -------------------------------
    # BMI Reference
    # -------------------------------

    with st.expander("📖 BMI Reference Chart"):

        st.table({
            "BMI Range": [
                "Below 18.5",
                "18.5 - 24.9",
                "25 - 29.9",
                "30 and above"
            ],
            "Category": [
                "Underweight",
                "Normal Weight",
                "Overweight",
                "Obese"
            ]
        })
        

    st.divider()
    

    # -------------------------------
    # AI Plan
    # -------------------------------
    

    with st.spinner("🤖 IBM Granite is generating your personalized fitness plan..."):

        plan = get_ai_plan(
            name,
            age,
            gender,
            bmi,
            goal
        )
       # ---------------------------------------------------------
    # AI FITNESS REPORT
    # ---------------------------------------------------------

    st.divider()

    st.markdown(
        """
        <div class='section-title'>
            🤖 AI Personalized Fitness Report
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("✅ Your personalized AI fitness plan has been generated successfully!")

    tab1, tab2 = st.tabs(
        [
            "🏋️ Fitness Plan",
            "📄 Complete Report"
        ]
    )

    # ----------------------------
    # FITNESS PLAN TAB
    # ----------------------------

    with tab1:

        st.markdown("### 🏋️ Personalized Workout & Diet")

        st.markdown(plan)

    # ----------------------------
    # COMPLETE REPORT TAB
    # ----------------------------

    with tab2:

        st.subheader("👤 Personal Information")

        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Fitness Goal:** {goal}")

        st.divider()

        st.subheader("📊 Health Analysis")

        st.write(f"**BMI:** {bmi}")
        st.write(f"**Health Category:** {category}")
        st.write(f"**Daily Water Intake:** {water} L")
        st.write(f"**Daily Calories:** {calories} kcal")

        st.divider()

        st.subheader("🤖 AI Generated Plan")

        st.markdown(plan)
            # ---------------------------------------------------------
    # DOWNLOAD REPORT
    # ---------------------------------------------------------

    report = f"""
AI FITNESS BUDDY REPORT
======================================

Generated on:
{datetime.now().strftime("%d-%m-%Y %I:%M %p")}

--------------------------------------

PERSONAL DETAILS

Name : {name}
Age : {age}
Gender : {gender}

Height : {height} cm
Weight : {weight} kg

Goal : {goal}

--------------------------------------

HEALTH SUMMARY

BMI : {bmi}

Category : {category}

Water Intake : {water} L

Calories : {calories} kcal

--------------------------------------

AI FITNESS PLAN

{plan}

======================================

Powered by IBM watsonx.ai
Granite Foundation Model
"""

    st.download_button(
        label="📥 Download Fitness Report",
        data=report,
        file_name=f"{name}_Fitness_Report.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.divider()

st.markdown(
    """
    <div style='text-align:center;color:gray;'>
        ❤️ Built using <b>Streamlit</b> • <b>IBM watsonx.ai</b> • <b>Granite Foundation Model</b>
    </div>
    """,
    unsafe_allow_html=True
)
    