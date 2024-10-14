package test;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class TestRunner {
    
    public static void main(String[] args) {
        
        Result result = JUnitCore.runClasses(
                UserFileReaderTest.class, 
                PasswordHasherTest.class, 
                UserAuthenticatorTest.class
        );

        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }

        System.out.println(result.wasSuccessful());
    }
}