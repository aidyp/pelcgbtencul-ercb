# OpenSSL & SoftHSM

The aim of this directory is to explore using our software HSM (softHSMv2) with OpenSSL. In this document I'm just trying to write down some stuff so I don't have to keep reminding myself of it.

The sample workflow here is to load a key into the softHSM first, then try to get OpenSSL to use it to do some signing work.



## Initialising Tokens

The softHSM requires root access, so use `sudo` when running these commands.

```bash
sudo softhsm-util --init-token --label "Token-1" --token "Token-1"
```

Initialises the token I've already created on the softHSM.



### Generating a Key via OpenSSL

Ideally you'd generate the key on the HSM, but baby steps I think. Especially as this might be a feature we need to learn and practice in the future.