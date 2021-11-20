# English_to_French_Translator

This project uses English and french text data to train

Train X: English
Target y: French

Since words in English and French are split by space that they have same format in language, I decided to use these two languages to make a translator.

The RNN with Embedding model performs **92%** accuracy.

(This project can use in Spanish Language too!)

(I tried to use it on chinese Language bu using tokenized package jieba but it performs not good. It may depend on the dataset and the language structure of chinese.)

All languages data can be found from [here](https://github.com/xiaolancara/English_to_French_Translator/tree/main/data)

# Model Prediction & Performance

![prediction](https://github.com/xiaolancara/English_to_French_Translator/blob/main/results/predicted%20translation%20to%20french.JPG)
![Performance](https://github.com/xiaolancara/English_to_French_Translator/blob/main/results/model%20performance.JPG)
