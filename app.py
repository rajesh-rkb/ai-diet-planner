import streamlit as st

st.title("AI Diet Planner for Indians🍍🥩🥚")
gender = st.selectbox("Select your Gender",["","Male","Female"])
if (gender != ""):
    if(gender == "Male"):
        st.image("image/male/bodyTypesMale.jpeg")
        body_type = st.selectbox("Select your Body Type",["","Skinny","Toned","fit","Athletic","Built","Strong Fat","Chubby"])
    elif (gender == "Female"):
        st.image("image/female/bodyTypesFemale.webp")  
        body_type = st.selectbox("Select your Body Type",["","Hourglass","Pear-Triangle","Apple-Round","Rectangle-Athletic","Inverted Triangle","Diamond","Top Hourglass","Bottom Hourglass","Petite","Tall"])  
    
    if (body_type):
        age = st.number_input("What is your age?",value=18,step=1,min_value=18,max_value=100)
        
        height_foots = st.number_input("Select height (ft)",value=1,step=1,min_value=1,max_value=10)
        heigh_inches = st.number_input("Select additional inches",value=0,step=1,min_value=0,max_value=11)
        
        weight_kg = st.number_input("Body Weight(Kg)",value=5,step=1)
        weight_grams = st.number_input("Select additional grams",value=0,step=100,min_value=0,max_value=900)
        
        sleep_time = st.time_input("When do you usually go to sleep")
        wakeup_time = st.time_input("When do you usually wake up")
        
        workout = st.selectbox("Do you work out daily?",["No","Yes"])
        if (workout == "Yes"):
            workout_type = st.selectbox("What is your workout type?",["WeavyLift","Normal"])
            workout_start_Time = st.time_input("When do you start your workout?")
            workout_duration = st.number_input("Select duration in minutes",value=0,step=10,min_value=0)

        running_walking_cycle = st.selectbox("Do you walk, run, or cycle daily?",["No","Yes"])
        if (running_walking_cycle == "Yes"):
            running_walking_cycle_duration = st.number_input("How many minutes do you walk, run, or cycle ",value=10,step=10,min_value=10)    

        working_person = st.selectbox("Are you a working professional?",["No","Yes","Homemaker"])
        if (working_person != "No"):
            if (working_person == "Yes"):            
                work_location = st.selectbox("Where do you work?",["","office","Work From Home","Hybrid"])
                work_start_timing = st.time_input("What time do you start work?")
                work_start_timing = st.time_input("What time do you finish work?")
                stressFullWork =  st.selectbox("Do you find your work stressful?",["No","Yes"])   
                work_active_level = st.selectbox("How active are you during work?",["Mostly sitting","Walking-Standing","Physical labor-Constant movement"]) 
            else:
                work_location = "home"   
                work_active_level = "Household work"       

        diet = st.selectbox("How would you describe your eating habits?",["Vegetarian","Non-Vegetarian","Eggetarian","Non-Vegetarian + Vegetarian(for some days)","Eggetarian + Vegetarian(for some days)"])    

        goal = st.selectbox("What is your Goal",["Weight loss","Weight Gain","Muscle Gain","Build Abs","Muscle Gain + Weight Maintain","Body Recomposition (Lose Fat, Gain Muscle)","Bulking (Muscle & Weight Gain)"])    
        city_name = st.text_input("Enter your  City Name")
        budget = st.number_input("Monthly Food Budget (₹)",value=0,step=100)

