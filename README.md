### Vicinity
### Description
##### A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts. 
### Author
Alex Muliande


### Screenshot
<img src="https://github.com/alex-muliande/Vicinity/blob/master/Screenshot%20from%202019-10-25%2016-39-15.png" width="1000">

### Requirements
##### These are the requirements you need to get the project running locally on your machine:
  - Text Editor
  - Install python3
  - Install and activate virtual
  - Setup Database
  - Install Django

### Installation Process
##### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.6```.
  - ```python --version``` to confirm that python has been installed.
##### Open the command-line and run the following command to open a directory:
  - ```cd your preferred directory``` => ```cd Desktop```
##### Git clone the project on your current directory by:
  - ```git clone https://github.com/alex-muliande/Vicinity.git```.
##### Open the project on your terminal:
  - ```atom . or code .``` , according to the type of your text editor.
##### Move to your project directory:
  - ```cd Vicinity```.
##### Install virtual environment using python:
  - ```python3.6 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.6``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After confirming you have all this
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.


#### For more information read the following django and python documentation:
  - [DjangoDocumentation](https://docs.djangoproject.com/en/1.11/intro/install/)
  - [PythonDocumentation](https://www.python.org/doc/)


### User Stories
##### As a user, I would like  Sign in with the application to start using..
##### As a user I would like to Set up a profile about me and a general location and my neighborhood name.
##### As a user I would like to Find a list of different businesses in my neighborhood
##### As a user I would like to Find Contact Information for the health department and Police authorities near my neighborhood.
##### As a user I would like to Create Posts that will be visible to everyone in my neighborhood.
##### As a user I would like to Change My neighborhood when I decide to move out.
##### As a user I would like to Only view details of a single neighborhood.

### Technologies Used
##### Python
##### Django
##### PostgreSQL
##### HTML5
##### CSS3

## Dependencies
##### Postgresql

### Licence
[MIT](LICENSE)

### Contact
##### alexnad425@gmail.com
