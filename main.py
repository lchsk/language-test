#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
import getopt

class Data(object):
    
    def __init__(self):
        self.foreign = {}
        self.my_words = {}
        
        self.words_no = 0
        
        # 1 - simple mode : translation from foreign language to native
        # 2 - simple mode : translation from native language to foreign
        self._playing_mode = -1
        
        # current dictionary for chosen playing mode
        self._current_set = {}
    
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
                self.foreign[foreign_word] = [x.replace('\n', '') for x in t ]
        
        print str(self.words_no) + ' entries found.'
        
        self.transform()
        
    def transform(self):
        for k, v in self.foreign.items():
            for w in v:
                key = w.replace('\n', '')
                
                self.my_words[key] = []
                self.my_words[key].append(k)
                
    def start_game(self):
        try:                                
            opts, args = getopt.getopt(sys.argv[1:], "h12", ['help', 'foreign', 'native']) 
            
            #print opts, sys.argv
            
            for opt, arg in opts:                
                if opt in ("-h", "--help"):      
                    print 'help'                  
                elif opt in ('-1', '--foreign'):
                    self._playing_mode = 1
                    self._current_set = self.foreign
                elif opt in ('-2', '--native'):
                    self._playing_mode = 2
                    self._current_set = self.my_words
                else:
                    print 'unhandled option'               
            
        except getopt.GetoptError:                                    
            print 'heeeeelp'
                
    def play(self):
        
        print 'Type QUIT to exit the program'
        
        answer = ''
        
        while(answer != 'QUIT'):
            
            question = random.choice(self._current_set.keys())
            correct = self._current_set[question]
            
            
            answer = raw_input(question + ': ')
            if answer in correct:
                print '\tCORRECT!'
            else:
                answers = ''
                for ind, ans in enumerate(correct):
                    answers += ans
                    if ind < len(correct) - 1:
                        answers += ', '
                print '\tWRONG!\tCorrect: ' + answers
                
        print 'Learn more later'
        

def main():
    print 'Welcome to Python Language Test'
    
    data = Data()
    data.load_db()
    data.start_game()
    data.play()
    
    #for k, v in data.my_words.items():
    #    print k, v
    
    
    
    
if __name__ == '__main__':
    main()