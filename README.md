resthookdemo
============

Check it out live at [http://demo.resthooks.org/](http://demo.resthooks.org/).

### Run Locally

Assuming you use virtualenv:

```
git clone git@github.com:zapier/resthookdemo.git
mkvirtualenv resthookdemo
pip install -r requirements.txt
./manage.py syncdb
./manage.py loaddata crm.json
./manage.py runserver
```

Log in as user/admin on `http://localhost:8000/` and enjoy!
