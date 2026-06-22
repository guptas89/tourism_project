# 🌴 Tourism Package Purchase Prediction - MLOps Project

An end-to-end MLOps project that predicts whether a customer will purchase a tourism package based on their profile and interaction details.

## 📋 Project Overview

This project demonstrates a complete MLOps pipeline including:

- Data preprocessing and feature engineering
- Model training with hyperparameter tuning (XGBoost)
- MLflow experiment tracking
- Model versioning and storage on Hugging Face
- Automated CI/CD pipeline using GitHub Actions
- Streamlit web application deployed on Hugging Face Spaces

## 🏗️ Project Structure

```
tourism_project/
├── .github/
│   └── workflows/
│       └── pipeline.yml          # GitHub Actions CI/CD pipeline
├── data/
│   └── tourism.csv               # Tourism dataset
├── model_building/
│   ├── data_register.py          # Upload dataset to HF Hub
│   ├── prep.py                   # Data preprocessing & feature engineering
│   └── train.py                  # Model training with MLflow tracking
├── deployment/
│   ├── .streamlit/
│   │   └── config.toml           # Streamlit configuration
│   ├── app.py                    # Streamlit web application
│   ├── Dockerfile                # Docker configuration for HF Spaces
│   ├── requirements.txt          # Python dependencies
│   └── README.md                 # HF Space metadata
├── hosting/
│   └── hosting.py                # Deploy app to HF Spaces
└── README.md                     # This file
```

## 🚀 Features

### Data Pipeline

- **Data Registration**: Upload raw dataset to Hugging Face Datasets
- **Preprocessing**: Handle missing values, encode categorical variables, feature scaling
- **Train/Test Split**: Stratified split with 80/20 ratio

### Model Training

- **Algorithm**: XGBoost Classifier
- **Hyperparameter Tuning**: GridSearchCV with 3-fold cross-validation
- **Experiment Tracking**: MLflow for logging parameters, metrics, and models
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC

### MLOps Pipeline (GitHub Actions)

1. **Register Dataset**: Upload tourism.csv to HF Hub
2. **Data Preparation**: Preprocess and create train/test splits
3. **Model Training**: Train with hyperparameter tuning, log to MLflow
4. **Model Deployment**: Upload best model to HF Model Hub
5. **App Deployment**: Deploy Streamlit app to HF Spaces

### Web Application

- **Framework**: Streamlit
- **Features**: Interactive form with 18 input features
- **Prediction**: Real-time classification with probability scores
- **Deployment**: Docker-based deployment on Hugging Face Spaces

## 📊 Dataset Features

The model uses 18 features to predict purchase likelihood:

| Feature                  | Description                    | Type        |
| ------------------------ | ------------------------------ | ----------- |
| Age                      | Customer age                   | Numeric     |
| TypeofContact            | How customer was contacted     | Categorical |
| CityTier                 | City tier (1, 2, 3)            | Categorical |
| DurationOfPitch          | Sales pitch duration (minutes) | Numeric     |
| Occupation               | Customer occupation            | Categorical |
| Gender                   | Customer gender                | Categorical |
| NumberOfPersonVisiting   | Number of persons visiting     | Numeric     |
| NumberOfFollowups        | Number of followups            | Numeric     |
| ProductPitched           | Tourism package type           | Categorical |
| PreferredPropertyStar    | Preferred hotel star rating    | Numeric     |
| MaritalStatus            | Marital status                 | Categorical |
| NumberOfTrips            | Past trips count               | Numeric     |
| Passport                 | Has passport (0/1)             | Binary      |
| PitchSatisfactionScore   | Satisfaction score (1-5)       | Numeric     |
| OwnCar                   | Owns car (0/1)                 | Binary      |
| NumberOfChildrenVisiting | Children count                 | Numeric     |
| Designation              | Job designation                | Categorical |
| MonthlyIncome            | Monthly income                 | Numeric     |

## 🔧 Installation & Setup

### Prerequisites

- Python 3.9+
- Git
- Hugging Face account with access token

### Local Setup

1. **Clone the repository**

```bash
git clone https://github.com/guptas89/tourism_project.git
cd tourism_project
```

2. **Install dependencies**

```bash
pip install -r deployment/requirements.txt
```

3. **Set environment variables**

```bash
export HF_TOKEN="your_huggingface_token"
```

4. **Run the pipeline locally**

```bash
# Register dataset
python model_building/data_register.py

# Preprocess data
python model_building/prep.py

# Train model
python model_building/train.py

# Deploy to HF Spaces
python hosting/hosting.py
```

## 🌐 Deployment

### GitHub Actions CI/CD

The project uses GitHub Actions for automated deployment:

1. **Trigger**: Push to `main` branch
2. **Jobs**:
   - `register-dataset`: Upload data to HF Hub
   - `data-prep`: Preprocess and split data
   - `model-training`: Train model with MLflow
   - `deploy-hosting`: Deploy app to HF Spaces

### Required Secrets

Add to GitHub repository secrets:

- `HF_TOKEN`: Your Hugging Face access token

## 📈 Model Performance

The XGBoost model is optimized using GridSearchCV with the following hyperparameters:

- `n_estimators`: [100, 200, 300]
- `max_depth`: [3, 5, 7]
- `learning_rate`: [0.01, 0.05, 0.1]
- `subsample`: [0.7, 0.8, 1.0]
- `colsample_bytree`: [0.7, 0.8, 1.0]
- `scale_pos_weight`: [1, 2, 3]

Evaluation metrics are logged to MLflow for experiment tracking.

## 🔗 Links

- **GitHub Repository**: https://github.com/guptas89/tourism_project
- **Hugging Face Space**: https://huggingface.co/spaces/guptas89/tourism-package-app
- **Model Hub**: https://huggingface.co/guptas89/tourism-prediction-model
- **Dataset Hub**: https://huggingface.co/datasets/guptas89/tourism-dataset

## 🛠️ Technologies Used

- **ML Framework**: Scikit-learn, XGBoost
- **Experiment Tracking**: MLflow
- **Web Framework**: Streamlit
- **Model Registry**: Hugging Face Hub
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Cloud Deployment**: Hugging Face Spaces

## 📝 Usage

### Web Application

1. Visit the deployed app: https://huggingface.co/spaces/guptas89/tourism-package-app
2. Fill in customer details (18 features)
3. Click "Predict Purchase Probability"
4. View prediction result with confidence score

### API Usage (Python)

```python
from huggingface_hub import hf_hub_download
import joblib
import pandas as pd

# Download model
model_path = hf_hub_download(
    repo_id="guptas89/tourism-prediction-model",
    filename="best_tourism_model_v1.joblib"
)

# Load model
model = joblib.load(model_path)

# Prepare input (example)
input_data = pd.DataFrame({
    "Age": [35],
    "TypeofContact": [1],  # Encoded
    "CityTier": [1],
    # ... (all 18 features)
})

# Predict
prediction = model.predict(input_data)
probability = model.predict_proba(input_data)
```

## 🤝 Contributing

This is a learning project for MLOps practice. Feel free to fork and experiment!

## 📄 License

This project is for educational purposes.

## 👨‍💻 Author

**Siddharth Gupta**

- GitHub: [@guptas89](https://github.com/guptas89)
- Email: siddharthgupta2010@gmail.com
