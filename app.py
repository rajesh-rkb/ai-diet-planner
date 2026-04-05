import streamlit as st

st.title("AI Diet Planner for Indians🍍🥩🥚")
gender = st.selectbox("Select your Gender",["","Male","Female"])
if (gender != ""):
    if(gender == "Male"):
        st.image("/workspaces/ai-diet-planner/image/male/bodyTypesMale.jpeg")
        body_type = st.selectbox("Select your Body Type",["","Skinny","Toner","fit","Athletic","Built","String FAt","Chubby"])
    elif (gender == "Female"):
        st.image("/workspaces/ai-diet-planner/image/female/bodyTypesFemale.webp")  
        body_type = st.selectbox("Select your Body Type",["","Hourglass","Pear-Triangle","Apple-Round","Rectangle-Athletic","Inverted Triangle","Diamon","Top HourGlass","Bottom Hourgass","Petite","Tall"])  
    
    if (body_type):
        age = st.number_input("Select your age",value=18,step=1,min_value=18,max_value=100)
        
        height_foots = st.number_input("Select your height in foot",value=1,step=1,min_value=1,max_value=10)
        heigh_inches = st.number_input("Select extra inches",value=0,step=1,min_value=0,max_value=11)
        
        weight_kg = st.number_input("Select your weight in Kg",value=5,step=1)
        weight_grams = st.number_input("Select extra grams",value=0,step=100,min_value=0,max_value=900)
        
        sleep_time = st.time_input("Select usual time of sleeping")
        wakeup_time = st.time_input("Select usual wakeup timing")
        
        workout = st.selectbox("Do you workout daily",["No","Yes"])
        if (workout == "Yes"):
            workout_type = st.selectbox("Workout Type",["WeavyLift","Noraml"])
            workout_start_Time = st.time_input("Select the Start timing of your workout session")
            workout_duration = st.number_input("Select in Minutes",value=0,step=10,min_value=0)

        running_walking_cycle = st.selectbox("Do you Walk/Run/Cycling daily",["No","Yes"])
        if (running_walking_cycle == "Yes"):
            running_walking_cycle_duration = st.number_input("Duration of (Walk/Run/Cycling) ",value=10,step=10,min_value=10)    

        working_person = st.selectbox("Are you are working Person",["No","Yes","HouseWife/HouseHusband"])
        if (working_person == "Yes"):            
            work_location = st.selectbox("What is your work location",["","office","Home",])
            if (work_location):
                work_start_timing = st.time_input("Select the Start timing of your work")
                work_start_timing = st.time_input("Select the End timing of your work")
            stressFullWork =  st.selectbox("Is your Work StreasFull? ",["No","Yes"])   

            
        diet = st.selectbox("Are you a ",["Vegetarian","Non-Vegetarian","Eggetarian","Non-Vegetarian + Vegetarian(for some days)","Eggetarian + Vegetarian(for some days)"])    