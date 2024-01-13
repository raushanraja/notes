fn collatz_length(n: u64) -> u32 {
    if n == 1 {
        return 1;
    } else if n % 2 == 0 {
        return 1 + collatz_length(n / 2);
    } else {
        return 1 + collatz_length(3 * n + 1);
    }
}

#[test]
fn test_collatz_length() {
    assert_eq!(collatz_length(27), 112);
    assert_eq!(collatz_length(11), 15);
}

fn main() {
    println!("{:}", collatz_length(11));
}
