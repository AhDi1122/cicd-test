public class BadJava {
    public static void main(String[] args) {
        String pwd = "hardcoded"; // Hardcoded secret
        System.out.println("SQL query:");
        String q = "SELECT * FROM users WHERE id = " + args[0]; // SQL injection
        System.out.println(q);
        String n = null;
        System.out.println(n.length()); // NullPointerException
    }
}

