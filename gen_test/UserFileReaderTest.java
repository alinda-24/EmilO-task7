package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class UserFileReaderTest {

    private static final String TEST_FILE = "test_users.txt";
    
    @Before
    public void setUp() throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(TEST_FILE))) {
            writer.write("john_doe,password123\n");
            writer.write("jane_doe,pass456\n");
            writer.write("invalid_line_without_comma\n");
            writer.write("user_with_trailing_comma,\n");
            writer.write(",password_without_username\n");
        }
    }
    
    @Test
    public void testReadUsersWithValidFile() {
        UserFileReader reader = new UserFileReader();
        Map<String, String> userMap = reader.readUsers(TEST_FILE);

        assertEquals(2, userMap.size());
        assertEquals("password123", userMap.get("john_doe"));
        assertEquals("pass456", userMap.get("jane_doe"));
    }
    
    @Test
    public void testReadUsersWithNonExistentFile() {
        UserFileReader reader = new UserFileReader();
        Map<String, String> userMap = reader.readUsers("non_existent_file.txt");

        assertTrue(userMap.isEmpty());
    }

    @Test
    public void testReadUsersWithInvalidLines() {
        UserFileReader reader = new UserFileReader();
        Map<String, String> userMap = reader.readUsers(TEST_FILE);

        assertEquals(2, userMap.size());
        assertFalse(userMap.containsKey("invalid_line_without_comma"));
        assertFalse(userMap.containsKey("user_with_trailing_comma"));
        assertFalse(userMap.containsKey(""));
    }
}

import org.junit.Test;
import static org.junit.Assert.assertNotNull;

import java.util.HashMap;
import java.util.Map;

