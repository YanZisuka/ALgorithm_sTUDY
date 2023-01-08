use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input).expect("FTRL");

    let input: Vec<&str> = input.trim().split_whitespace().collect();

    let a = match input[0].parse::<i32>() {
        Ok(i) => i,
        Err(_e) => -1,
    };
    let b = match input[1].parse::<i32>() {
        Ok(i) => i,
        Err(_e) => -1,
    };

    println!("{}", a + b)
}
