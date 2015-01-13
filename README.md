
	git clone https://github.com/timtan/bootstrap-customize-sample
	
	

### Setting Virtualenv

At first, you should make sure you have [virtualenv](http://www.virtualenv.org/) installed. 

after that, just cd to your\_project_name:

   cd bootstrap-customize-sample

Then create your virtualenv:

    virtualenv venv
    
Second, you need to enable the virtualenv by

	source venv/bin/activate
	



### Install requirements

For development:

    pip install -r requirements/local.txt


### Start To Run

to start project.  cd your\_project_name again (find manage.py )

```bash
python manage.py migrate   # you just do it once

python manage.py runserver
```

feel free to visit [http://127.0.0.1:8000/style_guide/](http://127.0.0.1:8000/style_guide/) and edit _varialbe.scss, you will see the amazing starting style guide for the project

	
