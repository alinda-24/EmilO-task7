package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class UserAuthenticatorTest {

    @Test
    public void testUniqueUserCount() {
        Map<String, String> userMap = new HashMap<>();
        userMap.put("user1", "hash1");
        userMap.put("user2", "hash2");
        
        UserAuthenticator authenticator = new UserAuthenticator(userMap);
        assertEquals(2, authenticator.uniqueUserCount());
    }
}

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

