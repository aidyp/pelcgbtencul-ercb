extern crate nalgebra as na;
extern crate tranpose;

fn bitwise_hamming_dist(left: &u8, right: &u8) -> u32 {
    return (left ^ right).count_ones();
}

pub fn hamming_distance(v1: &[u8], v2: &[u8]) -> u32 {
    let mut distance: u32 = 0;

    // Iterate through each byte, and perform bitwise hamming on each one
    for (b1, b2) in v1.iter().zip(v2) {
        distance += bitwise_hamming_dist(b1, b2);
    }

    return distance;
}

pub fn group_bytes(bytes: &[u8], groupsize: u32) -> Vec<&[u8]> {
    return bytes.chunks(groupsize as usize).collect();
}

pub fn transpose_bytes(v: Vec<&[u8]>) -> Vec<&[u8]> {
    /* Need to improve this later */

    let blocksize = v[0].len();
    






}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_hamming_distance() {
        let s1 = "this is a test".as_bytes();
        let s2 = "wokka wokka!!!".as_bytes();
        assert_eq!(hamming_distance(s1,s2), 37);
    }

    #[test]
    fn test_group_bytes() {
        let v: Vec<u8> = vec![1,1,1,2,2,2,3,3];
        println!("{:?}", group_bytes(&v, 3));
        
    }

    #[test]
    fn test_transpose() {
        let v: Vec<u8> = vec![1,2,3,4,5,6,7,8,9]
        let v_grp: Vec<&[u8]> = group_bytes(&v, 3);
        println!("{:?}", transpose_bytes(v_grp));
    }
}