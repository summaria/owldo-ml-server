QG_MODEL = "summaria/qa-qg-t5"
ANS_MODEL = "summaria/qa-t5"
MCQ_MODEL = "D:\\programs\\projects\\side\\summaria\\ml-server\\models\\t5-race-qa-2\\"
QA_QG_MODEL = "D:\\programs\\projects\\side\\summaria\\ml-server\\models\\t5-large-best-model\\"

QG_MODEL_ARGS = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 128,
        "eval_batch_size": 128,
        "num_train_epochs": 1,
        "save_eval_checkpoints": False,
        "use_multiprocessing": False,
        "num_beams": None,
        "do_sample": True,      
        "max_length": 50,
        "top_k": 50,
        "top_p": 0.95,
        "num_return_sequences": 3,
        "fp16":False,
        "silent":True
}

ANS_MODEL_ARGS = {
        "reprocess_input_data": True,
        "overwrite_output_dir": True,
        "max_seq_length": 128,
        "eval_batch_size": 128,
        "num_train_epochs": 1,
        "save_eval_checkpoints": False,
        "use_multiprocessing": False,
        "num_beams": None,
        "do_sample": True,
        "max_length": 50,
        "top_k": 50,
        "top_p": 0.75,
        "num_return_sequences": 1,
        "fp16":False,
        "silent":True
}

MCQ_MODEL_ARGS = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "max_seq_length": 128,
    "eval_batch_size": 128,
    "num_train_epochs": 1,
    "save_eval_checkpoints": False,
    "use_multiprocessing": False,
    "num_beams": None,
    "do_sample": True,
    "max_length": 50,
    "top_k": 50,
    "top_p": 0.95,
    "num_return_sequences": 3,
    "fp16":False,
    "silent":True
}

QA_QG_MODEL_ARGS = {
	"reprocess_input_data": True,
	"overwrite_output_dir": True,
	"max_seq_length": 128,
	"eval_batch_size": 128,
	"num_train_epochs": 1,
	"save_eval_checkpoints": False,
	"use_multiprocessing": False,
	"num_beams": None,
	"do_sample": True,
	"max_length": 50,
	"top_k": 50,
	"top_p": 0.95,
	"num_return_sequences": 3,
	"silent": True
}