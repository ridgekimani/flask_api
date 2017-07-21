# Flask API
This is a simple application that consumes a public api using a HTTP Client Library




### Getting Started
  #### Prerequisites
  1. Ensure you have a python interpreter installed, preferably python3.5 or python3.6
  2. Ensure you have git installed
  3. For running tests, it is prefarable to run them using nosetests, install using pip install nose 
  
  ### Setup and Installation
   Open the terminal or command prompt on your machine
  1. Since pip is installed, install a virtual environment using  sudo pip install virtualenv on linux machines, pip install virtualenv  on windows and mac based machines.
  2. Navigate to your working directory.
  3. Create a virtual environment by typing virtualenv [name], for example ~$ virtualenv env
  4. Navigate to your project directory
  5. Clone the project via git, using ~$git clone https://github.com/ridgekimani/flask_api.git or download the zipped file from https://github.com/ridgekimani/flask_api
  6. Change directory to the virtual environment directory
  7. Type ~$ source bin/activate to activate to your virtual environment
  8. Install the packages from the requirements.txt file by typing ~$ pip install -r requirements.txt'
  
  ### Running the app
    On your shell, run with the command (env)~$ python flask_api.py
    
  ### Testing the api
    On your shell, run the command 
    (env)~$curl curl -i http://127.0.0.1:5000/bucketlist/api/v1.0/bucketlists/
    (env)~$curl curl -i http://127.0.0.1:5000/bucketlist/api/v1.0/bucketlists/00000000

    
  ### Running tests
    Run tests using (env)~$  nosetests


