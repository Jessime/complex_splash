# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:21:52 2016

@author: jessime
"""
import pickle

def parse():
    """Reads question file and saves a dictionary of questions and answers"""
    qa_dict = {}
    with open('questions_raw.txt') as infile:
        for line in infile:
            try:
                no_cat = line.strip().split(':')
                del no_cat[0]
                no_cat = ':'.join(no_cat)
                qa = no_cat.split('*')
                qa_dict[qa[0]] = qa[1]
            except IndexError:
                print no_cat
                break
    pickle.dump(qa_dict, open('questions.txt', 'wb'))
    
if __name__ == '__main__':
    parse()