public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> res = new HashSet<int>();
        for (int i = 0; i < nums.Length; i++){
            if (res.Contains(nums[i])) {
                return true;
            }
            res.Add(nums[i]);
        }
        return false;
    }
}