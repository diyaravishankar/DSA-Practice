class Solution {
    public boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        StringBuilder res = new StringBuilder();
        for(int i=str.length()-1;i>=0;i--){
            res.append(str.charAt(i));
        }
        if(str.equals(res.toString())){

            return true;

        }
        return false;
    }
}


class Solution {
    public boolean isPalindrome(String s) {
        if(s==" "){
            return true;
        }
        s.toLowerCase();
        StringBuilder str=new StringBuilder("");
        char lower;
        for(int i=0;i<s.length();i++){
            if(Character.isLetter(s.charAt(i))||Character.isDigit(s.charAt(i))){
                lower = Character.toLowerCase(s.charAt(i));
                str.append(lower);
            }
        }
        String reversed = str.reverse().toString();
        String original = str.reverse().toString();
        System.out.println(reversed);
        System.out.println(original);
        if (reversed.equals(original)) {
            
            return true;
        }
        return false;
    }
}