# Camera Kit Manager

Camera Kit Manager is a Django application for comparing multiple kits (i.e. combinations of lenses) to find the optimal
combination of focal length coverage and total kit weight.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required python libraries.

```bash
pip install -r requirements.txt
```

Create the required migrations and apply these.

```bash
python manage.py makemigrations
python manage.py migrate
```

Create a superuser for the admin site.

```bash
python manage.py createsuperuser
```

Start the Django development server.

```bash
python manage.py runserver 
```

## Usage

After the development server is started, you can create new lenses in the Django admin page 
[/admin/](http://127.0.0.1:8000/admin/).

> \[!IMPORTANT]
>
> The input for zoom lens focal lengths has to be in the following format: min-max (e.g. 70-200).

Then visit the index page [/](http://127.0.0.1:8000/) to create a new kit using the _New Kit_ link. 
Here you can select multiple lenses via _Ctrl_+_Click_.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
