class Solution {
    // Greatest Common Divisor using recursion
    public int gcd(int num1, int num2) {
        // Make sure num1 is larger than num2
        if (num1 < num2) {
            return gcd(num2, num1);
        }
        // Base case
        if (num2 == 0) {
            return num1;
        }
        return gcd(num2, num1 % num2);
    }
    
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        // Create new array of size 2 to store result
        int[] answer = new int[2];
        
        // Calculate numerator and denominator
        int numerator, denominator;
        
        if (denom1 == denom2) {
            numerator = numer1 + numer2;
            denominator = denom1;
        } else {
            numerator = (numer1 * denom2) + (numer2 * denom1);
            denominator = denom1 * denom2;
        }
        
        // Get absolute values for GCD calculation
        int absNumerator = Math.abs(numerator);
        int absDenominator = Math.abs(denominator);
        
        // Calculate GCD
        int gcdValue = gcd(absNumerator, absDenominator);
        
        // Simplify fraction
        answer[0] = numerator / gcdValue;
        answer[1] = denominator / gcdValue;
        
        return answer;
    }
}