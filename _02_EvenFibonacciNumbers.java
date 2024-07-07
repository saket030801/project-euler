public class _02_EvenFibonacciNumbers {
    public static void main(String[] args) {
        long n = 4000000;

        long a=0, b=1, sum=0;

        while (true){
            long temp = a+b;
            if(temp>n)
                break;

            if(temp%2==0)
                sum+=temp;
            a=b;
            b=temp;
        }

        System.out.println(sum);
    }
}
