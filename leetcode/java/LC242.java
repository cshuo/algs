package leetcode;

/**
 * Created by cshuo on 2017/2/13.
 * Time: O(n)
 */
public class LC242{
    public boolean isAnagram(String s, String t) {
        int [] countSign = new int[26];
        for(int i = 0; i < s.length(); i++){
            countSign[s.charAt(i) - 'a'] += 1;
        }
        for(int i=0; i < t.length(); i++){
            if(--countSign[t.charAt(i) - 'a'] <0)
                return false;
        }
        return t.length() == s.length();
    }
}
