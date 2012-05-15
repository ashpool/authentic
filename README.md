# Authentic

Just me exploring Django's authentication framework.


Functionality:

* Register user
* Authenticate user
* List of 5 last successful logins (only authenticated users allowed)


## Encryption of passwords
https://docs.djangoproject.com/en/dev/topics/auth/#how-django-stores-passwords

By default, Django uses the PBKDF2 algorithm with a SHA256 hash, a password stretching
mechanism recommended by NIST, as its one way hashing or password storage algorithms.

This should be sufficient for most users: it's quite secure, requiring massive amounts of
computing time to break.

Django stores a secret key in settings.py
> # Make this unique, and don't share it with anybody.
> SECRET_KEY = 'r-7tm7riwgt9!g-z95@$%rntmli#72lh@y+1@nwu)g)q+f9#p&amp;'

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

> SHA256("")
> 0x e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855


Even a small change in the message will (with overwhelming probability) result in a mostly different hash, due to the avalanche effect. For example, adding a period to the end of the sentence:

> SHA224("The quick brown fox jumps over the lazy dog")
> 0x 730e109bd7a8a32b1cb9d9a09aa2325d2430587ddbc0c38bad911525
> SHA224("The quick brown fox jumps over the lazy dog.")
> 0x 619cba8e8e05826e9b8c519c0a5c68f4fb653e8a3d8aa04bb2c8cd4c


## Secure Sessions

> django.contrib.sessions.middleware.SessionMiddleware
> django.middleware.csrf.CsrfViewMiddleware
> django.contrib.auth.middleware.AuthenticationMiddleware

>  if request.user.is_authenticated():
>      # Do something for authenticated users.
>  else:
>      # Do something for anonymous users.