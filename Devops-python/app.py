# Import the load_dotenv() function to load environment variables from a .env file
from dotenv import load_dotenv

# Import the os module to access environment variables and operating system features
import os

# Load environment variables from the .env file into the current environment
load_dotenv()


# Read required environment variables
# If APP_ENV is missing, use "development" as the default value
app_env = os.getenv("APP_ENV", "development")

# Read the database host from the environment
db_host = os.getenv("DB_HOST")

# Read MAX_RETRIES and convert it from a string to an integer
max_retries = int(os.getenv("MAX_RETRIES"))


# Display the loaded configuration values
print("==== Connection Summary ====")
print(f"Environment: {app_env}")
print(f"Database Host: {db_host}")
print(f"Max Retries: {max_retries}")


# Verify that all required environment variables are available
print("\n==== Validation ====")
for var in ["APP_ENV", "DB_HOST", "MAX_RETRIES"]:
    if os.getenv(var) is None:
        print(f"Warning: {var} is not set in the environment variables.")
    else:
        print(f"{var} is set")


"""
Output:
==== Connection Summary ====
Environment: Prod
Database Host: mydb.server.com
Max Retries: 5

==== Validation ====
APP_ENV is set
DB_HOST is set
MAX_RETRIES is set


2nd time run output: by removing db_host
==== Connection Summary ====
Environment: Prod
Database Host: None
Max Retries: 5

==== Validation ====
APP_ENV is set
Warning: DB_HOST is not set in the environment variables.
MAX_RETRIES is set

Note: 
if you try to run this python script from outsideof the myenv virtual environment, you will get the following error:
(myenv) E:\aws_github_repos\Programming\Python\Devops-python>deactivate
E:\aws_github_repos\Programming\Python\Devops-python>python app.py
Traceback (most recent call last):
  File "E:\aws_github_repos\Programming\Python\Devops-python\app.py", line 2, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
"""

