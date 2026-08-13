# Emergency_System
# Research Question : How does limited access to emergency medical services affect the response time for aid provided to women in Togo in 2025?
# Model
1 center
4 ambulances
Traffic policy
Emergency call
Critical vs Normal condition
Travel, pickup, and hospital 
Traffic increase
Response times
Successful vs late rescues
Patients waiting ambulance in a queue
Ambulance availability
# Objects
Ambulances
Emergency calls
Rescues
Simulation time
# State
Number of ambulances available
Patients waiting
Current simulation time
Patients condition
Emergencies
Successful rescues and late rescues
# State Modification
Emergency call is received
Ambulance is sent out
Patient is seen or enters queue
Ambulance completes the rescue
Patients in queue receive the ambulance
Response time is calculated
Ambulance becomes available
# Methods/functions
exponential_time()
travel_time()
pickup_time()
hospital_time()
traffic_increase()
# Data structure
Waiting patients go in the queue
A list of completion times
