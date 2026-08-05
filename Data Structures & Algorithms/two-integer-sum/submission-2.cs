public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            int n = target-nums[i];
            if (map.ContainsKey(n)){
                return new int[2]{map[n], i};
            }
            map[nums[i]] = i;
        }
        return new int[2]{0,1};
    }
}
