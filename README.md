# 💸 Smart Budget Advisor

**Smart Budget Advisor** is an AI-powered budgeting tool that helps users analyze their income and expenses using OpenAI's GPT API. It provides smart, personalized financial advice and suggestions to help users make informed financial decisions.

Built using **Streamlit** and **Python**, this project is ideal for anyone looking to better understand their spending habits and optimize their monthly budget.

---

## 📌 Features

- 🧠 GPT-powered financial analysis  
- 💬 Natural language suggestions and breakdown  
- 📊 Smart allocation using 50/30/20 budgeting rule  
- 🔒 No personal data stored  
- ⚡️ Fast and user-friendly Streamlit web interface  

---

## 📁 Project Structure

```
advisorbudget/
├── app.py                   # Streamlit app source code
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── assets/
    └── sample_output.png    # (Optional) UI screenshot of app
```

---

## 💡 How It Works

1. User inputs monthly income and a list of expenses.  
2. The app formats this input into a prompt for the OpenAI GPT API.  
3. GPT returns:
   - Summary of expenses
   - Suggestions to cut costs
   - Savings recommendations
   - Expense distribution (needs, wants, savings)  
4. The output is shown inside the Streamlit interface.

---

## 🧪 Sample Input

```
Income: ₹50,000

Expenses:
- Rent: ₹12,000
- Groceries: ₹6,000
- Transport: ₹3,000
- Entertainment: ₹4,000
- Subscriptions: ₹1,000
```

---

## 📤 Sample Output

```
💡 Budget Analysis:
You've spent ₹26,000, which is 52% of your monthly income.

📌 Suggestions:
- Try to reduce entertainment expenses to ₹2,000/month.
- Subscriptions may be optimized — consider cancelling unused ones.

✅ Ideal Distribution (50/30/20 Rule):
- Needs (50%): ₹25,000
- Wants (30%): ₹15,000
- Savings (20%): ₹10,000

👏 You can potentially save ₹24,000. Great work!
```

---
## 🖼 Sample Outputs

### 📊 Budget Overview

![Budget Overview](assets/input.png)

---

### 📉 Budget Breakdown

![Budget Breakdown](assets/expenses_table.png)

---

### 💬 Financial Suggestions

![Suggestions](assets/budget_advice.png)

---

## 🚀 Deploy on Streamlit Cloud

1. Push this project to your GitHub account.  
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud).  
3. Connect your GitHub repository.  
4. Add `OPENAI_API_KEY` under "Secrets".  
5. Click "Deploy" – your app is live!

---

## 🧰 Technologies Used

- **Python** – Core programming language  
- **Streamlit** – Frontend web interface  
- **OpenAI GPT-3.5 Turbo** – AI model for financial advice  
- **Markdown** – For documentation
---


## 🙋‍♀️ Author & Contributions

Developed by [K.Alekya].  

> Made with 💙 using OpenAI and Streamlit.


