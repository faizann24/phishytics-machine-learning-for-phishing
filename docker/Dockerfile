FROM python
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain=nightly -y
RUN git clone https://github.com/huggingface/tokenizers
RUN git clone https://github.com/faizann24/phishytics-machine-learning-for-phishing.git
RUN unzip phishytics-machine-learning-for-phishing/pretrained_models/document-frequency-dictionary.zip -d phishytics-machine-learning-for-phishing/pretrained_models/
RUN pip3 install setuptools_rust
ENV PATH="/root/.cargo/bin:${PATH}"
RUN rustc --version
RUN cd tokenizers/bindings/python/ ;  python3 setup.py install
RUN pip3 install numpy tokenizers langdetect joblib requests scikit-learn pandas
WORKDIR phishytics-machine-learning-for-phishing/