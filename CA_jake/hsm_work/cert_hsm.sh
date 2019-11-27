#!/bin/bash
echo jake
echo OFF
_homedir=/home/leslielamport/Documents/Github/openssl-pkcs11/CA_jake/hsm_work/
_config_file=$_homedir"/openssl.cnf"
_module=/usr/local/lib/softhsm/libsofthsm2.so
_test=test
_chainfile=chainstunnel.pem

chain() {

	read -p "Please enter the Root CA Key name:" _rootname
	read -p "HSM key needs an ID:" _keyid
	#echo $_rootname > $_homedir/"rootfilename.txt"
	#/usr/local/ssl/bin/openssl version
	
	
	#openssl genrsa -out $_homedir"/"$_rootname".key" 4096
		
	#Change key generation to be on-board HSM	
	pkcs11-tool --module $_module --login --pin 12345 --keypairgen --key-type rsa:4096 --label "root_key" --id $_keyid --usage-sign
	
	
	
	
	#Get key from the HSM to make crt
	openssl req -out $_homedir"/"$_rootname".crt" -new -nodes -engine pkcs11 -keyform engine -key slot_748671277-label_root_key -config $_config_file -days 9125 -extensions root_cert -reqexts v3_req -x509 -subj "/C=GB/ST=Essex/L=Ipswich/O=BT PLC/OU=test/CN=jake test root"
	openssl x509 -text -noout -in $_homedir"/"$_rootname".crt"
	echo $_rootname
	
	: '
	read -p "Please enter the Issuing CA Key name: " _issuingname
	echo $_issuingname > $_homedir/"issuingfilename.txt"
	openssl genrsa -out $_homedir"/"$_issuingname".key" 2048
	openssl req -out $_homedir"/"$_issuingname".csr" -new -key $_homedir"/"$_issuingname".key" -config $_homedir"/openssl.cnf" -sha256 -subj "/C=GB/ST=Essex/L=Ipswich/O=BT PLC/OU=test/CN=jake test inter"
	openssl x509 -req -in $_homedir"/"$_issuingname".csr" -extfile $_homedir"/openssl.cnf" -extensions inter_cert -days 1825 -CA $_homedir"/"$_rootname".crt" -CAkey $_homedir"/"$_rootname".key" -CAcreateserial -out $_homedir"/"$_issuingname".crt"
	openssl x509 -text -noout -in $_homedir"/"$_issuingname".crt"
	echo $_issuingname

	read -p "Please enter the End CA Key name: " _endname
	echo $_endname > $_homedir"/endfilename.txt"
	openssl genrsa -out $_homedir"/"$_endname".key" 2048
	openssl req -out $_homedir"/"$_endname".csr" -new -key $_homedir"/"$_endname".key" -config $_homedir"/openssl.cnf" -reqexts v3_req -sha256 -subj "/C=GB/ST=Essex/L=Ipswich/O=BT PLC/OU=test/CN=www.jaketeststunnelfdqn.com"
	openssl x509 -req -in $_homedir"/"$_endname".csr" -extfile $_homedir"/openssl.cnf" -extensions usr_cert -days 365 -CA $_homedir"/"$_issuingname".crt" -CAkey $_homedir"/"$_issuingname".key" -CAcreateserial -out $_homedir"/"$_endname".crt"
	openssl x509 -text -noout -in $_homedir"/"$_endname".crt"
	echo $_endname
	'
	echo "Certificates Generated"
	read -n 1 -s -r -p "Press any key to continue..."
	clear
	menu
	
}

package() {
	_rootfilename=$(cat $_homedir/rootfilename.txt)
#	_rootfilename=<$_homedir/rootfilename.txt
#	_rootfilename="$(echo $_rootfilename | tr -d ' ')"
	echo $_rootfilename
	
	_issuingfilename=$(cat $_homedir/issuingfilename.txt)
#	_issuingfilename=<$_homedir/issuingfilename.txt
#	_issuingfilename="$(echo $_issuingfilename | tr -d ' ')"
	echo $_issuingfilename

	_endfilename=$(cat $_homedir/endfilename.txt)	
#	_endfilename=<$_homedir/endfilename.txt
#	_endfilename="$(echo "$_issuingfilename" | tr -d ' ')"
	echo $_endfilename

	cat $_homedir/$_endfilename.key > $_homedir/$_chainfile
	openssl x509 -issuer -subject -noout -in $_homedir/$_endfilename.crt >> $_homedir/$_chainfile
	cat $_homedir/$_endfilename.crt >> $_homedir/$_chainfile
	openssl x509 -issuer -subject -noout -in $_homedir/$_issuingfilename.crt >> $_homedir/$_chainfile
	cat $_homedir/$_issuingfilename.crt >> $_homedir/$_chainfile
	
	echo "Certs Packaged"
	read -n 1 -s -r -p "Press any key to continue..."
	clear
	menu
}

delete() {

	rm $_homedir/*.crt
	rm $_homedir/*.key
	rm $_homedir/*.pem
	rm $_homedir/*.csr
	rm $_homedir/*.srl
	rm $_homedir/*.txt
	echo "Files Deleted"
	read -n 1 -s -r -p "Press any key to continue..."
	clear
	menu
}

end() {

	echo "==============QUITTING==============="
	read -n 1 -s -r -p "Press any key to exit..."
	clear
}

menu() {
	echo $_number
	echo "------------------------MENU------------------------"
	echo "1: Generate Chain"
	echo "2: Package Certs"
	echo "3: Delete Certs"
	echo "4: Quit"
	echo "----------------------------------------------------"
	read -p "Please enter an input: " _number
	if [[ "$_number" -eq "1" ]]; then
	chain
	elif [[ "$_number" -eq "2" ]]; then
	package
	elif [[ "$_number" -eq "3" ]]; then
	:
	delete
	elif [[ "$_number" -eq "4" ]]; then
	:
	end
	else
		echo "Invalid input, please enter a number from the menu."
		menu
	fi
}
	


menu
