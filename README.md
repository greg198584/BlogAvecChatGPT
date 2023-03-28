# Flask Blog

Flask Blog is a web application built using the Flask micro-framework. It allows users to create an account, log in, create posts and add comments to other users' posts.

https://youtu.be/d21bEZEU1Fo

## Usage

To use this project, follow these steps:

1. Clone this repository.

2. Create a virtual environment and activate it. 

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```


3. Install the dependencies from `requirements.txt`.

```bash
$ pip install -r requirements.txt
```


4. Initialize the database.

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```

5. Run the application.

```bash
$ flask run
```

The application should now be running on `http://localhost:5000/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
