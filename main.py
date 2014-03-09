#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

class Data(object):
    
    def __init__(self):
        self.foreign = {}
        self.my_words = {}
        
        self.words_no = 0
    
    def load_db(self):
        try:
            db_file = open('it_pl.txt')
        except:
            print 'Cound not find file'
            
        for line in db_file:
            if len(line) > 0:
                self.words_no += 1
                translation = line.split('=')
                foreign_word = translation[0]
                t = translation[1].split(';')
                self.foreign[foreign_word] = t
        
        print str(self.words_no) + ' entries found.'
        
        self.transform()
        
    def transform(self):
        for k, v in self.foreign.items():
            for w in v:
                key = w.replace('\n', '')
                
                self.my_words[key] = []
                self.my_words[key].append(k)
                
    def play(self):
        
        print 'Type QUIT to exit the program'
        
        #while(True):
            
            #ans = raw_input(question + ': ')
            #print ans
                
        

def main():
    print 'Welcome to Python Language Test'
    
    data = Data()
    data.load_db()
    data.play()
    
    #for k, v in data.my_words.items():
    #    print k, v
    
    
    
    
if __name__ == '__main__':
    main()