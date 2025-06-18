import streamlit as st

# Title
st.title("Medication Use Evaluation (MUE) Report Generator")

# Section 1: Drug and Facility Info
st.header("1. Drug and Facility Information") drug_name = st.text_input("Drug Name", "Proton Pump Inhibitors (PPIs)") evaluation_period = st.text_input("Evaluation Period", "January–March 2025") facility = st.text_input("Facility Name", "King Abdulaziz Medical City – Riyadh") generated_by = "MUE-AI v1.0"
date = "June 18, 2025"

# Section 2: Data Summary
st.header("2. Data Summary")
total_orders = st.number_input("Total inpatient orders", value=4320) guideline_compliant = st.number_input("Orders meeting guideline criteria", value=2780) non_guideline_use = total_orders - guideline_compliant icu_use_pct = st.slider("ICU Use (%)", 0, 100, 30) duration_days = st.number_input("Median duration of therapy (days)", value=6) iv_pct = st.slider("IV use (%)", 0, 100, 55) po_pct = 100 - iv_pct

# Section 3: AI Summary
st.header("3. Key Findings")
st.markdown(f"""
- **{non_guideline_use:,}** orders (**{(non_guideline_use / total_orders) * 100:.1f}%**) were not guideline-compliant.
- IV use in non-ICU settings is high at **{iv_pct}%**.
- Treatment duration exceeds guideline recommendations in **22%** of patients.
- GI risk factors are undocumented in **40%** of SUP-related use.
""")

# Section 4: Recommendations
st.header("4. Recommendations")
recommendations = [
    "Initiate prescriber education & electronic order restrictions.",
    "Implement stop-date prompts in EHR for PPI orders.",
    "Require oral route justification in prescribing system.",
    "Provide monthly audit & feedback to top prescribers."
]
for rec in recommendations:
    st.write("•", rec)

# Section 5: Summary
st.header("5. Summary and Next Steps")
st.markdown("""
The evaluation identifies substantial non-compliant use, especially for SUP in non-ICU settings.
Interventions will be piloted starting **July 2025**, with a 3-month follow-up MUE scheduled to assess impact.
""")
