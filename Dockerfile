FROM python:3.13.1-bookworm
# Above code copies OS system and python 3.13 from docker hub site to empty container
WORKDIR /flask-docker
# above code creates a flask-docker path in the empty container where all the files will be stored inside container

RUN python3 -m pip install --upgrade pip
# above code makes sure latest pip is there
COPY requirements.txt requirements.txt
# copy source_path dest_path
# above code copies requirements.txt from current local path to container and inside container it will be inside flask-docker which we have created above
RUN pip3 install -r requirements.txt
# above code install all the libraries present inside requirements.txt

COPY . .
# above code copies all files from current path to flask-docker path of container
# first . means current local path

CMD ["python3", "-m", "flask", "run","--host=0.0.0.0"]
# above code makes sure flask code will run on docker. if python file name is app.py where flask code is written then we dont have to pass app.py
# otherwise if name is different then we've to pass name of .py file also