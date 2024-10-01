# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:59:06 2024

@author: duboi
"""

# commute_decision.py

def commute_decision_extended(rain, heavy_traffic, early_meeting, strike, appointment=False, road_construction=False):
    # Define the rules with additional conditions
    wfh = rain or early_meeting  # Work from home if it's raining or you have an early meeting
    drive = not rain and not heavy_traffic and not road_construction  # Drive if no rain, light traffic, and no road construction
    public_transport = not strike and not rain  # Use public transport if no strike and no rain

    # Override decision if there's an appointment
    if appointment:
        drive = True  # Drive if there's a doctor's appointment

    # Collect decisions into a dictionary
    decisions = {
        "WFH": wfh,
        "Drive": drive,
        "PublicTransport": public_transport
    }

    return decisions


# Define different scenarios with the new conditions
scenarios_extended = [
    {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": False, "appointment": True, "road_construction": False},  # Scenario with appointment
    {"rain": True, "heavy_traffic": True, "early_meeting": False, "strike": False, "appointment": False, "road_construction": True},  # Scenario with road construction
]

# Evaluate each scenario with extended logic
for idx, scenario in enumerate(scenarios_extended, 1):
    decisions = commute_decision_extended(**scenario)
    print(f"Extended Scenario {idx}:")
    print(f"  Work From Home: {decisions['WFH']}")
    print(f"  Drive: {decisions['Drive']}")
    print(f"  Public Transport: {decisions['PublicTransport']}")
    print("-" * 30)
