# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-12-15 22:26
import hanlp
from hanlp.components.mtl.multi_task_learning import MultiTaskLearning
from hanlp.components.mtl.tasks.tok.tag_tok import TaggingTokenization

# 加载多任务模型
HanLP: MultiTaskLearning = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
# 获取分词任务（以tok开头的任务都是分词任务，以细分标准为例）
tok: TaggingTokenization = HanLP['tok/fine']

tok.dict_force = tok.dict_combine = None
print(f'不挂词典:\n{HanLP("商品和服务项目")["tok/fine"]}')

tok.dict_force = {'和服', '服务项目'}
print(f'强制模式:\n{HanLP("商品和服务项目")["tok/fine"]}')  # 慎用，详见《自然语言处理入门》第二章

tok.dict_force = {'和服务': ['和', '服务']}
print(f'强制校正:\n{HanLP("正向匹配商品和服务、任何和服务必按上述切分")["tok/fine"]}')

tok.dict_force = None
tok.dict_combine = {'和服', '服务项目'}
print(f'合并模式:\n{HanLP("商品和服务项目")["tok/fine"]}')

# 需要算法基础才能理解，初学者可参考 http://nlp.hankcs.com/book.php
# See also https://hanlp.hankcs.com/docs/api/hanlp/components/tokenizers/transformer.html

# 含有空格、制表符等（Transformer tokenizer去掉的字符）的词语需要用tuple的形式提供
tok.dict_combine = {('iPad', 'Pro'), '2个空格'}
print(f'空格匹配：\n{HanLP("如何评价iPad Pro ？iPad  Pro有2个空格", tasks="tok/fine")["tok/fine"]}')
# 聪明的用户请继续阅读：tuple词典中的字符串其实等价于该字符串的所有可能的切分方式
print(f'词典内容：\n{dict(tok.dict_combine.config["dictionary"]).keys()}')
