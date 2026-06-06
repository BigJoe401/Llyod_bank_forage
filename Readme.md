# 🏦 Lloyds Bank Customer Churn Prediction & Analytics Engine

An end-to-end predictive analytics framework designed to analyze banking behaviors, evaluate customer interaction touchpoints, and forecast churn indicators using advanced machine learning models. Built using a decoupling philosophy, this project translates multiple complex financial data sources into clean feature-engineered sets optimized for high-recall operational interventions.

## 🔗 Live Demo
Deploy and test the live application here: [https://bigjoe401-llyod-bank-forage-app-gaqsrv.streamlit.app/](https://bigjoe401-llyod-bank-forage-app-gaqsrv.streamlit.app/)

---

## 📊 Dashboard Update

This section highlights recent enhancements and dashboard improvements implemented for the Lloyds Banking Group analytics platform. The updates focus on providing clearer insights, improved usability, and a better overall reporting experience.

---

## 📈 KPI Image 

The KPI Image presents key business metrics and performance indicators in a centralized view, enabling users to quickly monitor trends and assess overall performance.

### Screenshot

> *./screenshot/KPI-Lloyd.png*

```
![KPI Page - Lloyds Banking Group]
```

![KPI Page - Lloyds Banking Group](./screenshot/KPI-Lloyd.png)

---

## 📊 Comparison Image

The Comparison Image enables users to evaluate metrics across different periods, categories, or business segments. This functionality supports deeper analysis and helps drive data-informed decisions.

### Screenshot

> *./screenshots/Comparison_page-Llyod*

```text
[ Comparison Page Screenshot - Lloyds Banking Group ]
```

---

## 🚀 Summary of Improvements

* Enhanced KPI visibility and reporting capabilities
* Improved comparison views for more effective analysis
* Streamlined dashboard layout for a better user experience
* Increased accessibility and readability across dashboard components

---

For additional information and future updates, please refer to the main project documentation or contact the development team.


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