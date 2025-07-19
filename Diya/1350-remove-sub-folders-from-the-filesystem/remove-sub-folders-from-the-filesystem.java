class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);
        List<String> result=new ArrayList<>();
        for(String i:folder){
            if(result.isEmpty()){
                result.add(i);
            }
            else{
                String prev=result.get(result.size()-1);
                if(i.startsWith(prev)&& i.length()>prev.length() && i.charAt(prev.length())=='/'){
                    continue;
                }
                else{
                    result.add(i);
                }
            }
        }
        return result;
    }
}