#Python Virtual Environment:--

#It is basicaly an isolated workspace which help you to copy python intepreator along with it dependencies without intefering eith other projects 

# for example if you system has multiple python project and they use different flask version so for it you create a different virtual env for both project where one contains flask 2.o and second conatins flask 3.o.




# Two methods to create python virtual environment:-

# 1. by using virtualenv dependency 

# a. install virtual env , pip install virtualenv
# b. create virtual env in particular folder where it is required, pip -m venv "vertual env name"
# c. activate it by going to the script directory of particula folder and by writing ACTIVATE, /virtualenvname/scripts ACTIVATE
# to deactivate it type DEACTIVATE


# 2. By using virtualenvwrapper 

# a. install virtual env wrapper, pip install virtualenvwrapper-win 
# b. create virtual env in directory where you want to create, mkvirtualenv "environment name"

# It directly gets activate you dont have to actvate it to deactivate it type DEACTIVATE