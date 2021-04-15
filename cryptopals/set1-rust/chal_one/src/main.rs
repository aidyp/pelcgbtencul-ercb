use std::env;
use std::fs;
use std::collections::HashMap;
use std::collections::hash_map::Entry::{Occupied, Vacant};
mod lib;

/* this crate thing is very useful! */

extern crate hex;
extern crate base64;
#[macro_use]
extern crate lazy_static;


/* Lookup Tables */
lazy_static! {
    static ref ENG_FREQ_TABLE: HashMap<u8, f64> = {
        let mut m = HashMap::new();
        /* Lower case english frequency table */
        m.insert(97, 0.08167);
        m.insert(98, 0.01492);
        m.insert(99, 0.02782);
        m.insert(100, 0.02782);
        m.insert(101, 0.04253);
        m.insert(102, 0.1270);
        m.insert(103, 0.02228);
        m.insert(104, 0.02015);
        m.insert(105, 0.06094);
        m.insert(106, 0.06966);
        m.insert(107, 0.00153);
        m.insert(108, 0.00772);
        m.insert(109, 0.04025);
        m.insert(110, 0.02406);
        m.insert(111, 0.06749);
        m.insert(112, 0.07507);
        m.insert(113, 0.01929);
        m.insert(114, 0.00095);
        m.insert(115, 0.05987);
        m.insert(116, 0.06327);
        m.insert(117, 0.09056);
        m.insert(118, 0.02758);
        m.insert(119, 0.00978);
        m.insert(120, 0.02360);
        m.insert(121, 0.00150);
        m.insert(122, 0.01974);
        m.insert(123, 0.00074);
        m
    };
}


fn from_hex(hex_str: &str) -> Vec<u8> {
    let bytes = hex::decode(hex_str).expect("Decoding failed");
    return bytes;
}

fn to_hex(bytes: &[u8]) -> String {
    let hex_str = hex::encode(bytes);
    return hex_str;
}

fn print_freq_tbl(mut freq_table: HashMap<u8, f64>) {
    println!("Frequency table");
    println!("***");
    for (key, val) in freq_table.iter_mut() {
        println!("{} : {}", key, val);
    }
}

fn englishness(bytes: &[u8]) -> f64 {
    

    /* Build the frequency table for this set of bytes */
    let mut frequency_table: HashMap<u8, f64> = HashMap::new();
    for byte in bytes.iter() {
        *frequency_table.entry(*byte).or_insert(0.0) += 1.0;
    
    }
    let normal = bytes.len() as f64;   
    
    /* sum of sqrts of products of probability */


    /* This is so ugly, need to find the more idiomatic way of doing things */
    let mut coefficient: f64 = 0.0;
    for byte in ENG_FREQ_TABLE.keys() {
        let fq = match frequency_table.entry(*byte) {
            Vacant(entry) => entry.insert(0.0),
            Occupied(entry) => entry.into_mut(),
        };
        *fq /= normal;
        let overlap = ENG_FREQ_TABLE[byte] * frequency_table[byte];
        coefficient += overlap.sqrt();
    }

    return coefficient

    
}

fn challenge_one(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    /* get raw bytes */
    let bytes = lib::encoding::str_from_hex(&contents);

    /* convert to base64 */
    let b64 = lib::encoding::bytes_to_b64(&bytes);

    /* print the result */
    println!("base64: {}", b64);
}

fn challenge_two(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    /* File contains two hex strings that must be XOR'd together */
    let lines: Vec<&str> = contents.split("\n").collect();
    
    let (left, right) = (from_hex(&lines[0]), from_hex(&lines[1]));
    let res = vec_byte_xor(left.as_slice(), right.as_slice());
    println!("result: {}", to_hex(res.as_slice()));


}

