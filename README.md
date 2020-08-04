# cognito_utils
Utilities and example code to manage AWS Cognito User Pools and users. Clone the repo and configure a Python 3.7.3 virtualenv. Install the required dependencies from the provided requirements file. The commands to do this from macOS terminal:
```python
virtualenv -p `which python3` .venv3
source .venv3/bin/activate
pip install -r requirements.txt
```


## create_user
Create a user in a specified user pool and set it's initial password. Results in a user created with the desired password and Account Status in CONFIRMED state. This program creates a user with a temporary password ("Password123#") and executes an initial login to change the password to the desired value.

