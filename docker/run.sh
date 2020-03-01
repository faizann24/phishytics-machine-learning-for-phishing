#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "No url supplied"
    exit
fi

docker run --rm phishytics python3 test_pretrained_model.py --tokenizer_folder pretrained_models --threshold 0.5 --model_dir pretrained_models --website_to_test $1