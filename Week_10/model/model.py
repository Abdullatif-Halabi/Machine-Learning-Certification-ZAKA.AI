import pickle
import logging
import numpy as np
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences


class Translator:
    def __init__(
        self,
        model_path="model\last_model.h5",
        eng_tokenizer_path="model/eng_tokenizer.pkl",
        fr_tokenizer_path="model/fr_tokenizer.pkl",
    ):
        logging.info(f"loading model from : {model_path}")
        self.model = load_model(model_path)
        logging.info("model has been loaded.")

        with open(eng_tokenizer_path, "rb") as f1:
            logging.info(f"loading english tokenizer from : {eng_tokenizer_path}")
            self.eng_tokenizer = pickle.load(f1)

        with open(fr_tokenizer_path, "rb") as f2:
            logging.info(f"loading french tokenizer from : {fr_tokenizer_path}")
            self.fr_tokenizer = pickle.load(f2)

    def translate(self, input):
        words = input.split()
        encoded_sentence = [self.eng_tokenizer.word_index[word] for word in words]
        padded = pad_sequences([encoded_sentence], maxlen=15, padding="post")

        pred = self.model.predict(padded)

        encoded_output = []
        for i in range(len(words)):
            encoded_output.append(np.argmax(pred[0][i]))

        result = [self.fr_tokenizer.index_word[index] for index in encoded_output]
        translation = " ".join(result)

        return translation
