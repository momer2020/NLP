# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-28 22:22
import tensorflow as tf

from hanlp.components.tokenizers.tok_tf import NgramConvTokenizerTF
from hanlp.datasets.tokenization.ctb6 import CTB6_CWS_TRAIN, CTB6_CWS_DEV, CTB6_CWS_TEST
from hanlp.pretrained.word2vec import CONVSEG_W2V_NEWS_TENSITE_CHAR
from tests import cdroot

cdroot()
tokenizer = NgramConvTokenizerTF()
save_dir = 'data/model/cws/ctb6_cws'
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001,
                                     epsilon=1e-8, clipnorm=5)
tokenizer.fit(CTB6_CWS_TRAIN,
              CTB6_CWS_DEV,
              save_dir,
              word_embed={'class_name': 'HanLP>Word2VecEmbedding',
                          'config': {
                              'trainable': True,
                              'filepath': CONVSEG_W2V_NEWS_TENSITE_CHAR,
                              'expand_vocab': False,
                              'lowercase': False,
                          }},
              optimizer=optimizer,
              window_size=0,
              weight_norm=True)
tokenizer.evaluate(CTB6_CWS_TEST, save_dir=save_dir, output=False)
print(tokenizer.predict(['中央民族乐团离开北京前往维也纳', '商品和服务']))
print(f'Model saved in {save_dir}')
