use std::io;

fn fibonacci_dp(num: usize) -> usize {
    let mut dp: Vec<usize> = Vec::new();

    while dp.len() < num {
        if dp.len() < 2 {
            dp.push(1);
        } else {
            dp.push(dp[dp.len() - 2] + dp[dp.len() - 1]);
        }
    }

    dp[dp.len() - 1]
}

fn main() {
    loop {
        let mut input = String::new();

        io::stdin().read_line(&mut input).expect("FTRL");

        let input = match input.trim().parse::<usize>() {
            Ok(num) => {
                if num == 0 {
                    println!("0");
                    break;
                }
                num
            }
            Err(_e) => continue,
        };

        println!("{}", fibonacci_dp(input));
        break;
    }
}
