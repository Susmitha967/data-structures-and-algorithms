class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder s = new StringBuilder();
        Arrays.sort(strs);
        int n = strs.length;
        String f = strs[0];
        String l = strs[n-1];
        for(int i = 0;i < Math.min(f.length(),l.length());i++){
            if(f.charAt(i) != l.charAt(i)){
                return s.toString();
            }else{
                s.append(f.charAt(i));
            }
        }
        return s.toString();
    }
}