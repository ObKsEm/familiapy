#coding=utf-8

# Copyright (c) 2017, Baidu.com, Inc. All Rights Reserved
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys,os

from familiapy.topictable import TopicTable
from familiapy.api import InferenceEngineWrapper
from familiapy.api import TopicalWordEmbeddingsWrapper

if __name__ == '__main__':
    model_dir = os.path.join(os.path.dirname(__file__), 'Familia/model/webpage')
    conf_file = "lda.conf"
    emb_file = "webpage_twe_lda.model"
    # topic_words = os.path.join(os.path.dirname(__file__) ,'Familia/model/topic_words.lda.conf')

    inference_engine_wrapper = InferenceEngineWrapper(model_dir, conf_file, emb_file)
    
    vocpath =  os.path.join(model_dir, "vocab_info.txt") 
    topicpath = os.path.join(model_dir, "news_lda.model") 

#topic = TopicTable(2000, vocpath, topicpath)
    twe_wrapper = TopicalWordEmbeddingsWrapper(model_dir, emb_file)
    while True:
        input_text = input("Enter Document: ")
        # 分词
        seg_list = inference_engine_wrapper.tokenize(input_text.strip())
        # 构建句子结构,5个词为一个句子
        sentences = []
        length = len(seg_list)
#for index in range(0, length, 5):
#sentences.append(seg_list[index: index + 5])
        # 进行推断
#topic_dist = inference_engine_wrapper.slda_infer(sentences)
        topic_dist = inference_engine_wrapper.lda_infer(seg_list)
        # 打印结果
        print("Document Topic Distribution:")
        print(topic_dist)
        """
        topic_words = []
        for t in topic_dist:
            print(topic.topic_words(t[0], 10))
            topic_words.append(list(map(lambda x:x[0], topic.topic_words(t[0], 10))))
            # result_list = twe_wrapper.nearest_words_around_topic(t[0], 10)
            # print_result(result_list)
        topicids = map(lambda x:x[0], topic_dist)
        m = zip(topicids, topic_words)
        d = dict(m)
        print(d)
        r = {}
        for k ,v in d.items():
            print(v)
            for w in v :
                count = input_text.count(w)
                r.update({k: r.get(k,0) + count})
        print(r)
        maximum = max(d, key=d.get) 
        print(maximum)
        """
        for item in topic_dist:
            topic_words = twe_wrapper.nearest_words_around_topic(item[0])
            print (item[0])
            print (topic_words)
