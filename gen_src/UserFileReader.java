import java.util.Map;
import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class UserFileReader {

    public Map<String, String> readUsers(String filename) {
        HashMap<String, String> users = new HashMap<String, String>();
        
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))){
            String line;
            while ((line = reader.readLine()) != null){
                String[] userDetails = line.split(",");
                if (userDetails.length == 2) {
                    users.put(userDetails[0].trim(), userDetails[1].trim()); // Adding trim() to remove potential whitespace
                } else {
                    System.err.println("Skipping invalid line: " + line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return users;
    }
}