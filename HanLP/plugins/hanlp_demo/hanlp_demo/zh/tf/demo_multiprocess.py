# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-02-15 11:30
import multiprocessing
import hanlp

tokenizer = hanlp.load(hanlp.pretrained.tok.LARGE_ALBERT_BASE)


def worker(job):
    print(job)
    print(tokenizer(job))


if __name__ == '__main__':
    num_proc = 2
    # Important! The python multiprocessing package defaults to just call fork when creating a child process.
    # This cannot work when the child process calls async code (i.e TensorFlow is multithreaded).
    # See https://github.com/tensorflow/tensorflow/issues/8220#issuecomment-302826884
    # See https://sefiks.com/2019/03/20/tips-and-tricks-for-gpu-and-multiprocessing-in-tensorflow/
    multiprocessing.set_start_method('spawn', force=True)  # only spawn works with TensorFlow
    with multiprocessing.Pool(num_proc) as pool:
        pool.map(worker, [f'给{i}号进程的任务' for i in range(num_proc)])
