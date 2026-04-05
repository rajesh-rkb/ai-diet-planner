import streamlit as st

st.title("AI Diet Planner for Indians🍍🥩🥚")
city = st.text_input("Please enter your City Name")
if city:
    gender = st.selectbox("Select your Gender",["Female","Male"])
    age = st.number_input("Select your age",value=18,step=1,min_value=18,max_value=100)
    height_foots = st.number_input("Select your height in foot",value=1,step=1,min_value=1,max_value=10)
    heigh_inches = st.number_input("Select extra inches",value=0,step=1,min_value=0,max_value=11)
    weight_kg = st.number_input("Select your weight in Kg",value=5,step=1)
    weight_grams = st.number_input("Select extra grams",value=0,step=100,min_value=0,max_value=900)
    sleep_time = st.time_input("Select usual time of sleeping")
    wakeup_time = st.time_input("Select usual wakeup timing")
    diet = st.selectbox("Are you a ",["Vegetarian","Non-Vegetarian","Eggetarian","Non-Vegetarian + Vegetarian(for some days)","Eggetarian + Vegetarian(for some days)"])
    
    workout = st.selectbox("Do you workout daily",["No","Yes"])
    if (workout == "Yes"):
        workout_type = st.selectbox("Workout Type",["WeavyLift","Noraml"])
        workout_start_Time = st.time_input("Select the Start timing of your workout session")
        workout_duration = st.number_input("Select in Minutes",value=0,step=10,min_value=0)
    
    running_walking_cycle = st.selectbox("Do you Walk/Run/Cycling daily",["No","Yes"])
    if (running_walking_cycle == "Yes"):
        running_walking_cycle_duration = st.number_input("For how many minutes ",value=10,step=10,min_value=10)
    
    working_person = st.selectbox("Are you are working Person",["No","Yes","HouseWife/HouseHusband"])
    if (working_person == "Yes"):
        work_start_timing = st.time_input("Select the Start timing of your work")
        work_start_timing = st.time_input("Select the End timing of your work")
    
    goal = st.selectbox("What is your Goal",["Weight loss","Weight Gain","Muscle Gain","Abs","Muscle Gain + Weight Maintain","Muscle Gain + Weight loss","Muscle Gain + Weight Gain"])    
    budget = st.number_input("Monthly How much you can spend on diet/food in rupees",value=500,step=100,min_value=500)

