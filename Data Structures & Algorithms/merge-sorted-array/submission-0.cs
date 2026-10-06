public class Solution
 {
    public void Merge(int[] nums1, int m, int[] nums2, int n)
     {
        int y = 0;
        for (int x = m; x < m+n; x++)
        {
            nums1[x] = nums2[y];
            //Console.WriteLine($"{nums1[x]} replaced by {nums2[y]}");
            y++;
        }
        Array.Sort(nums1);
        Console.Write(nums1);
    }
}