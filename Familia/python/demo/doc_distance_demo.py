#coding=utf-8

# Copyright (c) 2017, Baidu.com, Inc. All Rights Reserved
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
from familia_wrapper import InferenceEngineWrapper

if sys.version_info < (3,0):
    input = raw_input

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage:python {} {} {}.\n".format(
            sys.argv[0], "model_dir", "conf_file"))
        exit(-1)

    # 获取参数
    model_dir = sys.argv[1]
    conf_file = sys.argv[2]
    # 创建InferenceEngineWrapper对象
    inference_engine_wrapper = InferenceEngineWrapper(model_dir, conf_file)
    while True:
        # 输入两个长文本
        doc1 = input("Enter Document1: ").strip()
        doc2 = input("Enter Document2: ").strip()
        doc1_seg = inference_engine_wrapper.tokenize(doc1)
        doc2_seg = inference_engine_wrapper.tokenize(doc2)
        distances = inference_engine_wrapper.cal_doc_distance(doc1_seg, doc2_seg)
        # 打印结果
        print("Jensen-Shannon Divergence = {}".format(distances[0]))
        print("Hellinger Distance = {}".format(distances[1]))
