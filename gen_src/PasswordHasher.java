import java.util.Map;
import java.util.HashMap;
import java.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.nio.charset.StandardCharsets;

public class PasswordHasher {

    public String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes(StandardCharsets.UTF_8));
            return Base64.getEncoder().encodeToString(hash);
        } 
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException("Error hashing password", e);
        }
    }

    public Map<String, String> hashUserPasswords(Map<String, String> userMap) {
        HashMap<String, String> hashedUserMap = new HashMap<String, String>();
        for (Map.Entry<String, String> entry : userMap.entrySet()) {
            String username = entry.getKey();
            String hashedPassword = hashPassword(entry.getValue());
            hashedUserMap.put(username, hashedPassword);
        }
        return hashedUserMap;
    }
}