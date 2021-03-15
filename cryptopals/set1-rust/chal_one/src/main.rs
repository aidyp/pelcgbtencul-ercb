use std::env;
use std::fs;



fn main() {
    let filename = "challenge.txt";
    let contents = fs::read_to_string(filename).expect("Something went wrong!");

    println!("Text: {}", contents);
}
