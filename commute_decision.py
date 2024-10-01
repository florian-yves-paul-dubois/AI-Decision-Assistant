# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:59:06 2024

@author: Florian Yves Paul DUBOIS
"""


# Function to make decisions based on the conditions
def commute_decision_extended(rain, heavy_traffic, early_meeting, strike, appointment=False, road_construction=False):
    return {
        "WFH": rain or early_meeting,  # Work from home if it's raining or you have an early meeting
        "Drive": appointment or (not rain and not heavy_traffic and not road_construction),  # Drive if no rain, light traffic, no road construction, or if there's an appointment
        "PublicTransport": not strike and not rain  # Use public transport if no strike and no rain
    }

# Function used to query decisions based on the commute options
def query_commute(decisions, query):
    if query == "WFH":
        return decisions["WFH"]
    elif query == "Drive":
        return decisions["Drive"]
    elif query == "PublicTransport":
        return decisions["PublicTransport"]
    else:
        return "Invalid query!"

# Function to check multiple scenarios and print the results of the scnearios
def check_scenarios(scenarios):
    for idx, scenario in enumerate(scenarios, 1):
        decisions = commute_decision_extended(**scenario)
        print(f"Scenario {idx}:")
        print(f"  Work From Home: {decisions['WFH']}")
        print(f"  Drive: {decisions['Drive']}")
        print(f"  Public Transport: {decisions['PublicTransport']}")
        print("-" * 30)



# Task 4: Example queries
def perform_queries():
    decisions = commute_decision_extended(rain=False, heavy_traffic=False, early_meeting=False, strike=False, appointment=True, road_construction=False)
    
    print("Query Results:")
    print(f"  Should I work from home? {query_commute(decisions, 'WFH')}")
    print(f"  Should I drive? {query_commute(decisions, 'Drive')}")
    print(f"  Should I take public transport? {query_commute(decisions, 'PublicTransport')}")
    print("-" * 30)
    
# Example scenarios for Task 6
scenarios_extended = [
    # Scenario 1: It’s raining, and there’s heavy traffic
    {"rain": True, "heavy_traffic": True, "early_meeting": False, "strike": False, "appointment": False, "road_construction": False},
    
    # Scenario 2: There’s a public transport strike, and it’s not raining
    {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": True, "appointment": False, "road_construction": False},
    
    # Scenario 3: There’s no rain, traffic is light, and there’s no strike
    {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": False, "appointment": False, "road_construction": False},
]

# Task 7: Add more rules for real-life situations
def commute_with_route_suggestions(rain, heavy_traffic, early_meeting, strike, appointment=False, road_construction=False, prefer_highway=False):
    decisions = commute_decision_extended(rain, heavy_traffic, early_meeting, strike, appointment, road_construction)
    
    # Bonus: Suggest route for driving based on preferences
    route = "Highway" if prefer_highway and not heavy_traffic else "Local roads" if not road_construction else "Avoid driving"
    return {
        **decisions,  # Keep original decisions
        "RouteSuggestion": route  # Add route suggestion if driving
    }

# Scenarios with more complex decision-making (for Task 7 and Bonus Task)
def extended_scenarios_with_routes():
    complex_scenarios = [
        {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": False, "appointment": False, "road_construction": True, "prefer_highway": True},  # Light traffic, prefer highway
        {"rain": False, "heavy_traffic": True, "early_meeting": False, "strike": False, "appointment": True, "road_construction": False, "prefer_highway": False},  # Appointment but heavy traffic
    ]
    
    for idx, scenario in enumerate(complex_scenarios, 1):
        decisions = commute_with_route_suggestions(**scenario)
        print(f"Complex Scenario {idx}:")
        print(f"  Work From Home: {decisions['WFH']}")
        print(f"  Drive: {decisions['Drive']}")
        print(f"  Public Transport: {decisions['PublicTransport']}")
        print(f"  Route Suggestion: {decisions['RouteSuggestion']}")
        print("-" * 30)

# Run section 
# Task 4: Queries based on different situations
perform_queries()

# Task 5: Model Checking by running predefined scenarios
check_scenarios(scenarios_extended)

# Task 7: More rules and bonus route suggestions
extended_scenarios_with_routes()
