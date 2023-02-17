#Diabetes Prediction web application


Diabetes
========

Heroku Diabetes is a simple web app that predicts the likelihood of a person having diabetes based on certain features. The app uses a machine learning model that was trained on the [Pima Indians Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database).

Demo
----

A live demo of the app can be found at <https://share.streamlit.io/phycoding/heraku-diabetes/main/stapp.py>.

Getting Started
---------------

### Prerequisites

To run the app locally, you will need to have the following installed on your machine:

-   Python 3
-   pip
-   numpy
-   streamlit

### Installation

1.  Clone the repository

shCopy code

`git clone https://github.com/phycoding/heraku-diabetes.git`

1.  Navigate to the project directory

shCopy code

`cd heraku-diabetes`

1.  Install the dependencies

`pip install -r requirements.txt`

### Usage

1.  Start the app


`python app.py`

1.  Open your web browser and go to <http://localhost:5000/>

2.  Enter the required features and click "Predict" to get the prediction.

Built With
----------

-   [Flask](https://flask.palletsprojects.com/en/2.0.x/) - The web framework used
-   [Streamlit](https://www.streamlit.io/) 
-   [scikit-learn](https://scikit-learn.org/stable/) - The machine learning library used
-   [Bootstrap](https://getbootstrap.com/) - The CSS framework used

License
-------

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/chat/LICENSE) file for details.

Acknowledgments
---------------

-   The Pima Indians Diabetes Dataset is available from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes).
