# Answers
---
## Exercise 1:
### Research Task:
When you hash a password, you change its value by adding a key to it. It is very important to in security to do that because of someone steals the password they can still not use the password if they don't also have the key.

Sources: *https://www.techtarget.com/searchdatamanagement/definition/hashing*
### Documentation Task:
I googled and found this website: *https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/security/MessageDigest.html*. This website was also very helpful: *https://gregorycernera.medium.com/generating-a-message-digest-with-java-explained-step-by-step-with-pictures-b9be6c6e5036*.

## Exercise 2:
### File I/O Concepts
`FileReader` makes it possible to read data from a file and `BufferedReader` makes it more effeciant by reading more data at once.

**Example:**
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderExample {

	public static void main(String[] args) {
		String inputFileName = "file.txt";

		try (BufferedReader reader = new BufferedReader(new FileReader(inputFileName))) {
			String line;
			while ((line = reader.readLine()) != null) {
				System.out.println(line + "\n");
			}
		}
                catch (IOException e) {
			e.printStackTrace();
		}
	}

}
```

### Error Handling
Exception handeling is importent to catch bugs and recovering from them without the entire program crashing. `try-with-resources` automatically closes the resource at the end of the block which minimizes errors and ensures effecient resourse management.