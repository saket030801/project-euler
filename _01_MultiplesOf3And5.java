public class _01_MultiplesOf3And5 {
    public static void main(String[] args) {
        int n=1000;
        int sum=0;

        for(int i=0 ; i<1000 ; i++){
            if(i%3==0 || i%5==0)
                sum+=i;
        }

        System.out.println(sum);

    }
}
