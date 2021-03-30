use std::env;
use std::fs;
use std::collections::HashMap;

/* this crate thing is very useful! */

extern crate hex;
extern crate base64;
#[macro_use]
extern crate lazy_static;


/* Lookup Tables */
lazy_static! {
    static ref ENG_FREQ_TABLE: HashMap<u8, f64> = {
        let mut m = HashMap::new();
        m.insert(97, 0.08167);
        /* more inserts to go here */
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

fn to_hex(bytes: Vec<u8>) -> String {
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
    let normal: usize = bytes.len();
    for (_, val) in frequency_table.iter_mut() {
        *val = *val / normal as f64;
    }
    
    
    /* sum of sqrts of products of probability */

    /* 
    let mut coefficient: f64 = 0.0;
    for byte in bytes.iter() {
        match ENG_FREQ_TABLE.get(byte) {
            Some(value) => (),
            None => (),
        }
    }
    */


    let coefficient:f64 = 0.0;
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

    println!("ans: {}", to_hex(res_vec))




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
