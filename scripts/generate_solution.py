import os
import sys
import subprocess
import re  # For regex operations
from openai import OpenAI

def main(api_key, branch_name):
    if not api_key:
        print("Error: OpenAI API key is missing.")
        sys.exit(1)
    if not branch_name:
        print("Error: Branch name is missing.")
        sys.exit(1)

    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)

    # Read the new task description
    new_task_path = os.path.join("tasks", "new_task.md")
    if not os.path.exists(new_task_path):
        print(f"Error: New task file not found at {new_task_path}")
        sys.exit(1)
    with open(new_task_path, "r") as f:
        task_description = f.read()

    # Split the new task into exercises
    exercise_chunks = split_task_into_exercises(task_description)

    # Combine all exercises into a single prompt
    prompt = build_prompt(task_description)

    # Call OpenAI API to generate the solution code
    response_content = generate_with_retries(client, prompt, max_retries=3)
    if response_content is None:
        print("Error: Failed to generate solution code after multiple retries.")
        sys.exit(1)

    # Ensure the .hidden_tasks directory exists
    hidden_tasks_dir = os.path.join(".hidden_tasks")
    os.makedirs(hidden_tasks_dir, exist_ok=True)

    # Write the generated code to Java files
    write_generated_code_to_files(hidden_tasks_dir, response_content)

    # Commit and push changes
    commit_and_push_changes(branch_name, hidden_tasks_dir)

def split_task_into_exercises(task_content):
    # Assuming each exercise starts with '#### Exercise'
    exercises = []
    lines = task_content.split('\n')
    current_exercise = []
    in_exercise = False
    for line in lines:
        if line.strip().startswith('#### Exercise'):
            if current_exercise:
                exercises.append('\n'.join(current_exercise))
                current_exercise = []
            in_exercise = True
        if in_exercise:
            current_exercise.append(line)
    if current_exercise:
        exercises.append('\n'.join(current_exercise))
    return exercises

def build_prompt(task_description):
    # Inspirational code snippet for the solution
    inspirational_code = """
    
        // REPOBEE-SANITIZER-SHRED
import java.util.HashMap;

/**
 * A file to analyze text
 * @author Linus Östlund
 */
public class FileTextAnalyzer {
    private FileWordSplitter words;
    private HashMap<String, Integer> wordOccurrences;

    public FileTextAnalyzer(String filename) {
        wordOccurrences = new HashMap<>();

        // Create a new FileWordSplitter (FWS)
        words = new FileWordSplitter(filename);

        // Iterate over all words in the FWS
        for (String word : words.getWords()) {
            // If it is the first occurrence, set value to 1
            word = word.toLowerCase();
            if(!wordOccurrences.containsKey(word)) {
                wordOccurrences.put(word, 1);
            } else {
                // Otherwise, increment the current value
                int oldValue = wordOccurrences.get(word);
                wordOccurrences.put(word, oldValue + 1);

                // Alternate solution:
                // wordOccurrences.merge(word, 1, Integer::sum);
            }
        }
    }

    /**
     * Get the number of words in the text file
     * @return number of words
     */
    public int wordCount() {
        return words.getWords().size();
    }

    /**
     * Get the HashMap containing all word occurrences
     * @return HashMap of all word occurrences
     */
    public HashMap<String, Integer> getWordOccurrences() {
        return wordOccurrences;
    }

    /**
     * Return the number of occurrences of word
     * @param word the word to count occurrences of
     * @return the number of times the word is present in the file
     */
    public int occurrencesOf(String word) {
        word = word.toLowerCase();
        if (!wordOccurrences.containsKey(word)) {
            return 0;
        } else {
            return wordOccurrences.get(word);
        }
    }

    /**
     * A method to find the frequency words in the file
     * @param word the word to get the frequency of
     * @return The number of times the word is present divided by the number of words in the file
     */
    public double frequencyOf(String word) {
        word = word.toLowerCase();
        if (wordOccurrences.containsKey(word)) {
            // If the word is in the corpus, return the frequency of it
            double occurrencesOfWord = occurrencesOf(word);
            double totalAmountOfWords = wordCount();
            return occurrencesOfWord / totalAmountOfWords;
        } else {
            return 0;
        }
    }

    /**
     * Find out how many unique word the input file has
     * @return the size of HashMap's key set
     */
    public int uniqueWordCount() {
        return wordOccurrences.keySet().size();
    }
}




// REPOBEE-SANITIZER-SHRED
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Sample solution for the File Word Splitter class
 * @author Linus Östlund
 */
public class FileWordSplitter {
    private ArrayList<String> words;

    /**
     * The constructor takes the name of a file and iterate over all words.
     * Requires tidy data with not delimiters other than '/n' and ' ' (whitespace)
     * @param filename name of the file. NOTE: has to be in the same folder
     * @throws IOException if something goes wrong while reading the file
     */
    public FileWordSplitter(String filename) {

        // Initialize the ArrayList
        words = new ArrayList<>();

        try {
            // Attempt to open a text file
            BufferedReader file = new BufferedReader(new FileReader(filename));

            // Try to read the first line of the file
            String line = file.readLine();

            // Keep reading while there are lines left
            while (line != null) {
                // NOTE: input has to be tidy and only have whitespace as delimiters
                for (String word : line.split(" ")) {
                    words.add(word);
                }

                // read the next line
                line = file.readLine();
            }

            // Don't forget to close the file!
            file.close();

        // Handle any errors that come up, such as the file not existing
        } catch (IOException e) {
            System.out.println("Something went wrong: " + e.getMessage());
            // Exit the program
            System.exit(1);
        }
    }

    /**
     * Getter for the ArrayList of words
     * @return the whitespace separated words
     */
    public ArrayList<String> getWords() {
        return words;
    }
}



// REPOBEE-SANITIZER-SHRED
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class WordCounter {

    HashMap<String, Integer> wordCounter;
    ArrayList<String> words;

    public WordCounter(File fileName) throws FileNotFoundException {
        Scanner sc = new Scanner(fileName);
        this.words = new ArrayList<>();
        while(sc.hasNextLine()) {
            this.words.add(sc.nextLine());
        }
        sc.close();
    }

    public ArrayList<String> getWords(){
        return this.words;
    }

    public static void main(String[] args) throws FileNotFoundException {
        WordCounter wc = new WordCounter(new File("hamlet.txt"));
        System.out.println(wc.getWords());
    }
}


    """

    additional_instructions = (
        
        "Ensure that each class is entirely self-contained and is not left incomplete. "
        "No part of the next file should be left in the current file. "
        "Ensure that each class is saved in its own appropriately named file, and that there are no 'leftover' initializers or class definitions from subsequent files. "
        "Ensure all imports, public classes, and everything related to the class is included in the appropriate file. "
        "Write NO TEXT beyond the code itself, whatsoever. "
        "IMPORTANT: The response must be plain Java code with no markdown formatting or ```java blocks. "
    )

    prompt = (
        f"Based on the following task description, generate complete and functional Java solutions for each coding exercise. "
        f"The solutions should be well-structured, use meaningful variable names, include necessary comments for clarity, "
        f"and be ready to pass a comprehensive set of unit tests.\n\n"
        f"### Task Description\n\n"
        f"{task_description}\n\n"
        f"### Inspirational Code Snippet\n\n"
        f"{inspirational_code}\n\n"
        f"{additional_instructions}"

        "IMPORTANT: The response must be plain Java code with no markdown formatting or ```java blocks. "
    )

    return prompt

