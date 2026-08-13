#Track the amount of rescues completed, during different times



import random
#Parameters and values
Simulation_Time = 1000            #Make sure to increase the simulation time
Numb_Ambulance = 4         # number of ambulances
Late_Rescues = 0
Completed = 0
Total_response_Time = 0
Call_Rate = 0.08            # How often emergency calls happen
Average_Travel = 10           # Not ready yet just for testing purposes
Average_Pickup = 4
Average_Hospital= 11
Critical = 8
Normal = 20
Successful_Rescues = 0
Critical_Percent = 0.15
Right_of_Way = False
#Methods
def exponential_time(rate):              # Random time generator
    return random.expovariate(rate)     #Generates random time until the next arrival
def travel_time():
    return exponential_time(1/Average_Travel)     #This generates one random travel time
def pickup_time():
    return exponential_time(1/Average_Pickup)
def hospital_time():
    return exponential_time(1/Average_Hospital)
def traffic_increase(current_time):
    hour = current_time % 24
    if 7 <= hour < 9:
        return 1.8 #This is for the morning when it is the busiest
    elif 16 <= hour < 19:
        return 1.6 #This is for the evening when it is the busiest
    else:
        return 1.0 #normal traffic
    if Right_of_Way:
        traffic = 1.0
    return traffic
if random.random() < Critical_Percent:
    target_response_time = Critical
else:
    target_response_time = Normal

#Data structure
current_time = 0                 #This is the time when we start the simulation
Available_Ambulances = Numb_Ambulance           #All ambulances are currently available
Waiting_Patients  = []                       # We have no patients yet
next_call = exponential_time(1/Call_Rate)          # Schedules the first emergency (This gives the time for when the next emergency will happen
completion_times = []                #No recues have been completed yet ###

#Model
while current_time < Simulation_Time:       #This just runs the clock until 1000
    if len(completion_times) > 0:
        next_completion = min(completion_times)
    else:
        next_completion = float("inf")
    if next_call < next_completion:        #Event, This decides what happens first like if it is a new emergency or rescue
        current_time = next_call
        if random.random() < 0.15:
            target_response_time = Critical
        else:
            target_response_time = Normal
        if Available_Ambulances > 0:  # Checks if an ambulance is free
            waiting_time = 0
            first_travel= travel_time() * traffic_increase(current_time)
            response_time = waiting_time +first_travel
            Total_response_Time = Total_response_Time + response_time

            if response_time <= target_response_time:
                Successful_Rescues = Successful_Rescues + 1
            else:
                Late_Rescues = Late_Rescues + 1
            Available_Ambulances = Available_Ambulances -1   #if an ambulance leaves then the number available decreases
            completed = Completed + 1
            service_time = (first_travel + pickup_time()+ travel_time()+ hospital_time())  #This adds up everything happening to see the time that we will have at the end
            completion_times.append(current_time + service_time)    # every ambulance that lives adds its finish time to the list
        else:
            Waiting_Patients.append(( current_time, target_response_time))       #If another patient is here but no ambulance is available.
        next_call = current_time + exponential_time(Call_Rate)       ###
    else:                                            #Event,When the ambulance is finishes, the simulation clock moves , the ambulance becomes available and completed rescue increases
        current_time = next_completion
        completion_times.remove(next_completion)
        Available_Ambulances = Available_Ambulances + 1
        Completed = Completed + 1
        if len(Waiting_Patients) > 0:                         # If we have patients, one gets the ambulance
            call_time, target_response_time = Waiting_Patients.pop(0)
            waiting_time = current_time - call_time
            first_travel = travel_time() * traffic_increase(current_time)
            response_time = waiting_time + first_travel

            Available_Ambulances = Available_Ambulances - 1
            Total_response_Time += response_time

            service_time = (first_travel + pickup_time()+ travel_time()+hospital_time())
            completion_times.append(current_time + service_time)
            if response_time <= target_response_time:
                Successful_Rescues +=1
            else:
                Late_Rescues +=1
if Successful_Rescues + Late_Rescues > 0:
    Average_Response_time = (Total_response_Time/ (Successful_Rescues + Late_Rescues))
    Success_Rate = (Successful_Rescues/(Successful_Rescues +Late_Rescues)) * 100
else:
    Average_Response_time = 0
    Success_Rate = 0
print(f"Simulation time: {current_time:.2f}")
print(f"Success rate: {Success_Rate:.1f}%")
print(f"Amount of complete rescues are : {Completed}")
print(f"Amount of successful rescues are : {Successful_Rescues}")
print(f"Amount of late rescues: {Late_Rescues}")
print(f"Average response time : {Average_Response_time:.2f} minutes")
print(f"Number of Patients waiting in a queue: {len(Waiting_Patients)}")
print(f"Number of available ambulances : {Available_Ambulances}")