# SoftHSM key management

Note: best practise to write all commands in sudo

### Variables

Let `module=/usr/local/lib/softhsm/libsofthsm2.so`

### Prerequisites

Make a new initialised token and intialised pin. The slot number must not be of an existing slot:

`sudo pkcs11-tool --module $module --init-token --label "relevant label" --slot 0x2 --login --init-pin`



Lists slots with **appropriate slot numbers** :

`sudo softhsm2-util --show-slots`

### Script

Make a key pair on software HSM:

`pkcs11-tool --module $module --login -p 12345 --keypairgen --key-type rsa:4096 --label $label1 --id 1007 --slot $slot1 --usage-sign`



Make CSRs/Certificates like before but referencing keys in the following way with additional engine and keyform flags:

`openssl req -out root.pem -new -nodes -key slot_$slot1-label_$label1 -keyform engine -config $config -x509 -days 1000 -extensions cert -reqexts csr_extensions -subj "/C=GB/ST=Suffolk/L=Ipswich/O=Company/OU=test/CN=root" -verbose -engine pkcs11`



### Additional commands

Delete token and linked slot:

`sudo softhsm2-util --delete-token --token "relevant label"`



View objects (keys) on specific token:

`sudo pkcs11-tool --module $module --login --token-label "relevant label" -O`



View all objects on SoftHSM:

`sudo pkcs11-tool --module $module -L`