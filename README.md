This project is a Flask-based web application designed to predict diseases based on user-selected symptoms. It leverages a pre-trained Random Forest Classifier model to classify potential diseases based on input symptoms. The application incorporates the following key components:

Backend (Flask Application):
Loads a trained machine learning model (model.joblib) and an encoder (encoder.pkl) to map disease predictions.
Reads the training dataset (Training.csv) and feature matrix (X.csv) to create a symptom-to-index mapping.
Defines a prediction function (predictDisease) that processes user-selected symptoms, encodes them into a binary feature vector, and predicts the disease using the trained model.


Frontend (HTML + CSS):
Presents users with an intuitive form to select up to three symptoms from dropdown menus.
Displays the predicted disease on submission.
Utilizes a clean and responsive design with Water.css for styling and custom styles defined in a static CSS file.

Interactive Workflow:
Users select symptoms from dropdown menus, which are dynamically populated with possible options.
After submitting, the application processes the selected symptoms and returns the predicted disease in real-time.

Key Features:
Symptom-to-index mapping ensures accurate feature encoding for the prediction model.
Includes user-friendly elements like form validation and dynamic option selection persistence.
Styled with an engaging and profes!

This application is ideal for educational purposes or as a starting point for more complex healthcare-related projects.

Sample Outputs:
![landing_page](https://github.com/user-attachments/assets/87690289-23bf-41b9-a681-fd1b3c87de22)
![symptoms_selc1](https://github.com/user-attachments/assets/6ad4791b-3ef1-428e-a34c-79618dc1d3f0)
![symptoms_selc2](https://github.com/user-attachments/assets/268c0eab-98e9-4acb-8a25-992e7d12e91e)
![sample_pred1](https://github.com/user-attachments/assets/5dc9b417-13c7-4d8c-a342-861885f7427a)
![sample_pred2](https://github.com/user-attachments/assets/4dfeba2d-e4dd-43b1-9357-2d690ed24678)
![sample_pred3](https://github.com/user-attachments/assets/b01574ca-e138-490c-b45c-0da2abca416b)


