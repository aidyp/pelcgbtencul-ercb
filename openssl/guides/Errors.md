## Errors that have occured and their fixes:

#### Failed loading private key:

Aldrin had multiple slots on his SoftHSM and did not specify a slot to generate the private key in when he generated the key pair on the HSM, so it automiatically assigned the key to Slot 0, then when Aldrin tried to create a certificate using the private key, he was using the ID of Slot 3.

2 Fixes:

1)

The fix was to change the slot ID of `-key slot_748671277-label_root_key` to the ID of Slot 3.

2)

The second fix would be to specify the slot when generating the key using `--slot 0x2c9fd12d` (yours will be different, but use the ID with this format. You can get this ID using `sudo softhsm2-util --show-slots`)

#### 140004762969216:error:0909006C:PEM routines:get_name:no start line:../crypto/pem/pem_lib.c:745:Expecting: CERTIFICATE REQUEST

Certificate Request must start with `----- BEGIN CERTIFICATE REQUEST -----`

#### openssl x509 does not take -keyform engine as an input as it only accepts PEM|DER, not sure how to connect to HSM using x509 yet.

The fix is to use CAKeyform.