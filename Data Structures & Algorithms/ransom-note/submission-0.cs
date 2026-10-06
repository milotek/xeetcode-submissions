public class Solution
{
    public bool CanConstruct(string ransomNote, string magazine)
    {
        int y;
        bool charFound;
        for (int x = 0; x < ransomNote.Length; x++)
        {
            //Console.WriteLine($"Finding {ransomNote[x]}");
            y = 0;
            charFound = false;
            while (y < magazine.Length && !charFound)
            {
                if (magazine[y] == ransomNote[x])
                {
                    charFound = true;
                    //Console.WriteLine($"Found {ransomNote[x]} at position {y}");
                    magazine = magazine.Remove(y, 1);
                }
                else
                {
                    //Console.WriteLine($"Didn't find {ransomNote[x]} at position {y}");
                    y++;
                }
            }
            
            if (!charFound)
            {
                return false;
            }
        }
        return true;
    }
}