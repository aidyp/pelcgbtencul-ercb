== Python PKCS#11 Development Directory ==

The purpose of this directory is to practice using a (virtual) HSM through the PKCS#11 API. 

This project uses python as a high level wrapper, so it's easy to understand what's going on.

We'll try and make a basic example of signing and verifying an arbitrary file through this HSM

Key Files:

Code_signing.py is a short primitive showing how to sign arbitrary data on an HSM with an RSA private key.

== Setting Up The Environment ==

At the moment, we have to export the environment variable PKCS11_MODULE every-time.

Let's make that permanent. I don't want to encapsulate it, because I think it's important to be aware of the initialisation procedure.

== softHSM pkcs11 implementation ==

The library is
/usr/local/lib/softhsm/libsofthsm2.so


== Edit Log ==

At first I thought I was generating keys okay, but it's turning out to not be so easy.

Perhaps I should write a utility to examine objects and their features so I can understand what's going on.