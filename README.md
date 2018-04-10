# contact_book
Rest APIs for contact_book app

## Setup Steps:

1. Install python2.7 using command 
 ```
  $sudo apt-get python
  ```
2. Create a virtual environment 
  ```
  $virtualenv ENV
  ```
3. Now clone the repository 
  ```
  $git clone https://github.com/visheshbhalla/contact_book.git
  ```
  
  Your directory Structure should look like this
  ```
  $PATH-----ENV
        |
        |---contact_book-----contact_book
                          |
                          |--development.ini
                          |
                          |--setup.py
  ```                      
4. Goto outer contact_book directory
  ```
  $cd contact_book
  ```
5. Run setup.py with install and develop
  ```
  $../ENV/bin/python setup.py install
  $../ENV/bin/python setup.py develop
  ```
6. Run the application using below command
  ```
  $../ENV/bin/pserve development.ini
  ```
7.You are Good to Go!!!!!

## CRUD APIs:
```
/contacts?contact_name=$contact_name - GET list
/contacts/$email - GET
/contacts - POST
/contacts/$email - PUT
/contacts/$email - DELETE
```
## Unit/Functional Testing command:
```
$ ../ENV/bin/py.test contact_book/test.py
```

