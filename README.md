# Hypertension-Heart-Disease-and-Stroke-Prediction-using-SVM

Kaggle Notebook Link : https://www.kaggle.com/code/bai14mou/hypertension-heart-disease-and-stroke-prediction  <br>
Live Webapp Link : https://baisali14-hypertension-heart-disease-and-stroke-p-webapp-ctk8ss.streamlit.app/     <br>
Stroke Prediction Dataset link : https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset       <br>

Sample values to try with : 19723  35.0  82.99  30.6    <br>
Resultant output with these values : No hypertension, No heart disease, No stroke

# Introduction
This Machine Learning project is aimed at predicting three different factors all at the same time depending on different Diagnostic aspects. The factors are as follows:<br>
    (a) A person has hypertension or not. <br>
    (b) A person has heart disease or not. <br>
    (c) A person has stroke or not. <br>
<br>
The dataset being used to make the predictive model is the Stroke Prediction Dataset. The different attributes of the dataset include - id, gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level bmi, smoking_status, stroke.

# Technologies Used
This Machine Learning project was implemented using Python Programming Language. The different libraries being used are: <br>
* Scikit-learn 
* Numpy
* Pandas
* Seaborn
* Pickle
        
# Data Collection and Analysis
The dataset used in this project is the Stroke Prediction Dataset. The dataset has 12 attributes. They are: <br>
1) id: unique identifier <br>
2) gender: "Male", "Female" or "Other" <br>
3) age: age of the patient <br>
4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension <br>
5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease <br>
6) ever_married: "No" or "Yes" <br>
7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed" <br>
8) Residence_type: "Rural" or "Urban" <br>
9) avg_glucose_level: average glucose level in blood <br>
10) bmi: body mass index <br>
11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown" <br>
12) stroke: 1 if the patient had a stroke or 0 if not <br>

The dataset is further understood and analysed using different satistical measures. The data is even visualised using seaborn library. This library represents the data in bar graphs and hence, we recieve a visual representation of the data.

# Data Preprocessing
The data is checked for null values. The dataset had some null values. These null values were replaced with the mean value of the particular attribute.
<br>
The dataset is then split into input features (X) and target variables (Y_hypertension, Y_heartdisease, Y_stroke). The input features are standardized using Standarad Scaler.

# Machine Learning Model
Support Vector Machine (SVM) is used to build our machine learning model. SVM is a supervised learning algorithm that can be used for both classification and regression tasks. SVM works by finding the best hyperplane that separates the data into different classes. <br>

The preprocessed dataset is further split into training and testing sets. The trained set is used to train the SVM model and the model's performance is evaluated on the testing set using accuracy as the evaluation metric.

# Results
After training the SVM model on the preprocessed dataset, an accuracy of 90% is achieved on the testing set for hypertension prediction, an accuracy of 94% is achieved on the testing set for heart disease prediction and  an accuracy of 95% is achieved on the testing set for stroke prediction. 

# Conclusion
In this project, we used SVM to predict whether a person has hypertension, heart disease and stroke depending on certain diagnostic aspects. We achieved an accuracy of 90% on the testing set for  hypertension prediction, an accuracy of 94% on the testing set for heart disease prediction and  an accuracy of 95% on the testing set for stroke prediction. The zzut there is still room for improvement. We can use other machine learning algorithms like Decision Tree, Logistic Regression and many more to improve the accuracy of the model.
