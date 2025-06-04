class Solution {
    public String answerString(String word, int numFriends) {
        if(numFriends==1){
            return word;
        }
        String res="";
        int l=word.length()-numFriends+1;
        for(int i=0;i<word.length();i++){
            String temp;
            if(i+l<=word.length()){
                temp=word.substring(i,i+l);
                
                            }
            else{
                temp=word.substring(i);
            }
            if(temp.compareTo(res)>0){
                res=temp;
            }

        }
        return res;
    }
}