import streamlit as st
import openai
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit Page Configuration
st.set_page_config(page_title="Smart Budget Advisor", layout="centered")

# Title
st.title("💸 Smart Budget Advisor")

# Sidebar for API Key
st.sidebar.header("🔐 API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")
openai.api_key = api_key

# Input: Monthly income
income = st.number_input("Enter your total monthly income (₹)", min_value=0.0, format="%.2f")

# Expense Entry
st.subheader("📋 Enter Your Expenses")
expense_data = []
with st.form("expense_form"):
    category = st.text_input("Category")
    amount = st.number_input("Amount (₹)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Expense")

    if submitted and category:
        expense_data.append({"Category": category, "Amount": amount})
        st.success(f"Added {category} — ₹{amount}")

# Persist expenses using session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

if submitted and category:
    st.session_state.expenses.append({"Category": category, "Amount": amount})

# Show table
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.write("### 🧾 Expense Table")
    st.dataframe(df)

    # Summary
    total_expense = df["Amount"].sum()
    savings = income - total_expense
    st.markdown(f"**Total Expenses:** ₹{total_expense:.2f}")
    st.markdown(f"**Savings:** ₹{savings:.2f}" if savings >= 0 else f"**⚠️ Overspending by:** ₹{-savings:.2f}")

    # Chart
    st.write("### 📊 Expense Distribution")
    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot(kind="bar", color="skyblue", ax=ax)
    ax.set_ylabel("Amount (₹)")
    ax.set_xlabel("Category")
    ax.set_title("Your Expenses")
    st.pyplot(fig)

    # GPT Advice
    if api_key:
        st.write("### 🧠 Budgeting Advice from GPT")
        prompt = f"My monthly income is ₹{income}. Here are my expenses:\n"
        for _, row in df.iterrows():
            prompt += f"- {row['Category']}: ₹{row['Amount']}\n"
        prompt += "Please give me smart advice to improve my savings."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a financial advisor helping users save money."},
                    {"role": "user", "content": prompt}
                ]
            )
            advice = response.choices[0].message.content
            st.success(advice)
        except Exception as e:
            st.error(f"Error fetching advice: {e}")
    else:
        st.warning("Please enter your OpenAI API key in the sidebar to get advice.")

else:
    st.info("Add some expenses to begin.")

