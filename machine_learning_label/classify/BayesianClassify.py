import os
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import jieba

path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../resources'))


class BayesianClassify:
    def __init__(self, key_word_path, dialogue_text_path, label_path):
        """
        :param key_word_path: 关键字文本集合路径
        :param dialogue_text_path:训练数据对话文本集路径
        :param label_path:训练数据标签集合路径

        """
        self.key_word_path = os.path.join(path, key_word_path)
        self.dialogue_text_path = os.path.join(path, dialogue_text_path)
        self.label_path = os.path.join(path, label_path)
        self.initial_words = []
        self.vec = CountVectorizer(token_pattern=r'(?u)\b\w+\b')
        self.clf = MultinomialNB()
        jieba.load_userdict(self.key_word_path)

        self.get_initial_word()
        self.initial_vector_space()
        self.train()

    def get_initial_word(self):
        with open(self.key_word_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                self.initial_words.append(line.strip())

    def initial_vector_space(self):
        self.vec.fit_transform(self.initial_words)
        # print(self.vec.get_feature_names())

    def train(self):
        """
        训练数据
        :return:
        """
        contents = []
        filenames = os.listdir(self.dialogue_text_path)
        for filename in filenames:
            filepath = os.path.join(self.dialogue_text_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                content = content.replace('A: ', '').replace('B: ', '').replace('\n', '')
                content = list(jieba.cut(content))
                contents.append(' '.join(content))
        contents = self.vec.transform(contents)
        # print(self.vec.get_feature_names())
        # print(self.vec.vocabulary_)
        labels = []
        with open(self.label_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                labels.append(line.strip())
        self.clf = self.clf.fit(contents, labels)

    def predict(self, text):
        content = self.vec.transform([text])
        label = self.clf.predict(content)[0]
        if label == '无':
            label = ''
        return label

