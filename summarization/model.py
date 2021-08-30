from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
# from .config import S_MODEL


class SUMMARY_MODEL:
    def __init__(self):

        self.model_name = 'google/pegasus-xsum'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(
            self.model_name).to(self.device)

    def train(self):
        pass

    def evaluate(self):
        pass

    def generate_summary(self, context):
        batch = self.tokenizer(context, truncation=True,
                               padding='longest', return_tensors="pt").to(self.device)
        translated = self.model.generate(**batch)
        tgt_text = self.tokenizer.batch_decode(
            translated, skip_special_tokens=True)
        return tgt_text[0]
