package talap;

public class NumberReverser {
    public static void main(String[] args) {
        int number = -12345;
        System.out.println(reverseNumber(number)); // Выведет: 54321
    }

    public static int reverseNumber(int num) {
        int reversed = 0;
        // Обработка отрицательных чисел
        boolean isNegative = num < 0;
        if (isNegative) {
            num = -num;
        }
        // Переворачивание цифр
        while (num > 0) {
            int digit = num % 10;
            if (reversed == 0 && digit == 0) {
                // Пропускаем нули в конце числа
            } else {
                reversed = reversed * 10 + digit;
            }
            num = num / 10;
        }
        return isNegative ? -reversed : reversed;
    }
}
