# Web Notepad
	
	A simple site contains two pages. In the first page you can enter and save the note, on the other see all notes and clear notepad. Sorting by number of unigue words.

# For start you must create virtualenv:

	\Notepad>python -m venv venv

# Activate your virtualenv:	
	
	\Notepad>venv\Scripts\activate

# Install requiments:
	
	(venv)>pip install -r requirements.txt

# Set the FLASK_APP enviroment variable:

	(venv)>set FLASK_APP=notepad.py

# Run the server and go to the http://127.0.0.1:5000/:
	
	(venv)>flask run