
class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        int 곱 = 1;
        for(int num : num_list){
            곱 *= num ; 
            sum += num;
        }
        return (곱 < Math.pow(sum,2) ? 1:0 ) ;
    }
}