# owldo-ml-server

This is the ml server for owldo, using FastAPI. This server takes care of routing and calling the different ml models required for the successful running of the application.

## Local development

### Dependencies

- Install [git](https://git-scm.com/downloads)
- Install [python 3.7+](https://www.python.org/downloads/)

## Setting up

- Setup and activate the environment.

  > ```bash
  > $ virtualenv env
  > $ source env/Scripts/activate
  > ```

- Install the dependencies

  > ```bash
  > $ pip install -r requirements.txt
  > ```

- Save a local copy of the trained models in `models/` from:

  - [question-generation-model](https://drive.google.com/drive/folders/164KCJS-omIMyDNEt5_dNR_G8Ic0IqzaE?usp=sharing) (t5-large-best-model)
  - [mcq-generation-model](https://drive.google.com/drive/folders/1-q6yJP7sWuCSL1-TTV5teIEbGkWrgg7d?usp=sharing) (t5-race-qa-2)

  Your folder structure should now look like:

  ```
  .
  ├── models
  │   └── t5-large-best-model
  │   └── t5-race-qa-2

  ```

- Start the server

  > ```bash
  > $ uvicorn app:app --reload
  > ```

- The server will run at port 8000 by default.

- Happy coding 🎉
