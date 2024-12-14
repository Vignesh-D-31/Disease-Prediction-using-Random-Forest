![landing_page](https://github.com/user-attachments/assets/f107cda9-225a-48b0-ac37-2b320d3497f0)This project is a Flask-based web application designed to predict diseases based on user-selected symptoms. It leverages a pre-trained Random Forest Classifier model to classify potential diseases based on input symptoms. The application incorporates the following key components:

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
