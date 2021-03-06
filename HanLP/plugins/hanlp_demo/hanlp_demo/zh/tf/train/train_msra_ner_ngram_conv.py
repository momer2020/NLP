# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-28 23:15
from hanlp.components.ner.ner_tf import NgramConvNamedEntityRecognizerTF
from hanlp.datasets.ner.msra import MSRA_NER_CHAR_LEVEL_TRAIN, MSRA_NER_CHAR_LEVEL_DEV, MSRA_NER_CHAR_LEVEL_TEST
from hanlp.pretrained.word2vec import CONVSEG_W2V_NEWS_TENSITE_CHAR, \
    CONVSEG_W2V_NEWS_TENSITE_WORD_MSR
from tests import cdroot

cdroot()
recognizer = NgramConvNamedEntityRecognizerTF()
save_dir = 'data/model/ner/msra_ner_ngram_conv'
recognizer.fit(MSRA_NER_CHAR_LEVEL_TRAIN, MSRA_NER_CHAR_LEVEL_DEV, save_dir,
               word_embed={'class_name': 'HanLP>Word2VecEmbedding',
                           'config': {
                               'trainable': True,
                               'filepath': CONVSEG_W2V_NEWS_TENSITE_CHAR,
                               'expand_vocab': False,
                               'lowercase': False,
                           }},
               ngram_embed={'class_name': 'HanLP>Word2VecEmbedding',
                            'config': {
                                'trainable': True,
                                'filepath': CONVSEG_W2V_NEWS_TENSITE_WORD_MSR,
                                'expand_vocab': True,
                                'lowercase': False,
                            }},
               weight_norm=True)
recognizer.evaluate(MSRA_NER_CHAR_LEVEL_TEST, save_dir)
