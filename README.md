# AI-Powered-Cloud-Cost-Optimizer-FinOps-ML-Project-

An AI-driven cloud cost optimization tool that detects anomalies, predicts future spending, and provides actionable FinOps recommendations using Python, Machine Learning, and Streamlit.

---

## 🔥 Features

- 📊 Load and analyze cloud cost data
- 🚨 Detect anomalies using statistical methods
- 📈 Predict future cloud costs using Machine Learning
- 💡 Generate cost optimization recommendations
- 🖥️ Interactive dashboard using Streamlit

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---
# Folder structure

ai-cloud-cost-optimizer/
│
├── data/
│ └── cost_data.csv
│
├── main.py # Core logic (AI + ML)
├── app.py # Streamlit dashboard
└── README.md


---

## 📄 Sample Data (`data/cost_data.csv`)

date,service,cost
2026-03-01,Compute,120
2026-03-02,Compute,130
2026-03-03,Compute,500
2026-03-04,Storage,80
2026-03-05,Compute,140
2026-03-06,Storage,90

---

## ▶️ How to Run

### 1. Clone Repository

git clone <your-repo-link>
cd ai-cloud-cost-optimizer


### 2. Create Virtual Environment

python -m venv venv
source venv/Scripts/activate # Git Bash (Windows)


### 3. Install Dependencies

pip install pandas numpy scikit-learn streamlit


---

## ▶️ Run Project (CLI)


python main.py


---

## ▶️ Run Dashboard (Recommended)


streamlit run app.py

---

👉 Opens in browser automatically  
👉 Shows data, anomalies, prediction & recommendations

---

## 📊 What It Does

- Detects unusual spikes in cloud cost (e.g., sudden jump to 500)
- Predicts next-day cloud spend using Linear Regression
- Suggests cost optimization actions:
  - Compute → Resize / Reserved Instances
  - Storage → Lifecycle / Tiering

---

## 💡 Use Case

This project simulates real-world **FinOps (Cloud Cost Optimization)** scenarios similar to:

- Azure Cost Management
- AWS Cost Explorer
- GCP Billing Insights

---

## 🚀 Future Improvements

- Integrate real cloud billing APIs (Azure/AWS/GCP)
- Add advanced ML models (Prophet, LSTM)
- Deploy as a web application
- Add alerting system (email/slack)
---

## 👩‍💻 Author

**Khushboo Sharma**  
Cloud & FinOps automation
