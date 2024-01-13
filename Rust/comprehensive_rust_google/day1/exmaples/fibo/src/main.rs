fn fibo(n: i32) -> i32 {
    if n <= 2 {
        return 2;
    } else {
        return n * fibo(n - 1);
    }
}

fn main() {
    println!("Hello, world!");
    println!("{:}", fibo(9));
}
