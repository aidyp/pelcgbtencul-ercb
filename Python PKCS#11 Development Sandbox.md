# Python PKCS#11 Development Sandbox



## Motivation

HSMs are designed to work with the PKCS#11 specification. In order to work with HSMs at a high level, you should understand how to use this specification. The specification is in C, which is too low-level to make for a good learning environment. This sandbox uses a python wrapper to eliminate some of the more painful aspects of C, so you can focus on learning how the PKCS#11 specification works.



## Housekeeping

### Directories

```
Development Directory:
/home/leslielamport/development/pythonic_hsm/

SoftHSM pkcs11 library:
/usr/local/lib/softhsm/libsofthsm2.so
```



## Code Samples

### Accessing Tokens

```python
import pkcs11 as pk
import os

lib = pk.lib(os.environ['PKCS11_MODULE'])
token = lib.get_token(token_label='Token-1')

with token.open(user_pin='12345') as session:
    #Do some cryptography!
```



### Generating Keys

#### Symmetric Keys

Symmetric keys are generating using the `get_key()` method. For example, you can make a temporary session key here.

```python
key = session.generate_key(pk.KeyType.AES, 256)
```



Sessions are *read-only* by default. To generate keys permanently, you need to change the session to *read/write*. 

```python
with token.open(rw=True, user_pin='12345') as session:
	#Now you can create new objects on the HSM
```



You can find the full API reference for creating keys here: https://python-pkcs11.readthedocs.io/en/latest/api.html#pkcs11.Session.get_key. In short, the method looks like this,

```
generate_key(key_type, key_length=None, id=None, label=None, store=False, capabilities=None, mechanism=None, mechanism_param=None, template=None)
```



Here's an example of generating a permanent AES key

```python
#Parameter build
	
kparams = {}
kparams['key_type']     = pk.KeyType.AES #KeyType
kparams['key_length']   = 256            #int
kparams['id']           = b'00000002'    #bytes
kparams['label']        = 'myfirstkey'   #string
kparams['store']        = True           #Bool

new_key = session.generate_key(**kparams)
```



#### Asymmetric Keys