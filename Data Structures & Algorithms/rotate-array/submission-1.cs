public class Solution
{
    public void Rotate(int[] nums, int k)
    {
        k = k % nums.Length;
        
        int[] oldnums = (int[])nums.Clone();
        
        for (int x = 0; x < nums.Length; x++)
        {
            nums[(x + k) % nums.Length] = oldnums[x];
        }
    }
}