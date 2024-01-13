use core::f64;

fn magnitude(point: &[f64; 3]) -> f64 {
    f64::sqrt(f64::powi(point[0], 2) + f64::powi(point[1], 2) + f64::powi(point[2], 2))
}

fn normalize(point: &mut [f64; 3]) {
    let magni = magnitude(point);

    for i in point {
        *i = *i / magni;
    }
}

fn main() {
    println!(
        "Magnitude of a unit vector: {}",
        magnitude(&[2.0, 1.0, 2.0])
    );

    let mut v = [1.0, 2.0, 9.0];
    println!("Magnitude of {v:?}: {}", magnitude(&v));
    normalize(&mut v);
    println!("Magnitude of {v:?} after normalization: {}", magnitude(&v));
}
