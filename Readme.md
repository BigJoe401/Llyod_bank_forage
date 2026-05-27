# 🏦 Lloyds Bank Customer Churn Prediction & Analytics Engine

An end-to-end predictive analytics framework designed to analyze banking behaviors, evaluate customer interaction touchpoints, and forecast churn indicators using advanced machine learning models. Built using a decoupling philosophy, this project translates multiple complex financial data sources into clean feature-engineered sets optimized for high-recall operational interventions.

---

# 🚀 Features

* 📊 **Multi-Source Data Aggregation:** Automatically merges transactional records, service interaction history, profiles, and engagement levels into a unified master frame.
* 🧠 **Advanced Feature Engineering:** Computes financial metrics such as recency flags, spend density per inactive day, and localized service tracking variables.
* ⚖️ **Cost-Sensitive Learning:** Employs tree-structure cost weighting (`balanced_subsample`) inside the ensemble algorithm to counter highly skewed class ratios without inflating dataset size.
* 🛠️ **Rigorous Evaluation Strategy:** Integrates Stratified $K$-Fold Cross-Validation alongside targeted precision-recall threshold optimization to maximize predictive sensitivity.

---

# 🧠 Tech Stack

* **Data Engineering & Manipulation:** Python, Pandas, NumPy, OpenPyXL
* **Statistical Testing:** SciPy Stats (Chi-Square Test of Independence)
* **Machine Learning Library:** Scikit-Learn (Sklearn)
* **Data Visualization Layer:** Seaborn, Matplotlib

---

# 📂 Project Structure

```bash
Llyod_Group/
│
├── data/
│   ├── Customer_Churn_Data.xlsx
│   ├── Transaction_Logs.xlsx
│   ├── Interaction_Logs.xlsx
│   └── Support_Tickets.xlsx
│
├── model/
│   └── random_forest_churn_v1.pkl
│
├── Llyod_Group.ipynb    # Research, EDA, Hypothesis Testing, and Model Architecture Validation
├── app.py              # Operational Streamlit Interface & Dashboard Analytics Engine
├── utils.py            # Core pipeline operations (Preprocessing, Feature Mapping, and Inference Engine)
├── requirements.txt    # Production runtime dependencies
└── README.md           # Project Documentation