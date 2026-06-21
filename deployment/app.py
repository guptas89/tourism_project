import streamlit as st
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

# Download and load the trained model
model_path = hf_hub_download(
    repo_id="guptas89/tourism-prediction-model",
    filename="best_tourism_model_v1.joblib"
)

model = joblib.load(model_path)

st.title("🌴 Tourism Package Purchase Prediction")
st.write("Enter customer details to predict if they will purchase a tourism package")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    typeofcontact = st.selectbox("Type of Contact", ["Self Enquiry", "Company Invited"])
    citytier = st.selectbox("City Tier", [1, 2, 3])
    durationofpitch = st.number_input("Duration of Pitch (minutes)", min_value=0, max_value=100, value=15)
    occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Large Business", "Free Lancer"])
    gender = st.selectbox("Gender", ["Male", "Female"])
    numberofpersonvisiting = st.number_input("Number of Persons Visiting", min_value=1, max_value=10, value=2)
    numberoffollowups = st.number_input("Number of Followups", min_value=0, max_value=10, value=3)

with col2:
    productpitched = st.selectbox("Product Pitched", ["Basic", "Standard", "Deluxe", "Super Deluxe", "King"])
    preferredpropertystar = st.selectbox("Preferred Property Star", [3.0, 4.0, 5.0])
    maritalstatus = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Unmarried"])
    numberoftrips = st.number_input("Number of Trips", min_value=0, max_value=20, value=1)
    passport = st.selectbox("Has Passport?", [0, 1])
    pitchsatisfactionscore = st.number_input("Pitch Satisfaction Score", min_value=1, max_value=5, value=3)
    owncar = st.selectbox("Owns Car?", [0, 1])
    numberofchildrenvisiting = st.number_input("Number of Children Visiting", min_value=0, max_value=5, value=0)
    designation = st.selectbox("Designation", ["Executive", "Manager", "Senior Manager", "AVP", "VP"])
    monthlyincome = st.number_input("Monthly Income", min_value=0, max_value=100000, value=20000)

if st.button("Predict Purchase Probability", type="primary"):
    # Encode categorical variables (same encoding as during training)
    typeofcontact_encoded = 0 if typeofcontact == "Company Invited" else 1
    occupation_encoded = {"Free Lancer": 0, "Large Business": 1, "Salaried": 2, "Small Business": 3}[occupation]
    gender_encoded = 0 if gender == "Female" else 1
    productpitched_encoded = {"Basic": 0, "Deluxe": 1, "King": 2, "Standard": 3, "Super Deluxe": 4}[productpitched]
    maritalstatus_encoded = {"Divorced": 0, "Married": 1, "Single": 2, "Unmarried": 3}[maritalstatus]
    designation_encoded = {"AVP": 0, "Executive": 1, "Manager": 2, "Senior Manager": 3, "VP": 4}[designation]
    
    # Create input dataframe with all features in the correct order
    input_data = pd.DataFrame({
        "Age": [age],
        "TypeofContact": [typeofcontact_encoded],
        "CityTier": [citytier],
        "DurationOfPitch": [durationofpitch],
        "Occupation": [occupation_encoded],
        "Gender": [gender_encoded],
        "NumberOfPersonVisiting": [numberofpersonvisiting],
        "NumberOfFollowups": [numberoffollowups],
        "ProductPitched": [productpitched_encoded],
        "PreferredPropertyStar": [preferredpropertystar],
        "MaritalStatus": [maritalstatus_encoded],
        "NumberOfTrips": [numberoftrips],
        "Passport": [passport],
        "PitchSatisfactionScore": [pitchsatisfactionscore],
        "OwnCar": [owncar],
        "NumberOfChildrenVisiting": [numberofchildrenvisiting],
        "Designation": [designation_encoded],
        "MonthlyIncome": [monthlyincome]
    })
    
    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)
    
    # Display result
    st.success("Prediction Complete!")
    
    if prediction[0] == 1:
        st.markdown("### ✅ **Likely to Purchase**")
        st.write(f"Probability: {prediction_proba[0][1]*100:.2f}%")
    else:
        st.markdown("### ❌ **Unlikely to Purchase**")
        st.write(f"Probability of Purchase: {prediction_proba[0][1]*100:.2f}%")