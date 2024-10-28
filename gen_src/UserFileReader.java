import java.util.Map;
import java.util.HashMap;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class UserFileReader {

    public static Map<String, String> readUsers(String filename) {
        HashMap<String, String> userMap = new HashMap<String, String>();
        
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))){
            String line;
            while ((line = reader.readLine()) != null){
                String[] userDetails = line.split(",");
                if (userDetails.length == 2) {
                    userMap.put(userDetails[0].trim(), userDetails[1].trim()); // Adding trim() to remove potential whitespace
                } else {
                    System.err.println("Skipping invalid line: " + line);
                }
            }
        } catch (IOException e) {
            System.err.println("Error!");
            System.err.println("Couldn't find file 'user_data.txt");
            System.err.println(e.getMessage());
        }

        return userMap;
    }
}