# Install dependencies by upgrading pip and installing requirements from requirements.txt
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run pylint to perform linting on the app.py file
lint:
	pylint --disable=R,C app.py

# Run the black formatter on all .py files in the current directory
format:
	black *.py

# Define a target 'all' that includes the 'install', 'lint', and 'format' targets
all: install lint format