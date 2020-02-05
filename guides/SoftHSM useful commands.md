# SoftHSM Useful Commands

### Variables

Let module=/usr/local/lib/softhsm/libsofthsm2.so

### Commands

Note: best practise to write all commands in sudo



Make a new initialised token and intialised pin. The slot number must not be of an existing slot:

`sudo pkcs11-tool --module $module --init-token --label "relevant label" --slot 0x3 --login --init-pin`



Delete token and linked slot:

`sudo softhsm2-util --delete-token --token "relevant label"`



Lists slots with **appropriate slot numbers** :

`sudo softhsm2-util --show-slots`



View objects (keys) on specific token:

`sudo pkcs11-tool --module $module --login --token-label "relevant label" -O`



View all objects on SoftHSM:

`sudo pkcs11-tool --module $module -L`