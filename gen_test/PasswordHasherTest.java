package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class PasswordHasherTest {

    @Test
    public void testHashPasswordNotNull() {
        PasswordHasher hasher = new PasswordHasher();
        String hashedPassword = hasher.hashPassword("examplePassword");
        
        assertNotNull(hashedPassword);
    }

    @Test
    public void testHashUserPasswords() {
        PasswordHasher hasher = new PasswordHasher();
        Map<String, String> userMap = new HashMap<>();
        userMap.put("user1", "password1");
        userMap.put("user2", "password2");
        
        Map<String, String> hashedMap = hasher.hashUserPasswords(userMap);
        assertEquals(2, hashedMap.size());
        assertNotNull(hashedMap.get("user1"));
        assertNotNull(hashedMap.get("user2"));
    }
}

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;

