# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-28 23:15
from hanlp.components.taggers.transformers.transformer_tagger_tf import TransformerTaggerTF
from tests import cdroot

cdroot()
tagger = TransformerTaggerTF()
save_dir = 'data/model/pos/ctb9_albert_base'
tagger.fit('data/pos/ctb9/train.tsv',
           'data/pos/ctb9/test.tsv',
           save_dir,
           transformer='uer/albert-base-chinese-cluecorpussmall',
           max_seq_length=130,
           warmup_steps_ratio=0.1,
           epochs=20,
           learning_rate=5e-5)
tagger.load(save_dir)
print(tagger(['我', '的', '希望', '是', '希望', '和平']))
tagger.evaluate('data/pos/ctb9/test.tsv', save_dir=save_dir)
print(f'Model saved in {save_dir}')
