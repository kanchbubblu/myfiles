import java.io.*;
 class GFG {
    static String areAllBitsSet(int n)
    {
        if (n == 0)
            return "No";
        while (n > 0)
        {
            if ((n & 1) == 0)
                return "No";
     
            // right shift 'n' by 1
            n = n >> 1;
        }
     
            // all bits are set
            return "Yes";
    }
    public static void main (String[] args) {
    int n = 7;
     
    System.out.println(areAllBitsSet(n));
    }
}
 
 
