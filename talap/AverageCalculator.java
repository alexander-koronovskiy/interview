package talap;

import java.util.Scanner;

public class AverageCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Введите количество чисел: ");
        int count = scanner.nextInt();
        
        int[] numbers = new int[count];
        int sum = 0;
        
        for (int i = 0; i < count; i++) {
            System.out.print("Введите число " + (i+1) + ": ");
            numbers[i] = scanner.nextInt();
            sum += numbers[i];
        }
        
        double average = (double) sum / count;
        
        System.out.println("Среднее значение: " + average);
        
        scanner.close();
    }
}
