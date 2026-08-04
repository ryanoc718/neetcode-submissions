public class Solution {
    public int[] GetConcatenation(int[] nums) {
        int[] ans = new int[2*(nums.Length)];
        for (int i = 0; i < nums.Length*2; i++){
            if (i >= nums.Length) {
                ans[i] = nums[i-nums.Length];
            }
            else {
                ans[i] = nums[i];
            }
        }
        return ans;
    }
}