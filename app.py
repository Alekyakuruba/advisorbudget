import streamlit as st
import openai
import pandas as pd
import matplotlib.pyplot as plt

# Set your OpenAI API key directly (no user input)
openai.api_key = "your-api-key-here"  # 🔐 <- Replace with your actual API key

# Streamlit UI
st.set_page_config(page_title="Smart Budget Advisor", layout="centered")
st.title("💸 Smart Budget Advisor")

# Input: Monthly income
income = st.number_input("Enter your total monthly income (₹)", min_value=0.0, format="%.2f")

# Expense Input Form
st.subheader("📋 Enter Your Expenses")
expense_data = []
with st.form("expense_form"):
    category = st.text_input("Category")
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Expense")

    if submitted and category:
        expense_data.append({"Category": category, "Amount": amount})
        st.success(f"Added {category} — ₹{amount}")

# Session state for expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

if submitted and category:
    st.session_state.expenses.append({"Category": category, "Amount": amount})

# Show data
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.write("### 🧾 Expense Table")
    st.dataframe(df)

    # Summary
    total_expense = df["Amount"].sum()
    savings = income - total_expense
    st.markdown(f"**Total Expenses:** ₹{total_expense:.2f}")
    st.markdown(f"**Savings:** ₹{savings:.2f}" if savings >= 0 else f"**⚠️ Overspending by:** ₹{-savings:.2f}")

    # Plot chart
    st.write("### 📊 Expense Distribution")
    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot(kind="bar", color="skyblue", ax=ax)
    ax.set_ylabel("Amount (₹)")
    ax.set_xlabel("Category")
    ax.set_title("Your Expenses")
    st.pyplot(fig)

    # GPT Advice
    st.

