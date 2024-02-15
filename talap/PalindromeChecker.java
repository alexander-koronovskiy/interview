package talap;

public class PalindromeChecker {
    public static void main(String[] args) {
        String testString = "A man, a plan, a canal, Panama";
        System.out.println(isPalindrome(testString)); // Выведет: true
    }

    public static boolean isPalindrome(String str) {
        // Удаляем пробелы и знаки пунктуации из строки и приводим к нижнему регистру
        String cleanStr = str.replaceAll("[^a-zA-Z0-9]", "");

        // Проверяем, является ли очищенная строка палиндромом
        int left = 0;
        int right = cleanStr.length() - 1;
        while (left < right) {
            if (cleanStr.charAt(left) != cleanStr.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
