from simpletransformers.t5 import T5Model
import re
from .config import QG_MODEL, ANS_MODEL, MCQ_MODEL, QA_QG_MODEL, QG_MODEL_ARGS, ANS_MODEL_ARGS, MCQ_MODEL_ARGS, QA_QG_MODEL_ARGS
"""
# Commenting for better reach

class QG_QA_MODEL:
  def __init__(self):
    super()
    print("✨ Initializing qg model from:", QG_MODEL)
    self.ques_model = T5Model("t5", QG_MODEL, use_cuda=False, args=QG_MODEL_ARGS, silent=True)
    self.ans_model = T5Model("t5", ANS_MODEL , use_cuda=False, args=ANS_MODEL_ARGS, silent=True)

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
"""
class QAQG_MODEL:
  def __init__(self):
    super()
    print("✨ Initializing qg model from:", QA_QG_MODEL)
    self.model = T5Model("t5", QA_QG_MODEL, use_cuda=False, args = QA_QG_MODEL_ARGS, silent=True)

  def train(self):
    pass
  
  def evaluate(self):
    pass
  
  def prep_input_for_qg(self,input):
    input = " ".join(input.split())
    max_sentences = 5 #max no of sentences for context
    sentence_split = input.split("(?<=[a-z])\\.\\s+")
    n = len(sentence_split)
    return ["".join(sentence_split[i:i+max_sentences]) for i in range(0,n,max_sentences)]

  def generate_questions(self, context):
    print("Preparing input for qg..")
    questions = self.prep_input_for_qg
    print("Generating qa-qg for input...")
    preds = self.model.predict(
        [("qa_gen: " + question) for question in self.prep_input_for_qg(context)]
    )
    output = []
    print("Completed qa-qg...")
    for pred in preds:
      for qa in pred:
        ques, ans = self.preprocess_output(qa)
        output.append([ques,ans])
        print(ques, "\n" + ans, end='\n\n')
    return output

  def preprocess_output(self, output):
    ques = re.findall("(?<=question>)(.*?)(?=/question>)", output)
    ans = re.findall("(?<=answer>)(.*?)(?=/answer>)", output)
    ques = ques[0] if len(ques)>0 else ""
    ans = ans[0] if len(ans)>0 else ""
    return ques,ans

class MCQ_QG_MODEL:
  def __init__(self):
    super()
    print("✨ Initializing mcq model from:", MCQ_MODEL)
    self.mcq_model = T5Model("t5", MCQ_MODEL, use_cuda=False, args=MCQ_MODEL_ARGS, silent=True)
  
  def generate(self, input):
    preds = self.mcq_model.predict(["generate_mcqtype_answer: " + input])
    result = []
    for pred in preds:
      for output in pred:
        x = []
        question = output.split("/ques>")[0] + "?"
        answer = output.split("/ques>")[1:]
        print(question)
        x.append(question)
        options = []
        for idx, option in enumerate(("".join(answer)).split(",")):
          status = option[-2:]
          option = option[:-2]
          options.append(option)
          if (status == "_A"):
            x.append(idx)
            print("✅ "+option)
          else:
            print("⭕ "+option)
        x.append(options)
        print("\n")
        result.append(x)
    return result