fn guess_xor(bytes: &[u8]) -> (f64, Vec<u8>) {


    let length = bytes.len();
    let mut xor_vec = vec![0; length];
    let mut bst_coef: f64 = 0.0;
    let mut res_vec = vec![0; length];
    for n in 0..=255 {
        for x in 0..length {
            xor_vec[x] = n;
        }

        let tmp_vec = vec_byte_xor(bytes, xor_vec.as_slice());
        let tmp_coef = englishness(tmp_vec.as_slice());
        if tmp_coef >= bst_coef {
            bst_coef = tmp_coef;
            res_vec = tmp_vec;
        }
    }

    /* Print the vector alongside it's coefficient */
    //println!("{} : {}", bst_coef, to_hex(res_vec.as_slice()));
    return (bst_coef, res_vec)
}


fn challenge_four(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong reading");

    // Read every line into a hex string
    let lines: Vec<&str> = contents.split("\n").collect();

    // For each line, work out the best xor character
    let mut bst_coef: f64 = 0.0;
    let mut bst_vec = Vec::new();
    for line in lines.iter() {
        let (coef, bytes_vec) = guess_xor(from_hex(line).as_slice());
        if coef >= bst_coef {
            bst_coef = coef;
            bst_vec = bytes_vec
        }
    }
    println!("{}: {}", bst_coef, to_hex(bst_vec.as_slice()));

}

fn challenge_thr(filename: &String) {

    // Get the target 
    let contents = fs::read_to_string(filename).expect("File read failed");
    let target = from_hex(&contents);

    
    // XOR

    // Iterate, get the best coefficient
    let mut xor_vec = vec![0; target.len()];
    let mut tmp_vec = vec![0; target.len()];
    let mut res_vec = vec![0; target.len()];

    let mut bst_coef: f64 = 0.0;
    let mut tmp_coef: f64 = 0.0;
    for n in 0..=255 {
        for x in 0..target.len() {
            xor_vec[x] = n;
        }
        tmp_vec = vec_byte_xor(target.as_slice(), xor_vec.as_slice());
        tmp_coef = englishness(tmp_vec.as_slice());

        if tmp_coef >= bst_coef {
            bst_coef = tmp_coef;
            res_vec = tmp_vec;
        }

    }

    println!("ans: {}", to_hex(res_vec.as_slice()))




}

fn challenge_five(filename: &String) {
    /* Encrypt against repeating key, "ICE" */

    let contents = fs::read_to_string(filename).expect("File read failed");
    let key = "ICE";

    /* Lazy hack */
    let mut mulpt = 0;
    if (contents.len() % key.len()) == 0 {
        mulpt = contents.len() / key.len();
    }
    else {
        mulpt = (contents.len() + key.len()) / key.len();
    }
    let rep_key = key.repeat(mulpt);


    // We want to keep the newline character
    let bytes = contents.as_bytes();
    let xor_key = rep_key.as_bytes();

    let res_xor = vec_byte_xor(bytes, xor_key);
    println!("{}", to_hex(res_xor.as_slice()));
}

fn challenge_six(filename: &String) {

    let raw = fs::read_to_string(filename).expect("File read failed");

    // File has been b64 encoded
    let contents = lib::encoding::b64_to_bytes(&raw);
    let s1 = "this is a test".as_bytes();
    let s2 = "wokka wokka!!!".as_bytes();

    let hd = lib::bitmaths::hamming_distance(s1, s2);
    println!("hamming distance: {}", hd);

    /* For each KEYSIZE, take the first keysize worth of bytes */
}

fn bitwise_hamming_dist(left: &u8, right: &u8) -> u32 {
    return (left ^ right).count_ones()
}

fn hamming_distance(v1: &[u8], v2: &[u8]) -> u32 {
    let mut distance: u32 = 0;

    // Iterate through bytes
    // Can use zip here
    for (b1, b2) in v1.iter().zip(v2){
        distance += bitwise_hamming_dist(b1, b2);
    }

    return distance
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
        "4" => challenge_four(challenge_file),
        "5" => challenge_five(challenge_file),
        "6" => challenge_six(challenge_file),
        _ => println!("You haven't written code for this challenge yet!"),
    }
}
