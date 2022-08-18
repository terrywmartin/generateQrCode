# generateQrCode

Generate a QR Code from a website URL.  Enter the URL then hit 'Generate'.   A QR Code will displayed along with a download button.

TODO:

 - Improve user interface code
 - Add error handling
 - Add comments
 - Add Tests
 - Refactor code as I learn new techniques
 - Ready for deployment

I first saw this idea on Traversy Media's YouTube page.  He made this using Html/Tailwind CSS/Javascript.  I wanted to see if I could do it using Django.  I did this in a couple of hours.  I'm terrible at front-end so it's not very polished, but it works.  I'm sure there a few places in the code that could use improving but I was really focused on getting it done quickly.  

I am still learning so forgive the crudeness of the code.

## To run the project

Create your virtual environment.  I use virtualenvwrapper-win.

```
mkvirtialenv genqrcode
```

Install dependencies in your virtual environment.

```
pip install -r requirements.txt
```

Run the project.

```
py manage.py runserver
```
