Python version of a Turing School project, see [https://backend.turing.edu/module1/projects/enigma/] for background information on the project and encryption algorithm.

Setup:

For now, this program is run locally. First, clone the repo, and ```pip install```
 
 navigate to ```src/encrypt_runner.py```
  
 To encrypt message:
  - put your message in to the ```message``` variable
  - if desired, uncomment the ```key``` and/or ```date``` variables and input desired values, if no values are provided, default values will be assigned
      ```date``` must be in ddmmyy format, as a string
      ```key``` must be 5 numeric characters, as a string
  - if using ```key``` and/or ```date``` variables, add them to the arguments on line 7
  - run ```python src/encrypt_runner.rb``` to encrypt message
  
  To decrypt message:
  - put your encrypted string in to the ```cyphertext``` variable
  - put your key from the encryption step in to the ```key``` variable 
  - if using a date other than today, uncomment the ```date variable``` and input desired value, if no value is provided, today's date will be assigned
      ```date``` must be in ddmmyy format, as a string
      ```key``` must be 5 numeric characters, as a string
  - if using ```date``` variable, add it to the arguments on line 7
  - run ```python src/decrypt_runner.rb``` to decrypt message
