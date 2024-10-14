import java.util.Map;

public class UserAuthenticator {

    private final Map<String, String> userMap;

    public UserAuthenticator(Map<String, String> userMap) {
        this.userMap = userMap;
    }

    public int uniqueUserCount() {
        return userMap.size();
    }

    public static void main(String[] args) {
        UserFileReader reader = new UserFileReader();
        Map<String, String> userMap = reader.readUsers("src/user_data.txt");

        PasswordHasher hasher = new PasswordHasher();
        Map<String, String> hashedUserMap = hasher.hashUserPasswords(userMap);

        UserAuthenticator authenticator = new UserAuthenticator(hashedUserMap);

        // Test cases
        System.out.println("Test case 1: " + authenticator.validateLogin("john_doe", "password123")); // should be true
        System.out.println("Test case 2: " + authenticator.validateLogin("john_doe", "wrongpassword")); // should be false

        // User statistics
        System.out.println("Unique User Count: " + authenticator.uniqueUserCount());
    }
}