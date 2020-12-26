## Openssl cms with Software HSM

`OPENSSL_CONF=` is used to specify config as cms does not have a config flag. Insert the signing private key, its corresponding certificate and the intermediate certifcate. In addition, specify the engine the keys are in. 

`OPENSSL_CONF=config.cnf openssl cms -sign -in testfile.txt -out testfile256signed.pem -outform PEM -certfile intermediateCert.pem -noattr -nodetach -signer EndCert.pem -inkey slot_${slot2}-label_${label2} -keyform engine -engine pkcs11`



View the signature

`openssl cms -cmsout -inform PEM -in testfile256signed.pem -print`



Verify the signing key certificate and the chain of the certificate.

`openssl cms -verify -inform PEM -in testfile256signed.pem -CAfile rootCert.pem`