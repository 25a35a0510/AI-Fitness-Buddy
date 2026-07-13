# 🏋️ AI Fitness Buddy

An AI-powered fitness assistant built using **IBM watsonx.ai**, the **Granite Foundation Model**, **Python**, and **Streamlit**. This application analyzes user health information and generates personalized workout plans, healthy diet recommendations, calorie estimates, water intake guidance, and motivational health tips using Artificial Intelligence.

---

## 📖 Project Overview

AI Fitness Buddy is an intelligent web application designed to help users achieve their fitness goals through personalized AI-powered recommendations.

The application calculates important health metrics such as **Body Mass Index (BMI)**, **daily calorie requirements**, and **recommended water intake**, then uses the **IBM Granite Foundation Model** available through **IBM watsonx.ai** to generate customized fitness plans based on the user's profile.

This project was developed as part of the **IBM SkillsBuild AI Internship Program** supported by **Edunet Foundation** and **AICTE**.

---

## ✨ Features

- 📊 BMI Calculator
- 🔥 Daily Calorie Estimator
- 💧 Water Intake Recommendation
- 🤖 AI-Powered Weekly Workout Plan
- 🥗 Personalized Healthy Diet Plan
- 💡 Daily Health Tips
- 💬 Motivational Fitness Suggestions
- 📄 Download Personalized Fitness Report
- 🎨 Modern Streamlit User Interface
- ☁️ IBM watsonx.ai Granite Model Integration

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application Framework |
| IBM watsonx.ai | AI Model Hosting |
| Granite Foundation Model | AI Recommendation Engine |
| IBM Watson Machine Learning | Model Inference |
| Pillow | Image Processing |

---

## ☁️ IBM Cloud Services Used

- IBM Cloud
- IBM watsonx.ai Studio
- IBM Watson Machine Learning
- IBM Granite Foundation Model

---

## 🏗️ System Architecture

```text
                User
                  │
                  ▼
      Streamlit Web Application
                  │
                  ▼
      User Health Information
   (Age, Gender, Height, Weight)
                  │
                  ▼
     Health Metric Calculations
     (BMI, Calories, Water Intake)
                  │
                  ▼
        IBM watsonx.ai Platform
                  │
                  ▼
     Granite Foundation Model
                  │
                  ▼
 AI Workout + Diet Recommendations
                  │
                  ▼
      Personalized Fitness Report
```

---

## 📂 Project Structure

```text
AI-Fitness-Buddy/
│
├── app.py
├── ai_model.py
├── utils.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── logo.png
│   ├── fitness_banner.png
│   ├── app_background.png
│   └── diet.png
│
└── screenshots/
    ├── home.png
    ├── dashboard.png
    └── ai_plan.png
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/25a35a0510/AI-Fitness-Buddy.git
```

### Navigate to the Project

```bash
cd AI-Fitness-Buddy
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Environment Variables

Create a `.env` file and add the following:

```text
API_KEY=YOUR_IBM_API_KEY
PROJECT_ID=YOUR_PROJECT_ID
URL=YOUR_IBM_REGION_URL
MODEL_ID=ibm/granite-4-h-small
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Application Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

---

### 📊 Health Dashboard

![Dashboard](screenshots/dashboard.png)

---

### 🤖 AI Personalized Fitness Plan

![AI Plan](screenshots/ai_plan.png)

---

---

## 🔄 Application Workflow

1. User enters personal health details.
2. The application calculates BMI.
3. Daily calorie requirement is estimated.
4. Recommended daily water intake is calculated.
5. User information is sent securely to IBM watsonx.ai.
6. Granite Foundation Model generates personalized fitness recommendations.
7. Results are displayed in an interactive dashboard.
8. User downloads the personalized fitness report.

---

## 🚀 Future Enhancements

- User Authentication
- Fitness Progress Tracking
- Exercise Demonstration Videos
- AI Chat Assistant
- Nutrition Database Integration
- Smartwatch Integration
- Multi-language Support
- Cloud Deployment

---

## 📈 Project Outcomes

- Automated BMI Analysis
- AI-Based Personalized Recommendations
- Improved User Engagement
- Interactive Health Dashboard
- Personalized Fitness Report Generation

---

## 🎯 Learning Outcomes

During this project, the following concepts were implemented:

- IBM watsonx.ai Integration
- Granite Foundation Model Inference
- Prompt Engineering
- Streamlit Web Application Development
- Health Data Analysis
- AI-powered Recommendation Systems
- Python Programming
- Cloud-based AI Services

---

## 👩‍💻 Author

SEERAPU RUSHIKA
B.Tech Student

Pragati Engineering College

AICTE – IBM SkillsBuild Internship Participant

---

## 🙏 Acknowledgements

- IBM SkillsBuild
- IBM watsonx.ai
- IBM Granite Foundation Models
- IBM Cloud
- Edunet Foundation
- AICTE

---

## 📜 License

This project is developed for educational and internship purposes only.

---
