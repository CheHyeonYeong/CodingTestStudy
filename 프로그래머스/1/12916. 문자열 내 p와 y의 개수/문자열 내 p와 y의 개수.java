class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toLowerCase(); // 소문자로 변환
        int y = 0;
        int p = 0;
        for(int i = 0; i < s.length(); i++) { // 루프 변수 선언 및 length() 메소드 사용
            if(s.charAt(i) == 'p') p++; // 'p'의 개수를 셈
            else if(s.charAt(i) == 'y') y++; // 'y'의 개수를 셈
        }
        if(y == p) return answer;
        else return !answer;
    }
}
