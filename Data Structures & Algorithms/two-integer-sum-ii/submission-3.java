class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length-1;

        while(left<right){
            System.out.println(left + " index" +  right);
            System.out.println(numbers[left] +" actual value " + numbers[right]);
            if(numbers[left] + numbers[right] == target){
                return new int[] {left+1,right+1};
            }
            if(numbers[left] > numbers[right] && numbers[left] + numbers[right] > target){
                System.out.println(left + " " +  right);
                System.out.println(numbers[left] +" " + numbers[right]);
                left++;
            }
            if(numbers[left] > numbers[right] && numbers[left] + numbers[right] < target){
                right--;
            }
            if(numbers[left] < numbers[right] && numbers[left] + numbers[right] < target){
                left++;
            }
            else{
                right--;
            }
        }
        System.out.println("help");
        return numbers;
    }
}
