# Authentic

Just me exploring Django's authentication framework.


Functionality:

* Register user
* Authenticate user
* List of 5 last successful logins (only authenticated users allowed)

## Setup

### Install Python
https://docs.djangoproject.com/en/dev/topics/install/?from=olddocs

Get Python at http://www.python.org. If you’re running Linux or Mac OS X,
you probably already have it installed.

### Install pip
Install [pip](http://www.pip-installer.org/en/latest/index.html).
The easiest is to use [the standalone pip installer](http://www.pip-installer.org/en/latest/installing.html#using-the-installer).
If your distribution already has pip installed, you might need to
update it if it's outdated. (If it's outdated, you'll know
because installation won't work.)

### Install Django
If you're using Linux, Mac OS X or some other flavor of Unix, enter the command

> sudo pip install Django

at the shell prompt.

If you're using Windows, start a command shell with administrator privileges and run the command

> pip install Django

This will install Django in your Python installation's site-packages directory.

### Download Authentic from Github

    git clone git@github.com:ashpool/authentic.git

or

[Download zip](https://github.com/ashpool/authentic/zipball/master)

## Usage

    cd authentic
    python manage.py runserver

Direct your browser to http://localhost:8000


## Encryption of passwords
https://docs.djangoproject.com/en/dev/topics/auth/#how-django-stores-passwords

By default, Django uses the PBKDF2 algorithm with a SHA256 hash, a password stretching
mechanism recommended by NIST, as its one way hashing or password storage algorithms.

This should be sufficient for most users: it's quite secure, requiring massive amounts of
computing time to break.

Django stores a secret key in settings.py used as salt:

    #Make this unique, and don't share it with anybody.
    SECRET_KEY = 'r-7tm7riwgt9!g-z95@$%rntmli#72lh@y+1@nwu)g)q+f9#p&amp;'

When applying this algorithm on "foobar" we get:

    pbkdf2_sha256$10000$9sr17uhNhreK$Q0MSV64ITz6+yIKk6cZhOyEm03inau5zZYhExH2B/Wk=

The prepend "pbkdf2_sha256$10000" is just a markup for the algorithm used and the number of iterations, in this case 10000.

### PBKDF2 (Password-Based Key Derivation Function)
http://en.wikipedia.org/wiki/PBKDF2
PBKDF2 (Password-Based Key Derivation Function) is a key derivation function that is part of RSA
Laboratories' Public-Key Cryptography Standards (PKCS) series, specifically PKCS #5 v2.0,
also published as Internet Engineering Task Force's RFC 2898. It replaces an earlier standard,
PBKDF1, which could only produce derived keys up to 160 bits long.

PBKDF2 applies a pseudorandom function, such as a cryptographic hash, cipher, or HMAC to
the input password or passphrase along with a salt value and repeats the process many
times to produce a derived key, which can then be used as a cryptographic key in
subsequent operations. The added computational work makes password cracking much more
difficult, and is known as key stretching.

When the standard was written in 2000, the recommended minimum number of iterations was 1000,
but the parameter is intended to be increased over time as CPU speeds increase.
Having a salt added to the password reduces the ability to use a precomputed dictionary to
attack a password (such as rainbow tables) and means that multiple passwords have to be
tested individually, not all at once. The standard recommends a salt length of at least 64 bits.


### SHA256 (Secure Hash Algorithm)
http://en.wikipedia.org/wiki/SHA-2

SHA-2 is a set of cryptographic hash functions (SHA-224, SHA-256, SHA-384, SHA-512) designed by
the National Security Agency (NSA) and published in 2001 by the NIST as a U.S.
Federal Information Processing Standard. SHA stands for Secure Hash Algorithm.

    SHA256("")
    0x e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855


Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the avalanche effect. For example, adding a period to the end of the sentence:

    SHA224("The quick brown fox jumps over the lazy dog")
    0x 730e109bd7a8a32b1cb9d9a09aa2325d2430587ddbc0c38bad911525

    SHA224("The quick brown fox jumps over the lazy dog.")
    0x 619cba8e8e05826e9b8c519c0a5c68f4fb653e8a3d8aa04bb2c8cd4c


## Secure Sessions
https://docs.djangoproject.com/en/dev/topics/auth/#how-django-stores-passwords

Django hooks its authentication framework into the request objects.

    if request.user.is_authenticated():
        # Do something for authenticated users.
    else:
        # Do something for anonymous users.

Django provides two functions in django.contrib.auth: authenticate() and login().

### authenticate()
To authenticate a given username and password, use authenticate(). It takes two keyword arguments, username and password, and it returns a User object if the password is valid for the given username. If the password is invalid, authenticate() returns None. Example:

    from django.contrib.auth import authenticate
    user = authenticate(username='john', password='secret')
    if user is not None:
        if user.is_active:
            print("You provided a correct username and password!")
        else:
            print("Your account has been disabled!")
    else:
        print("Your username and password were incorrect.")

### login()
To log a user in, in a view, use login(). It takes an HttpRequest object and a User object. login() saves the user's ID in the session, using Django's session framework, so, as mentioned above, you'll need to make sure to have the session middleware installed.

Note that data set during the anonymous session is retained when the user logs in.

This example shows how you might use both authenticate() and login():

    from django.contrib.auth import authenticate, login

    def my_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
        else:
            # Return an 'invalid login' error message.


### logout()
To log out a user who has been logged in via django.contrib.auth.login(), use django.contrib.auth.logout() within your view. It takes an HttpRequest object and has no return value. Example:

    from django.contrib.auth import logout

    def logout_view(request):
        logout(request)
        # Redirect to a success page.