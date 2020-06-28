# employee salary predictor application



## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Directory Tree](#directory-tree)
  * [Installation](#installation)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Contribution](#contribution)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [Credits](#credits)


## Demo
Link: [https://spam-detector-ml-app.herokuapp.com/](https://spam-detector-ml-app.herokuapp.com/)

[![](https://i.imgur.com/z3LLN7V.png)](https://spam-detector-ml-app.herokuapp.com/)



## Overview
This is a simple spam detection application developed using sklearn. The trained model (`model/model.h5`) takes string of message as an input and predicts the class of message as spam or not spam. It's a multiclass problem. Dataset has been taken from [Kaggle](https://www.kaggle.com/uciml/sms-spam-collection-dataset)



## Directory Tree 
```
├── model
|    ├── nlp_model.pkl
|    ├── transform.pkl
├── static
|    ├── style.css
├── templates
|    ├── home.html
|    ├── result.html
├── LICENSE
├── Procfile
├── README.md
├── activation.bat
├── app.py
├── requirements.txt

```

## Installation
1. Windows user can double click on activation.bat file to install required package
2. Linux User type following command in commnand line
```bash
pip install -r requirements.txt
```

## Run
1. After successfull installation windows user can directly open this link : https://127.0.0.1:5000
2. After successful installation open type
```bash
python app.py
 ```
and then open link : https://127.0.0.1:5000

## To Do
1. More Interactive and stylish
2. Multi - text prediction at same time
3. Upload csv and make prediction on csv and download that file



## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/pandeynandancse/spam_detection_app/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/pandeynandancse/spam_detection_app/issues/new). Please include sample queries and their corresponding results.


## Contribution
If you'd like to do some contribution, feel free to do so by opening a pull request [here](https://github.com/pandeynandancse/spam_detection_app/pulls). Please include sample queries and their corresponding results.




## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://blogeduonix-2f3a.kxcdn.com/wp-content/uploads/2018/12/Linear-Discriminant-Analysis.jpg" width=200>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 




## Team
[![Nandan Pandey](https://qph.fs.quoracdn.net/main-thumb-189737418-200-jmwzsixdznlgemnejuecomukeluqkgzd.jpeg)](https://pandeynandancse.github.io) |
-|
[Nandan Pandey](https://pandeynandancse.github.io) |)



## Credits
Data has been taken from [Kaggle](https://www.kaggle.com/uciml/sms-spam-collection-dataset).
Thanks to kaggle for this awesome data.
