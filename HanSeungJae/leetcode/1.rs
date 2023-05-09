impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut res = vec![0, 0];

        for (i1, n1) in nums.iter().enumerate() {
            for (i2, n2) in nums[i1 + 1..].iter().enumerate() {
                if n1 + n2 == target {
                    res[0] = i1 as i32;
                    res[1] = (i1 + 1 + i2) as i32;
                }
            }
        }
        return res;
    }
}
