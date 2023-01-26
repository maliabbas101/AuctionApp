# Online Auction Application

Online Auction Application is an online application where people(sellers,buyers) can signup, Sellers can create thier products and enlist them into auctions.Then buyers can come and bid on products.
## Python Interpreter
```bash
python_version = "Python 3.8.9"
```
## Dependencies
```bash
django = "*"
psycopg2 = "*"
django-environ = "*"
crispy-bootstrap5 = "*"
django-crispy-forms = "*"
cloudinary = "*"
django-cloudinary-storage = "*"
pillow = "*"
black = "*"
```

## Usage
First clone or download this project.
Once you open this project first you have to create virtual environment.Then you can run the following commands.
```bash
pipenv shell
```
Then you can run server through the following command.
```bash
./manage.py runserver
```

Before running the server just make sure to run.
```bash
./manage.py migrate
```


## Deployment

You can deploy the application on any online cloud platform just make sure to migrate the database through following command.
```bash
./manage.py migrate
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Application Link

[Dinerdash](https://dinerdash91.herokuapp.com/)