def write_generated_code_to_files(directory, code_content):
    """
    Write generated Java code to appropriate files in the specified directory.
    Handles cases where leftover comments or initializations are present.
    Also ensures that import statements and public class declarations are captured.
    """
    # Split the code content into separate class definitions
    class_blocks = re.split(r'(?:^|\n)(?=public\s+class\s)', code_content)

    for block in class_blocks:
        if not block.strip():
            continue  # Skip empty blocks

        # Extract class name
        class_name_match = re.search(r'public\s+class\s+(\w+)', block)
        if class_name_match:
            class_name = class_name_match.group(1)
        else:
            print(f"Skipping block due to missing class name:\n{block[:50]}")
            continue

        # Clean up the block, removing content after the last closing brace
        cleaned_block = clean_class_block(block)

        # Ensure the necessary imports are included
        cleaned_block = check_and_add_missing_imports(cleaned_block)

        # Write cleaned code to a file
        file_name = f"{class_name}.java"
        file_path = os.path.join(directory, file_name)

        try:
            with open(file_path, "w") as java_file:
                java_file.write(cleaned_block)
            print(f"Successfully wrote {file_name}")
        except IOError as e:
            print(f"Error writing file {file_name}: {e}")

def clean_class_block(block):
    """Ensure the block only contains content until the last closing brace."""
    # Find the position of the last closing brace '}'
    last_closing_brace = block.rfind("}")
    if last_closing_brace != -1:
        # Truncate the block at the last closing brace
        block = block[:last_closing_brace + 1]
    return block

def check_and_add_missing_imports(block):
    """
    Check the class block for missing imports and add necessary imports based on the content.
    """
    required_imports = {
        "List": "import java.util.List;",
        "ArrayList": "import java.util.ArrayList;",
        "Map": "import java.util.Map;",
        "HashMap": "import java.util.HashMap;",
        "Scanner": "import java.util.Scanner;",
        "Set": "import java.util.Set;",
        "HashSet": "import java.util.HashSet;",
        "Random": "import java.util.Random;"
    }

    # Extract existing imports from the block
    existing_imports = re.findall(r'^\s*import .*;', block, re.MULTILINE)

    # Add missing imports
    imports_to_add = []
    for class_name, import_statement in required_imports.items():
        if class_name in block and import_statement not in existing_imports:
            imports_to_add.append(import_statement)

    # Prepend missing imports at the start of the block
    if imports_to_add:
        block = "\n".join(imports_to_add) + "\n\n" + block

    return block

def generate_with_retries(client, prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[
                    {"role": "system", "content": "You are an expert Java programmer and educator."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating solution code: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
    return None

def commit_and_push_changes(branch_name, directory_path):
    try:
        # Ensure we're on the correct branch
        subprocess.run(["git", "checkout", branch_name], check=True)

        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions"], check=True)

        # Add the .hidden_tasks directory to git
        subprocess.run(["git", "add", directory_path], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Add generated solution"], check=True)

        # Push the changes
        subprocess.run(
            ["git", "push", "--set-upstream", "origin", branch_name],
            check=True,
            env={
                **os.environ,
                "GIT_ASKPASS": "echo",
                "GIT_USERNAME": "x-access-token",
                "GIT_PASSWORD": os.getenv("GITHUB_TOKEN")
            }
        )
    except subprocess.CalledProcessError as e:
        print(f"Error committing and pushing changes: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_solution.py <api_key> <branch_name>")
        sys.exit(1)

    api_key = sys.argv[1]
    branch_name = sys.argv[2]
    main(api_key, branch_name)
