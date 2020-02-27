# Basic libraries
import os
import io
import sys
import numpy as np
from os import walk
from tokenizers import ByteLevelBPETokenizer

# Parsing arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--labeled_data_folder", type=str, default = "labeled_data", help="Labeled data folder")
parser.add_argument("--vocab_size", type=int, default = 10000, help="Maximum number of tokens to have in the vocabulary")
parser.add_argument("--min_frequency", type=int, default = 5, help="Tokens with frequency less than this parameter will be ignored")

args = parser.parse_args()
labeledDataFolder = args.labeled_data_folder
vocabSize = args.vocab_size
minFrequency = args.min_frequency

"""
How to run:
python3 create_data_for_tokenization.py --labeled_data_folder labeled_data --vocab_size 300 --min_frequency 5
"""

# Get all html files
files = []
for(_,_,f) in walk(labeledDataFolder + "/legitimate_htmls"):
	files.extend([labeledDataFolder + "/legitimate_htmls/" + file for file in f])
for(_,_,f) in walk(labeledDataFolder + "/phishing_htmls"):
	files.extend([labeledDataFolder + "/phishing_htmls/" + file for file in f])
print("Total number of html files: %d\n" % len(files))

# Writing data, one html file per line. This is the format the tokenizer expects
print("Writing html data into a single file...")
output = open("tokenizer/htmlCodePerLine.txt", "w")
count = 0
for file in files:
	count = count + 1
	print("Files processed: %d, Total files: %d" % (count, len(files)))
	fileData = io.open(file, "r", errors="ignore").readlines()
	fileData = ''.join(str(line) for line in fileData)
	fileData = fileData.replace("\n", " ")
	output.write(fileData + "\n")
output.close()

# Starting tokenization
print("\nStarting tokenization with BPE")
tokenizer = ByteLevelBPETokenizer()
tokenizer.train("tokenizer/htmlCodePerLine.txt", min_frequency=minFrequency, vocab_size = vocabSize)
print("Vocabulary size is: %d\nNOTE: Sometimes, the vocab size might not be equal to the input 'vocab_size'\n" % (tokenizer.get_vocab_size()))
tokenizer.save("tokenizer", "tokenizer.tok")
print("Tokenizer files have been saved in 'tokenizer' directory...")