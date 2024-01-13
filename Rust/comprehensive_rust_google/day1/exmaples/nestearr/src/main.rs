fn transpose(mut matrix: [[i32; 3]; 3]) -> [[i32; 3]; 3] {
    for i in 0..3 {
        for j in 0..i {
            println!("i: {}, j: {}", i, j);
            let tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }
    matrix
}

fn main() {
    let matrix = [[101, 102, 103], [201, 202, 203], [301, 302, 303]];

    println!("matrix: {:#?}", matrix);
    let transposed = transpose(matrix);
    println!("transposed: {:#?}", transposed);
}
