use std::env;
use std::fs;
use std::collections::HashMap;

/* this crate thing is very useful! */
extern crate hex;
extern crate base64;
extern crate lazy_static;


/* Lookup Tables */
lazy_static! {}
    static ref ENG_FREQ_TABLE: HashMap<u8, f64> = {
        let mut m = HashMap::new();
        m.insert(65, 0.08167);
        /* more inserts to go here */

        m
    };



fn from_hex(hex_str: &str) -> Vec<u8> {
    let bytes = hex::decode(hex_str).expect("Decoding failed");
    return bytes;
}

fn to_hex(bytes: Vec<u8>) -> String {
    let hex_str = hex::encode(bytes);
    return hex_str;
}

fn englishness(bytes: Vec<u8>) --> f64 {
    

    /* Build the frequency table for this set of bytes */
    let mut frequency_table: HashMap<u8, f64> = HashMap::new();
    for byte in bytes.iter() {
        *frequency_table.entry(byte).or_insert(0) += 1;
    
    }
    let normal: u32 = bytes.len();
    for (_, val) in frequency_table.iter_mut() {
        *val = *val / normal as f64;
    } 
    
    
    /* sum of sqrts of products of probability */

    let mut coefficient: f64 = 0.0;
    for byte in bytes.iter() {
        match ENG_FREQ_TABLE.get(byte) {
            Some(value) => ,// square root
            None => (),
        }
    }



    return coefficient

    
}

fn challenge_one(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    /* get raw bytes */
    let bytes = from_hex(&contents);

    /* convert to base64 */
    let b64 = base64::encode(&bytes);

    /* print the result */
    println!("base64: {}", b64);
}

fn challenge_two(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    /* File contains two hex strings that must be XOR'd together */
    let lines: Vec<&str> = contents.split("\n").collect();
    
    let (left, right) = (from_hex(&lines[0]), from_hex(&lines[1]));
    let res = vec_byte_xor(left.as_slice(), right.as_slice());
    println!("result: {}", to_hex(res));


}




fn challenge_thr(filename: &String) {

    // Get the target 
    let contents = fs::read_to_string(filename).expect("File read failed");
    let target = from_hex(&contents);

    

    // Create a vector for each byte 
    let mut xor_vec = vec![0; target.len()];
    let mut res_vec = vec![0; 256];
    for n in 0..=255 {
        /* Write n to the vector */
        for x in 0..target.len() {
            xor_vec[x] = n;
        }

        res_vec = vec_byte_xor(target.as_slice(), xor_vec.as_slice());
        println!("xor w/ {}: {}", n, to_hex(res_vec));       

    }


}


fn vec_byte_xor(v1: &[u8], v2: &[u8]) -> Vec<u8> {
    /* using iterators */
    let v3: Vec<u8> = v1
        .iter()
        .zip(v2.iter())
        .map(|(&x1, &x2)| x1 ^ x2)
        .collect();
    
    return v3;
}

fn main() {

    let args: Vec<String> = env::args().collect();
    let challenge = &args[1];
    let challenge_file = &args[2];

    match challenge.as_str() {
        "1" => challenge_one(challenge_file),
        "2" => challenge_two(challenge_file),
        "3" => challenge_thr(challenge_file),
        _ => println!("You haven't written code for this challenge yet!"),
    }
}
