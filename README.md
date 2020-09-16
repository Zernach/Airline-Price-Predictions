# Airline Price Predictions

Select your origin city, your destination city, with which airline company you are flying, and how many tickets you are purchasing — and my model will predict the round-trip cost — based on 9 million 2018 Domestic Flight Prices in the United States. Try it yourself: I deployed [this web app using Heroku](https://airline-price-predictions.herokuapp.com/).

![GIF Image](https://ryan.zernach.com/wp-content/uploads/Airline_Price_Predictor_made_with_giphy.gif)

* View my [Modeling Process & Statistical Analysis](https://ryan.zernach.com/portfolio/airline-price-predictor-how-are-flight-prices-calculated/)
* Here's my [.ipynb notebook file](https://colab.research.google.com/drive/1s3SJs2dpnH2LQvR9S3JNH2C-yD1na_4R?usp=sharing), where I gathered, cleaned, analyzed, modeled my prediction algorithm.
* After cleaning the data, I [uploaded the dataset](https://www.kaggle.com/zernach/2018-airplane-flights) to Kaggle for others to use, which has since been downloaded 500+ times by others in the Kaggle community!


# How to Locally Run this Repo
1. Download repo to local machine and CD to directory
2. Run `pipenv shell` in terminal to activate the pipenv environment from the pipfile
3. Run `python run.py` to launch the app and host it on a local server on your machine


# Dependencies
There's a whole list of Python libraries that are used in code. However, because I included a dependency management file (pipfile) for this project, the only two libraries that you should have to install are `pip` and `pipenv`. The first time you run `pipenv shell`, your computer will recognize that, in the repo, there is a pipfile that contains a list of libraries needed to run this web app, and will automatically install those libraries in a newly created virtual environment. Then each time you run it in the future, you're simply "activating" this virtual environment. It's convenient for everyone.

# Files in This Repo
File/Directory | Description
--- | ---
`Assets` | `Directory` — Includes the .joblib file, which is the trained and compressed machine learning algorithm that's used to generate pricing predictions — and all of the individual images that are displayed in the web app.
`Pages` | `Directory` — Contains files with the code that's rendered when the user visits different pages on the web app: front page (index.py), live predictions (predictions.py), and modeling process (process.py).
`Pipfile` & `Pipfile.lock` | See above section, "Dependencies," for more information.
`Procfile` | Declares the web app's server. [Gunicorn](https://gunicorn.org/) is a pure-Python HTTP server for WSGI applications. It allows you to run any Python application concurrently by running multiple Python processes within a single dyno. It provides a perfect balance of performance, flexibility, and configuration simplicity when deploying a web app to somewhere [Heroku](https://devcenter.heroku.com/articles/procfile).
`app.py` | Downloads an external stylesheet (.css) theme for quickly launching an interactive web app.
`run.py` | This is main, executable HTML server file, except I wrote it in Python using [Dash](https://dash.plotly.com/introduction).


# Questions?
I can be reached via email: [Ryan@Zernach.com](mailto:Ryan@Zernach.com)