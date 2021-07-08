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

- Start the server
> ```bash
> $ uvicorn app:app --reload
> ``` 

- The server will run at port 8000 by default.

- Happy coding 🎉