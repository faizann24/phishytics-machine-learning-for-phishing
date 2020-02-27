# Phishytics - Machine Learning for Detecting Phishing Websites
Machine Learning and Random Forests with Byte Pair Encoding and TFIDF scores for Phishing Website Detection.

![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)

This repository contains code for the blog post [Phishytics – Machine Learning for Detecting Phishing Websites](https://faizanahmad.tech/blog/2020/02/phishytics-machine-learning-for-phishing-websites-detection/). Using Random Forests on top of Byte Pair Encoding and TFIDF scores, we can obtain a highly accurate model for predicting phishing websites. Pre-trained models are also provided for users and companies to use.

### Files Description
| Path | Description
| :--- | :----------
| phishytics-machine-learning-for-phishing | Main folder.
| &boxur;&nbsp; sample_data | Folder containing data for phishing and legitimate websites.
| &ensp;&ensp; &boxvr;&nbsp; phishing_htmls| HTML files of phishing web pages. 
| &ensp;&ensp; &boxvr;&nbsp; legitimate_htmls| HTML files of legitimate web pages. 
| &boxvr;&nbsp; phishing_detection.py | Train a phishing website detection model.
| &boxvr;&nbsp; test_website.py | Test a website for phishing using our pre-trained random forest model.

## Usage
### Packages
You will need to install the following package to train and test the models.
- [Scikit-learn](https://scikit-learn.org/)
- [Numpy](https://numpy.org/)
- [Tokenizers](https://github.com/huggingface/tokenizers)
- [Langdetect](https://pypi.org/project/langdetect/)
