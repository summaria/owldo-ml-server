from simpletransformers.t5 import T5Model
from .config import QG_MODEL, ANS_MODEL, QG_MODEL_ARGS, ANS_MODEL_ARGS

class QG_QA_MODEL:
  def __init__(self):
    super()
    self.ques_model = T5Model("t5", QG_MODEL, use_cuda=False, args=QG_MODEL_ARGS)
    self.ans_model = T5Model("t5", ANS_MODEL , use_cuda=False, args=ANS_MODEL_ARGS)
  
  def train(self):
    pass
  
  def evaluate(self):
    pass
  
  def prep_output_for_qa(self, question, context):
    return  "<question>"+question+"</question>"+"<context>"+context+"</context>"
  
  def prep_input_for_qg(self,input):
    # TODO: Context/topic based context division
    sentence_split = input.split(".\n") #nltk.sent_tokenize(input)
    return sentence_split #[("".join(sentence_split[i:i+max_sentences])) for i in range(0,n,max_sentences)]
  
  def generate_answers(self, questions, context ):
    preds = self.ans_model.predict(
        [(("answer_question : " + self.prep_output_for_qa(question,context) )) for question in questions]
    )
    print(preds)
    return preds
  
  def generate_questions(self, context):
    modified_context = self.prep_input_for_qg(context)
    preds = self.ques_model.predict(
        [("ask_question: " + question) for question in modified_context]
    )
    return preds, modified_context
  
  def displayoutput(self, output):
    for ques,ans in output:
      print("\nQuestion: ", ques, "\nAnswer: ",ans,"\n")

  def generate_question_and_answer(self, context):
    questions, modified_context = self.generate_questions(context)
    output = []
    for i in range(len(questions)):
        answers = self.generate_answers(questions[i], modified_context[i])
        for j in range(len(answers)):
          output.append([questions[i][j], answers[j]])
    
    self.displayoutput(output)
    return output