import java.util.Map;
import java.util.HashMap;
import java.util.Set;

public class PasswordHasher {

    public String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes(StandardCharsets.UTF_8));
            return Base64.getEncoder().encodeToString(hash);
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }

    public Map<String, String> hashUserPasswords(Map<String, String> userMap) {
        Map<String, String> hashedMap = new HashMap<>();
        for (Map.Entry<String, String> entry : userMap.entrySet()) {
            hashedMap.put(entry.getKey(), hashPassword(entry.getValue()));
        }
        return hashedMap;
    }
}