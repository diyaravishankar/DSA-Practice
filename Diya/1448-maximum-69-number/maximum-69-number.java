class Solution {
    public int maximum69Number (int num) {
        char[] n1=String.valueOf(num).toCharArray();
        for(int i=0;i<n1.length;i++)
        {
            if(n1[i]=='6'){
            n1[i]='9';
            break;
        }
    }
    return Integer.parseInt(new String(n1));
      
    
}
}