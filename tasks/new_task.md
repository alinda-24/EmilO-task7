## 🛡️ Password Management System

Welcome to your next project, where you'll explore password management and hashing. This exercise will integrate using documentation, reading from files, and utilizing Java's `HashMap` class to create a basic password management system. By the end of this assignment, you'll have a deeper understanding of how password systems work, including the importance of hashing passwords for security.

### 🚀 Learning Goals

1. **Using Documentation:**
   - Navigate and comprehend Java documentation and community resources.
   - Integrate understanding into the implementation of Java classes.

2. **Reading from a Text File:**
   - Set up file paths and manage file streams.
   - Employ `FileReader` and `BufferedReader` for efficient file I/O.

3. **Using the `HashMap` Class:**
   - Create and manipulate `HashMap` objects for data storage and retrieval.
   - Implement operations on key-value pairs and understand hash functions.

---

### 📋 Task Overview

You'll create a simple password management system that reads user data from a file, hashes the passwords, and then verifies login attempts. Follow the exercises below to build and test your application progressively.

---

### Exercise 1: 📚 Understanding Password Hashing (Theoretical)

1. **Research Task:**  
   Explain the concept of password hashing and its importance in security. Why is it crucial to hash passwords instead of storing them as plain text? Include sources or documentation you referenced.

2. **Documentation Task:**  
   Locate and explore the Java `MessageDigest` class used for hashing. Provide a brief explanation of how you found the necessary information and how `MessageDigest` can be used.

---

### Exercise 2: 📑 File Reading Fundamentals (Theoretical)

1. **File I/O Concepts:**  
   Describe the process of reading a text file in Java. What are `BufferedReader` and `FileReader`, and why would you use them? Include examples from the documentation.

2. **Error Handling:**  
   Explain the importance of exception handling when working with file I/O in Java. How does `try-with-resources` help in managing resources efficiently?

---

### Exercise 3: 🖥️ Implementing File Reading

1. **File Setup:**  
   Create a file named `user_data.txt` in your project's `src` folder. Each line should contain a username and password separated by a comma (e.g., `john_doe,password123`).

2. **Java Class:**  
   Implement a class `UserFileReader` with a method `public Map<String, String> readUsers(String filename)`. This method should read the file and return a `HashMap` with usernames as keys and passwords as values.

---

### Exercise 4: 🔒 Hashing Passwords

1. **Hashing Method:**  
   Extend `UserFileReader` or create a new class named `PasswordHasher`. Implement the hashing of passwords using `MessageDigest`. Create a method `public String hashPassword(String password)` that returns the hashed version of the input password.

2. **Integration Task:**  
   Modify your previous code to store hashed passwords instead of plain text in your `HashMap`.

```java
public String hashPassword(String password) {
    try {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] hash = md.digest(password.getBytes(StandardCharsets.UTF_8));
        return Base64.getEncoder().encodeToString(hash);
    } catch (NoSuchAlgorithmException e) {
        throw new RuntimeException("Error hashing password", e);
    }
}
```

---

### Exercise 5: 🔑 Validating Credentials

1. **Validation Method:**  
   Implement a method `public boolean validateLogin(String username, String password)` in a new class `UserAuthenticator`. This should check whether the hashed password for a given username matches the input password after hashing.

2. **Testing:**  
   Create a few test cases to ensure `validateLogin` works correctly. Use assertions or a simple main method to output test results to the console.

---

### Exercise 6: 📊 User Statistics & Security Evaluation

1. **Statistics Method:**  
   Add a method `public int uniqueUserCount()` in your `UserAuthenticator` class to return the number of unique usernames in your system.

2. **Security Evaluation:**  
   Analyze your password management system. Identify potential security flaws or areas of improvement and document strategies for addressing these issues. Consider enhancements like salts, password policy enforcement, etc.

---

## ✏️ Submission Checklist
- [ ] Detailed explanation for hashing and file I/O (Exercises 1 & 2).
- [ ] `UserFileReader` and `PasswordHasher` classes implemented correctly (Exercises 3 & 4).
- [ ] Passwords are properly hashed and validated (Exercise 5).
- [ ] Unique user count functionality and security evaluation completed (Exercise 6).

### 🌟 Bonus Challenge
- Implement a salts mechanism to enhance password security. Explain its implementation and benefits.

Tackle this task with attention to detail and creativity. Best of luck, and secure those passwords! 🧑‍💻✨