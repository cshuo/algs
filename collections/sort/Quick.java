package collections;

/**
 * Created by cshuo on 2017/2/13.
 * Time NlgN
 */
public class Quick extends Sort{
    public static void sort(int[] a){
        sort(a, 0, a.length-1);
    }

    private static void sort(int[] a, int low, int hi){
        if(low >= hi) return;
        int p = partition(a, low, hi);
        sort(a, low, p-1);
        sort(a, p+1, hi);

    }

    private static int partition(int[] a, int low, int hi){
        int i = low, j = hi+1;
        while (true){
            while(a[++i] <= a[low]){
               if(i==hi) break;
            }
            while(a[--j] >= a[low]){
                if(j==low) break;
            }
            if(i >= j) break;
            swap(a, i, j);
        }
        swap(a, low, j);
        return j;
    }

    public static void main(String[] args){
        int []a = {1,3,4,2,7,5,8,6,0};
        Quick.sort(a);
        Quick.partition(a, 0, a.length-1);
        Quick.printList(a);
    }
}
