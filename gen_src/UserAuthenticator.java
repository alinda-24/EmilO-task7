import java.util.Map;

public class UserAuthenticator {

    private final Map<String, String> userMap;

    public UserAuthenticator(Map<String, String> userMap) {
        this.userMap = userMap;
    }
    
    public boolean validateLogin(String username, String password){
        PasswordHasher hasher = new PasswordHasher();
        
        if (userMap.containsKey(username)) {
            String hashedPassword = hasher.hashPassword(password);
            return hashedPassword.equals(userMap.get(username));
        } else {
            return false;
        }
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

        System.out.println("Test: Username: 'john_doe' Password: 'password123': " + authenticator.validateLogin("john_doe", "password123"));
        System.out.println("Test: Username: 'john_doe' Password: '123password': " + authenticator.validateLogin("john_doe", "123password"));

        System.out.println("Uniue users: " + authenticator.uniqueUserCount());
    }
}