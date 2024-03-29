## Product Review Sentiment Analysis - A Simple Flask App
This project provides a comprehensive sentiment analysis framework for product reviews using Flask and pre-trained machine learning models. It allows you to analyze customer feedback across various categories (badminton, tawa, tea) and understand their sentiment.

### What you can do:
* Analyze written reviews and predict their sentiment.
* Help you understand customer feedback and gauge overall satisfaction.
* Provide a foundation for building more advanced sentiment analysis tools.

### Project Structure:
The project follows a structured layout to organize its components and files. Below is an overview of the main directories and files:

- *`Real_Time_Flipkart_Sentiment_Analysis/`*
  - *`data/`*: This folder houses the product review datasets used for model training
    - *`reviews_badminton/`*
  - *`notebooks/`*: This folder contains Jupyter notebooks for data analysis and model development.
    - `Flipkart_Sentiment_Analysis_v3.ipynb`: (used notebook)
  - *`models/`*: This folder stores the trained sentiment analysis models and vectorizers.
    - `model_v2.pkl`: (used model)
    - `vectorizer_v2.pkl`: (used vectorizer)
  - *`src/`*: This folder contains the Flask application code.
    - *`templates/`*
      - `index.html`
      - `result.html`
    - `app.py`
  - `requirements.txt`

### Installation:
* Clone the repository using the command ```git clone https://github.com/vjabhi000985/Real_Time_Flipkart_Sentiment_Analysis.git```
* Install the prerequisites by going to the cloned repository and run the command ```pip install -r requirements.py```
* Data Exploration: Review the Jupyter notebooks in the `notebooks` folder to gain insights into data processing, model training approaches, and model evaluations.
* `Run the App`: Navigate to the project directory in your terminal and execute: ```python src/app.py```

### Potential Enhancements:
* `Model Selection`: Explore the different models (`r_model.pkl`, `model.pkl`, etc.) and vectorizers (`tf_vectorizer.pkl`, `vectorizer.pkl`, etc.) to understand their performance and choose the best option based on the data and task.
* `Custom Model Training`: Consider training a custom model on a larger dataset specific to your domain for improved accuracy.
* `Advanced Techniques`: Integrate advanced techniques like word2vec or BERT for richer text representation and potentially better sentiment analysis.
* `User Interface`: Develop a more comprehensive user interface with features like sentiment visualization, review history, and the ability to analyze reviews across different product categories.

### AWS Deployment Link: `http://3.108.41.228:5000/`
- AWS Instance closed, therefore the above url will not work.
