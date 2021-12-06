//{4: 59, 3: 42, 5: 39, 2: 54, 1: 106})
fn main() {
    let fishes = [(4, 59), (3, 42), (5, 39), (2, 54), (1, 106)];

    let mut sum: i64 = 0;
    for (fish, count) in fishes.iter() {
        sum += step(*fish, 0, 256) * count;
    }
    println!("{}", sum);
}

fn step(fish: i64, cur_step: i64, max_step: i64) -> i64 {
    let delta = -fish - 1;
    if (cur_step - delta) > max_step {
        return 1;
    } else {
        return step(6, cur_step-delta, max_step) + step(8, cur_step-delta, max_step)
    }
}