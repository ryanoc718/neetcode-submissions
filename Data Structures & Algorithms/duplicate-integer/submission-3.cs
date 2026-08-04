public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> res = new HashSet<int>(nums);
        return (res.Count != nums.Length);
    }
}