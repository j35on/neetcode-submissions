class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*HashMap<Integer, Integer> map = new HashMap<>();
        int l = 0; 
        int r = nums.length -1;
        int difference = 0;
        
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            difference = target - map.get(nums[i]);
            if(map.containsKey(difference) && map.get(difference) != i){
                l = i;
                r = map.get(difference);
                return new int[] {l,r};
            }
        }
        return new int[] {l,r};*/


        HashMap<Integer, Integer> map = new HashMap();

        for(int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            
            if(map.containsKey(difference) && map.get(difference) != i){
                return new int[] {map.get(difference),i};
            }
            map.put(nums[i], i);

        }
        return new int[] {0,1};
    }
}
//[3,2,3]
//{3:0, 2:1}

//target = 6

