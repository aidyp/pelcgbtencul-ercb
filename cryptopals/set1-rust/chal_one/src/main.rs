use std::env;
use std::fs;

/* this crate thing is very useful! */
extern crate hex;
extern crate base64;

fn challenge_one(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    /* get raw bytes */
    let bytes = hex::decode(contents).expect("Decoding failed");

    /* convert to base64 */
    let b64 = base64::encode(&bytes);

    /* print the result */
    println!("base64: {}", b64);
}

fn challenge_two(filename: &String) {
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    /* File contains two hex strings that must be XOR'd together */

    
}

fn main() {

    let args: Vec<String> = env::args().collect();
    let challenge = &args[1];
    let challenge_file = &args[2];

    match challenge.as_str() {
        "1" => challenge_one(challenge_file),
        _ => println!("You haven't written code for this challenge yet!"),
    }
}
