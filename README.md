# CardiAi  

CardiAi is a state-of-the-art machine learning solution for multi-class heart disease prediction. This project combines advanced machine learning algorithms with a user-friendly Flask-based web application, enabling accessible and accurate predictions. The solution has been seamlessly deployed on **Heroku**, making it available to users worldwide.  

---

## Key Features  

- **Heart Disease Prediction**: Predicts heart disease severity on a scale from 0 to 4, providing actionable insights.  
- **Cutting-Edge Machine Learning**: Implements models such as XGBoost, CatBoost, and LightGBM with rigorous cross-validation and hyperparameter tuning for enhanced accuracy.  
- **Scalable Web Deployment**: The solution is deployed on Heroku for global accessibility.  
- **Team Collaboration**: Fully integrated with PHP backend, frontend, and a mobile application to deliver a cohesive user experience.  

---

## Technology Stack  

- **Programming Language**: Python  
- **Machine Learning**: Scikit-learn, XGBoost, CatBoost, LightGBM  
- **Data Handling & Visualization**: Pandas, NumPy, Seaborn, Matplotlib  
- **Web Framework**: Flask  
- **Deployment**: Heroku  
- **Integration**: PHP backend and frontend  

---

## Installation

### Prerequisites
- Python 3.8 or higher  
- Flask 2.0 or higher  
- PHP for backend integration  
- npm (optional for frontend setup)  

### Steps to Set Up

1. Clone the repository:
   ```bash
   git clone https://github.com/CardiAi/Heart-Disease-Model
   ```

2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:
   ```bash
   python app.py
   ```

4. (Optional) Set up the PHP backend and frontend according to the provided documentation ```https://github.com/CardiAi/```

---

## Usage

1. Run the Flask application to access the API.
2. Input patient data (e.g., age, cholesterol levels, blood pressure, etc.) via the interface.
3. Submit the data to get predictions on heart disease levels (0 to 4).
4. Use the results to make informed decisions or integrate with the mobile app for further analysis.

---

## Project Workflow

### Data Pipeline
1. **Data Collection**: Preprocessed patient data.
2. **Feature Engineering**: Handled missing values, performed feature scaling, and selected significant features.
3. **Model Training**: Trained models using XGBoost, CatBoost, and LightGBM with hyperparameter tuning and cross-validation.
4. **Evaluation**: Achieved high performance metrics (e.g., accuracy, F1-score) on the validation set.
5. **Deployment**: Exported the best-performing model and integrated it with a Flask application.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by Kaggle datasets for heart disease prediction.
- Special thanks to the collaborators who made this project a success.
