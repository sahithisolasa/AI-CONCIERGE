import streamlit as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI CONCIERGE", layout="wide")

# ---------- UI STYLE (BLACK + WHITE + GOLD) ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #000000, #111111);
    color: #ffffff;
}

.block-container {
    max-width: 1000px;
    margin: auto;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    color: #FFD700;
}

.subtitle {
    text-align: center;
    color: #aaaaaa;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
}

button[kind="primary"] {
    background: linear-gradient(90deg, #FFD700, #C0C0C0);
    color: black !important;
    border-radius: 12px;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
}

.stNumberInput input {
    background-color: #111 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">AI CONCIERGE</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Financial Intelligence System</div>', unsafe_allow_html=True)

# ---------- FORM ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("## 🧠 Financial Profile")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 60, 23)

    income = st.text_input("Monthly Income (₹)", placeholder="Enter exact income")

    savings_existing = st.text_input("Current Savings (₹)", placeholder="Optional")

    employment = st.selectbox(
        "Employment Type",
        ["Student", "Salaried", "Self-employed", "Business"]
    )

with col2:
    expense = st.text_input("Monthly Expenses (₹)", placeholder="Enter exact expenses")

    debt = st.text_input("Monthly EMI / Debt (₹)", placeholder="0 if none")

    goal = st.selectbox(
        "Financial Goal",
        ["Emergency fund", "Buy house/car", "Build wealth", "Early retirement"]
    )

    horizon = st.selectbox(
        "Investment Horizon",
        ["< 1 year", "1-3 years", "3-5 years", "5+ years"]
    )

risk = st.selectbox(
    "Market Reaction",
    ["Sell everything", "Wait and watch", "Invest more"]
)

generate = st.button("✨ Generate Smart Plan")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- OUTPUT ----------
if generate:

    try:
        income_val = int(income)
        expense_val = int(expense)
        debt_val = int(debt) if debt else 0
    except:
        st.error("⚠️ Please enter valid numeric values")
        st.stop()

    payload = {
        "age": age,
        "income": income_val,
        "expense": expense_val,
        "goal": goal,
        "risk": risk
    }

    res = requests.post("http://127.0.0.1:8000/recommend", json=payload)

    if res.status_code == 200:
        result = res.json()

        st.markdown("## ✅ Your Financial Blueprint")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("👤 Profile Type")
            st.success(result["type"])

            st.subheader("📊 Financial Summary")
            st.write(result["advice"])

        with col2:
            st.subheader("📦 Recommended Tools")
            for s in result["services"]:
                st.write("✔", s)

            st.subheader("📌 Next Steps")
            st.write(result["next_steps"])

        st.subheader("📊 Investment Allocation")
        st.success(result["allocation"])

        # ---------- ADVANCED BAR CHART ----------
        savings = income_val - expense_val - debt_val

        if savings >= 0:
            st.subheader("📊 Monthly Financial Breakdown")

            categories = ["Income", "Expenses", "Debt", "Savings"]
            values = [income_val, expense_val, debt_val, savings]

            fig, ax = plt.subplots()
            ax.bar(categories, values)

            ax.set_ylabel("Amount (₹)")
            ax.set_title("Financial Distribution")

            st.pyplot(fig)

        else:
            st.warning("⚠️ You are overspending. Reduce expenses or debt.")