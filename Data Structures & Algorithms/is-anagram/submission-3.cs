public class Solution {
    public bool IsAnagram(string s, string t) {
        string ss = new string(s.OrderBy(c => c).ToArray());
        string tt = new string(t.OrderBy(c => c).ToArray());
        return ss == tt;
    }
}
