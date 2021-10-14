from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import os
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import math
from .config import EASY,MEDIUM,EXTENSIVE
class SUMMARY_MODEL:
    def __init__(self):
        self.model_name = 'google/pegasus-xsum'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name).to(self.device)

    def process_paragraphs(self,content, target_length, content_length):
        # convert into sentences
        sentences = sent_tokenize(content)
        sent_count = len(sentences)

        target_para_length = (sent_count/content_length)*target_length
        split_count = math.ceil(sent_count/target_para_length)
        split_string = [" ".join(sentences[i: i+split_count]).strip() for i in range(0, sent_count, split_count)]
        return split_string

    def splitString(self,summaryType=0, content=""):
        """
            summaryType ->  0: easy, 1: medium, 2: extensive
            content -> whole string content
        """
        
        # split into paragraphs
        # TODO use standardized package
        paragraphs = content.split('\n\n')
        
        sentences = sent_tokenize(content)
        n = len(sentences)
        split_percent = EASY if summaryType == 0 else MEDIUM if summaryType == 1 else EXTENSIVE
        target_length = int(split_percent*n) #6 
        l = []
        i=0
        for para in paragraphs:
            i+=1
            x= self.process_paragraphs(para, target_length, n)
            l.append(x)
        return l
    
    def summarize(self, src_text):
        batch = self.tokenizer(src_text, truncation=True, padding='longest', return_tensors="pt").to(self.device)
        translated = self.model.generate(**batch)
        tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text

    def generate_summary(self,content, extend=1):
        x = self.splitString(extend, content)
        tgt_text = []
        for i in x:
            tgt_text += self.summarize(i)
        return " ".join(tgt_text)
