# MamaAlert 🚑

AI-powered maternal triage system for rural healthcare in India.

## Problem
Delay in identifying pregnancy risks leads to preventable maternal deaths.

## Solution
MamaAlert helps health workers quickly assess risk using simple inputs.

## Features
- Risk classification (Safe / Monitor / Emergency)
- Works with minimal input
- Designed for low-resource settings

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   python app.py

3. Test API using Postman:
   POST /triage
   {
     "bp": 150,
     "swelling": "yes",
     "headache": "yes"
   }

## Future Scope
- USSD integration
- SMS alerts
- AI-based prediction model
