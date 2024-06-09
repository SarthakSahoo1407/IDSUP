import java.sql.*;
import java.io.*;

public class myjdbcproj {
    static Connection con = null;
    static Statement stmt = null;
    static BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String args[]) throws IOException {
        try {
            Class.forName("oracle.jdbc.driver.OracleDriver");
            String conurl = "jdbc:oracle:thin:@172.17.144.110:1521:ora11g";
            con = DriverManager.getConnection(conurl, "cseu2141019110", "cseu2141019110");
            stmt = con.createStatement();
            int choice_variable;
            do {
                System.out.println("\n\n***** Banking Management System*****");
                System.out.println("1. Show Customer Records");
                System.out.println("2. Add Customer Record");
                System.out.println("3. Delete Customer Record");
                System.out.println("4. Update Customer Information");
                System.out.println("5. Show Account Details of a Customer");
                System.out.println("6. Show Loan Details of a Customer");
                System.out.println("7. Deposit Money to an Account");
                System.out.println("8. Withdraw Money from an Account");
                System.out.println("9. Exit");
                System.out.println("Enter your choice(1-9):");

                choice_variable = Integer.parseInt(reader.readLine());
                
                switch (choice_variable) {
                    case 1:
                        showCustomerRecords();
                        break;
                    case 2:
                        addCustomerRecord();
                        break;
                    case 3:
                        deleteCustomerRecord();
                        break;
                    case 4:
                        updateCustomerRecord();
                        break;
                    case 5:
                        showAccountDetails();
                        break;
                    case 6:
                        showLoanDetails();
                        break;
                    case 7:
                        depositMoney();
                        break;
                    case 8:
                        withdrawMoney();
                        break;
                    case 9:
                        // Exit the menu
                        break;
                    default:
                        System.out.println("Invalid choice! Please enter a number from 1 to 9.");
                        break;
                }
            } while (choice_variable != 9);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                if (stmt != null)
                    stmt.close();
                if (con != null)
                    con.close();
                reader.close();
            } catch (SQLException | IOException e) {
                e.printStackTrace();
            }
        }
    }

    static void showCustomerRecords() {
        try {
            String query = "SELECT * FROM CUSTOMER";
            ResultSet rs = stmt.executeQuery(query);
            System.out.println("Customer Records:");
            while (rs.next()) {
                System.out.println("Cust No: " + rs.getString("CUST_NO") + ", Name: " + rs.getString("NAME") +
                        ", Phone No: " + rs.getString("PHONE_NO") + ", City: " + rs.getString("CITY"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    static void addCustomerRecord() {
        try {
            System.out.println("Enter Customer No:");
            String custNo = reader.readLine();
            System.out.println("Enter Name:");
            String name = reader.readLine();
            System.out.println("Enter Phone No:");
            String phoneNo = reader.readLine();
            System.out.println("Enter City:");
            String city = reader.readLine();
            String query = "INSERT INTO CUSTOMER (CUST_NO, NAME, PHONE_NO, CITY) VALUES ('" + custNo + "', '" +
                    name + "', '" + phoneNo + "', '" + city + "')";
            int rowsAffected = stmt.executeUpdate(query);
            if (rowsAffected > 0) {
                System.out.println("Customer record added successfully!");
                showCustomerRecords();
            } else {
                System.out.println("Failed to add customer record.");
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    static void deleteCustomerRecord() {
        try {
            System.out.println("Enter Customer No to delete:");
            String custNo = reader.readLine();
            String query = "DELETE FROM CUSTOMER WHERE CUST_NO = '" + custNo + "'";
            int rowsAffected = stmt.executeUpdate(query);
            if (rowsAffected > 0) {
                System.out.println("Customer record deleted successfully!");
                showCustomerRecords();
            } else {
                System.out.println("Customer record not found or deletion failed.");
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    static void updateCustomerRecord() {
        try {
            System.out.println("Enter Customer No to update:");
            String custNo = reader.readLine();
            System.out.println("Enter 1: For Name 2: For Phone no 3: For City to update:");
            int choice = Integer.parseInt(reader.readLine());
            String columnName = "";
            switch (choice) {
                case 1:
                    columnName = "NAME";
                    break;
                case 2:
                    columnName = "PHONE_NO";
                    break;
                case 3:
                    columnName = "CITY";
                    break;
                default:
                    System.out.println("Invalid choice for update.");
                    return;
            }
            System.out.println("Enter new value:");
            String newValue = reader.readLine();
            String query = "UPDATE CUSTOMER SET " + columnName + " = '" + newValue + "' WHERE CUST_NO = '" + custNo + "'";
            int rowsAffected = stmt.executeUpdate(query);
            if (rowsAffected > 0) {
                System.out.println("Customer record updated successfully!");
                showCustomerRecords();
            } else {
                System.out.println("Customer record not found or update failed.");
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    static void showAccountDetails() {
        try {
            System.out.println("Enter Customer No:");
            String custNo = reader.readLine();
            String query = "SELECT * FROM ACCOUNT WHERE CUST_NO = '" + custNo + "'";
            ResultSet rs = stmt.executeQuery(query);
            System.out.println("Account Details for Customer " + custNo + ":");
            while (rs.next()) {
                System.out.println("Account No: " + rs.getString("ACCOUNT_NO") + ", Type: " + rs.getString("TYPE") +
                        ", Balance: " + rs.getString("BALANCE") + ", Branch Code: " + rs.getString("BRANCH_CODE"));
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    static void showLoanDetails() {
        try {
            System.out.println("Enter Customer No:");
            String custNo = reader.readLine();
            String query = "SELECT LOAN.*, BRANCH.BRANCH_NAME, BRANCH.BRANCH_CITY " +
                    "FROM LOAN JOIN BRANCH ON LOAN.BRANCH_CODE = BRANCH.BRANCH_CODE " +
                    "WHERE LOAN.CUST_NO = '" + custNo + "'";
            ResultSet rs = stmt.executeQuery(query);
            System.out.println("Loan Details for Customer " + custNo + ":");
            boolean found = false;
            while (rs.next()) {
                found = true;
                System.out.println("Loan No: " + rs.getString("LOAN_NO") + ", Amount: " + rs.getString("AMOUNT") +
                        ", Branch Code: " + rs.getString("BRANCH_CODE") + ", Branch Name: " + rs.getString("BRANCH_NAME") +
                        ", Branch City: " + rs.getString("BRANCH_CITY"));
            }
            if (!found) {
                System.out.println("No loan details found for Customer " + custNo);
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    static void depositMoney() {
        try {
            System.out.println("Enter Account No:");
            String accountNo = reader.readLine();
            System.out.println("Enter Amount to deposit:");
            double amount = Double.parseDouble(reader.readLine());
            String query = "UPDATE ACCOUNT SET BALANCE = BALANCE + " + amount + " WHERE ACCOUNT_NO = '" + accountNo + "'";
            int rowsAffected = stmt.executeUpdate(query);
            if (rowsAffected > 0) {
                System.out.println("Money deposited successfully!");
                showAccountDetails();
            } else {
                System.out.println("Account not found or deposit failed.");
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }

    static void withdrawMoney() {
        try {
            System.out.println("Enter Account No:");
            String accountNo = reader.readLine();
            System.out.println("Enter Amount to withdraw:");
            double amount = Double.parseDouble(reader.readLine());
            String query = "UPDATE ACCOUNT SET BALANCE = BALANCE - " + amount + " WHERE ACCOUNT_NO = '" + accountNo + "'";
            int rowsAffected = stmt.executeUpdate(query);
            if (rowsAffected > 0) {
                System.out.println("Money withdrawn successfully!");
                showAccountDetails();
            } else {
                System.out.println("Account not found or insufficient balance.");
            }
        } catch (SQLException | IOException e) {
            e.printStackTrace();
        }
    }
}
