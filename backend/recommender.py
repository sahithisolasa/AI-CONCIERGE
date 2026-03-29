def generate_recommendation(profile):

    income = profile["income"]
    expense = profile["expense"]
    goal = profile["goal"]
    risk = profile["risk"]

    # -------- VALIDATION --------
    if income <= 0:
        return {
            "type": "Insufficient Data",
            "advice": "Please enter valid monthly income.",
            "allocation": "N/A",
            "services": [],
            "next_steps": "Provide income details."
        }

    # -------- CALCULATIONS --------
    savings = income - expense

    if savings <= 0:
        return {
            "type": "Financial Stress",
            "advice": f"Your expenses (₹{expense}) exceed income (₹{income}). Reduce expenses first.",
            "allocation": "Focus 100% on expense control",
            "services": ["ET Prime - Budgeting"],
            "next_steps": "Track expenses daily and cut unnecessary costs."
        }

    savings_rate = (savings / income) * 100

    # -------- RISK SCORING --------
    if risk == "Sell everything":
        risk_score = 1
    elif risk == "Wait and watch":
        risk_score = 2
    else:
        risk_score = 3

    # -------- USER TYPE --------
    if savings_rate < 10:
        user_type = "Low Saver"
    elif risk_score == 1:
        user_type = "Conservative Investor"
    elif risk_score == 2:
        user_type = "Balanced Investor"
    else:
        user_type = "Aggressive Investor"

    # -------- ALLOCATION --------
    if risk_score == 1:
        allocation = f"""
₹{int(savings*0.7)} → Safe Savings  
₹{int(savings*0.2)} → Mutual Funds  
₹{int(savings*0.1)} → Gold
"""
    elif risk_score == 2:
        allocation = f"""
₹{int(savings*0.4)} → Mutual Funds  
₹{int(savings*0.4)} → Stocks  
₹{int(savings*0.2)} → Emergency Fund
"""
    else:
        allocation = f"""
₹{int(savings*0.7)} → Stocks  
₹{int(savings*0.2)} → High-Risk Assets  
₹{int(savings*0.1)} → Emergency Fund
"""

    # -------- FINAL ADVICE --------
    advice = f"""
Monthly Income: ₹{income}  
Expenses: ₹{expense}  
Savings: ₹{savings} ({round(savings_rate,1)}%)

You are doing {'great' if savings_rate > 30 else 'okay'}, but can improve savings discipline.
"""

    return {
        "type": user_type,
        "advice": advice,
        "allocation": allocation,
        "services": [
            "ET Prime (Insights)",
            "ET Markets (Tracking)",
            "ET Learning (Masterclasses)"
        ],
        "next_steps": "Invest monthly, review every 3 months, increase savings gradually."
    }