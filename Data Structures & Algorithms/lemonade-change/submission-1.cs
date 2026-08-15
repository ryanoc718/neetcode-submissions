public class Solution {
    public bool LemonadeChange(int[] bills) {
        Dictionary<int, int> change = new Dictionary<int, int>();
        change.Add(5,0);
        change.Add(10,0);
        for (int i = 0; i < bills.Length; i++) {
            if (bills[i] == 5) {
                change[5] += 1;
            }
            else if (bills[i] == 10) {
                if (change[5] > 0) {
                    change[5] -= 1;
                    change[10] += 1;
                }
                else {
                    return false;
                }
            }
            else {
                if (change[10] > 0 && change[5] > 0) {
                    change[10] -= 1;
                    change[5] -= 1;
                }
                else if (change[5] > 2) {
                    change[5] -= 3;
                }
                else {
                    return false;
                }
            }
        }
        return true;
    }
}