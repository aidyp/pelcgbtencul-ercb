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