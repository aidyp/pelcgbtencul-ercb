extern crate hex;
extern crate base64;


pub fn str_from_hex(hex_str: &str) -> Vec<u8> {
    let bytes = hex::decode(hex_str).expect("Decoding Error");
    return bytes
}

pub fn bytes_to_hex(bytes: &[u8]) -> String {
    return hex::encode(&bytes);
}

pub fn bytes_to_b64(bytes: &[u8]) -> String {
    return base64::encode(&bytes);
}

pub fn b64_to_bytes(b64_str: &str) -> Vec<u8> {
    let bytes = base64::decode(b64_str).expect("Decoding Error");
    return bytes
}