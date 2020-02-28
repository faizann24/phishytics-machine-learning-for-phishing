# Phishytics - Machine Learning for Detecting Phishing Websites
Machine Learning and Random Forests with Byte Pair Encoding and TFIDF scores for Phishing Website Detection.

![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)

This repository contains code for the blog post [Phishytics – Machine Learning for Detecting Phishing Websites](https://faizanahmad.tech/blog/2020/02/phishytics-machine-learning-for-phishing-websites-detection/). Using Random Forests on top of Byte Pair Encoding and TFIDF scores, we can obtain a highly accurate model for predicting phishing websites. Pre-trained models are also provided for users and companies to use.

### Files Description
| Path | Description
| :--- | :----------
| phishytics-machine-learning-for-phishing | Main folder.
| &boxur;&nbsp; tokenizer | Folder to store the tokenizer output files.
| &boxur;&nbsp; saved_models | Folder to save trained models.
| &boxur;&nbsp; pretrained_models | Folder containing required model files to run the pre-trained phishing detection model.
| &boxur;&nbsp; labeled_data | Folder containing data for phishing and legitimate websites.
| &ensp;&ensp; &boxvr;&nbsp; phishing_htmls| HTML files of phishing web pages. Please do not change the folder names.
| &ensp;&ensp; &boxvr;&nbsp; legitimate_htmls| HTML files of legitimate web pages. Please do not change the folder names.
| &boxvr;&nbsp; create_data_for_tokenization.py | Create data for tokenization and apply byte pair encodings to get tokens.
| &boxvr;&nbsp; train_phishing_detection_model.py | Train a phishing website detection model.
| &boxvr;&nbsp; test_model.py | Test a website for phishing using our pre-trained random forest model.
| &boxvr;&nbsp; test_pretrained_model.py | Test a fully trained Random Forest model with 99% test accuracy on any given website.

## Usage
### Packages
You will need to install the following package to train and test the models.
- [Scikit-learn](https://scikit-learn.org/)
- [Numpy](https://numpy.org/)
- [Tokenizers](https://github.com/huggingface/tokenizers)
- [Langdetect](https://pypi.org/project/langdetect/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/en/master/)

### Training your own Model
#### 1. Data Tokenization
In order to train a phishing website detection model, you first need to tokenize all the HTML files into tokens using Byte Pair Encoding (BPE). We will use the tokenizer library for this. Once the html files are in their respective folders, run the following command.
```
python3 create_data_for_tokenization.py --labeled_data_folder labeled_data --vocab_size 300 --min_frequency 3
```
The script takes three parameters as inputs:
- labeled_data_folder: Folder containing data for phishing and legitimate websites.
- vocab_size: Maximum number of tokens to have in the vocabulary
- min_frequency: Tokens having frequency lower than this value will be ignored

#### 2. Model Training
Once we have create a Byte Pair Encoding tokenizer, we will be able to use it to tokenize HTML files and extract features for machine learning. On top of BPE tokens, we will apply TFIDF scores to get a feature representation of each HTML file. Run the following command to train your own model.
```
python3 train_phishing_detection_model.py --tokenizer_folder tokenizer/ --labeled_data_folder labeled_data/ --ignore_other_languages 1 --apply_different_thresholds 1 --save_model_dir saved_models
```
The script takes five parameters as inputs:
- tokenizer_folder: Folder containing tokenizer files. The default folder is 'tokenizers'
- labeled_data_folder: Folder containing data for phishing and legitimate websites.
- ignore_other_languages: Whether to ignore languages other than english. Set it to 0 if you want to include all languages.
- apply_different_thresholds: Whether to apply different confidence thresholds during model evaluation.
- save_model_dir: Directory to save to model files

#### 3. Model Testing
Once we have a trained model, we can simply test it live on any website using the following command. 
```
python3 test_model.py --tokenizer_folder tokenizer --threshold 0.5 --model_dir saved_models --website_to_test https://www.google.com
```
The script takes four parameters as inputs:
- tokenizer_folder: Folder containing tokenizer files. The default folder is 'tokenizers'
- threshold: Threshold to use for making final predictions. By default, the value is 0.5.
- model_dir: Directory where saved model files exist.
- website_to_test: Website you want to test. Please add "http://" or "https://" before the website to make everything work. Otherwise, you will face an error.

### Using Pre-trained Model
To use the pre-trained model, please go to the 'pretrained_models' directory and unzip the 'document-frequency-dictionary.zip' file. Do not unzip it in a new directory, keep it in the same directory. Once that is done, you can run the following command to use the pre-trained model.
```
python3 test_pretrained_model.py --tokenizer_folder pretrained_models --threshold 0.5 --model_dir pretrained_models --website_to_test https://www.google.com
```
The script takes four parameters as inputs:
- tokenizer_folder: Folder containing tokenizer files. The default folder is 'tokenizers' but here we will use 'pretrained_models'.
- threshold: Threshold to use for making final predictions. By default, the value is 0.5.
- model_dir: Directory where saved model files exist. The pre-trained model files exist in 'pretrained_models'.
- website_to_test: Website you want to test. Please add "http://" or "https://" before the website to make everything work. Otherwise, you will face an error.

## License
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](LICENSE)

Copyright (c) 2020-present, Faizan Ahmad