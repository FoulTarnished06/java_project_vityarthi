# Banking & Transaction Simulation System (Java)

A modular, robust **Banking and Transaction Simulation System** implemented in pure Core Java (JDK 17/21/25 LTS compatible, zero external runtime dependencies). Designed specifically for college computer science courses, academic project submissions, and viva demonstrations.

---

## 🌟 Key Features

1. **Object-Oriented Architecture (OOP):**
   - **Abstraction & Polymorphism:** Abstract base class `Account` with polymorphic implementations `SavingsAccount` and `CheckingAccount`.
   - **Encapsulation:** Synchronized mutator methods with state protection and validation guards.
   - **Inheritance:** Shared transaction logging, customer metadata, and balance handling.
2. **Real-World Financial Business Logic:**
   - **Savings Account:** Enforces a minimum balance rule ($100.00) and supports annual interest calculation (4.5% p.a.).
   - **Checking Account:** Overdraft protection up to $500.00 credit with automatic $15.00 overdraft fee application.
3. **Atomic Fund Transfers & Rollback:**
   - Inter-account transfers operate atomically. If a transfer fails mid-way, the sender balance is automatically rolled back.
4. **Security & Cryptography:**
   - 4-digit PIN authentication protected by salted SHA-256 cryptographic hashing.
5. **Persistent Storage (Zero Configuration):**
   - Human-readable CSV storage (`data/accounts.csv` and `data/transactions.csv`) ensuring account state and transaction ledgers persist across restarts.
6. **Dual Portal Experience:**
   - **Customer Portal:** Check balance, deposit cash, withdraw funds, transfer to another account, view transaction statements.
   - **Bank Manager / Admin Portal:** View all registered accounts, total bank liquidity/reserves, execute monthly interest distribution, and freeze/unfreeze accounts.
7. **Quick Demo Seeder:**
   - Built-in option to automatically seed sample accounts and transactions for quick viva/demo presentations.

---

## 📂 Project Structure

```
java_project/
├── src/
│   └── com/bank/
│       ├── Main.java                          # Interactive CLI application
│       ├── TestRunner.java                    # Automated verification & test suite
│       ├── model/
│       │   ├── Account.java                   # Abstract base account class
│       │   ├── SavingsAccount.java            # Savings account logic (min balance, interest)
│       │   ├── CheckingAccount.java           # Checking account logic (overdraft)
│       │   ├── Customer.java                  # Customer profile model
│       │   ├── Transaction.java               # Immutable transaction model
│       │   └── TransactionType.java           # Transaction type enumeration
│       ├── service/
│       │   ├── BankService.java               # Core banking business logic
│       │   └── SecurityUtil.java              # Salted SHA-256 PIN hasher
│       ├── repository/
│       │   ├── AccountRepository.java         # Repository interface
│       │   └── FileAccountRepository.java     # CSV file persistence engine
│       └── exception/
│           ├── BankingException.java          # Base checked domain exception
│           ├── InsufficientFundsException.java
│           ├── AccountNotFoundException.java
│           ├── InvalidPinException.java
│           └── OverdraftExceededException.java
├── data/                                      # Persistent storage directory
│   ├── accounts.csv
│   └── transactions.csv
├── report/
│   ├── report_template.html                   # Formatted academic project report
│   ├── generate_pdf.py                        # Headless PDF compilation script
│   ├── generate_pdf.bat                       # 1-click batch script to compile PDF
│   └── Banking_System_Project_Report.pdf      # Compiled Project Report PDF
├── compile_and_run.bat                        # 1-click Windows compilation & launch
├── run_tests.bat                              # 1-click test suite runner
└── README.md                                  # Project documentation
```

---

## 🚀 How to Compile and Run

### Option 1: Double-Click Batch File (Easiest for Windows)
Simply double-click:
```
compile_and_run.bat
```

### Option 2: Command Line (PowerShell / Terminal)
1. **Compile the source files:**
   ```powershell
   javac -d bin (Get-ChildItem -Recurse -Filter *.java | Select-Object -ExpandProperty FullName)
   ```
2. **Run the application:**
   ```powershell
   java -cp bin com.bank.Main
   ```

---

## 🧪 Running the Automated Test Suite

To run the automated verification suite (11 unit and integration scenarios covering minimum balance limits, overdraft fees, atomic rollback, PIN hashing, and file persistence):

```powershell
java -cp bin com.bank.TestRunner
```
*(Or double-click `run_tests.bat`)*

---

## 🔑 Default Credentials & Quick Demo

- **Admin / Manager Portal Passcode:** `admin123`
- **Quick Demo Seeder:** Option `[4]` in the main menu automatically sets up:
  - **Savings Account:** `ACC-1001` (PIN: `1234`, Holder: Alice Johnson)
  - **Checking Account:** `ACC-1002` (PIN: `4321`, Holder: Bob Smith)

---

## 📄 Academic Project Report PDF

A complete, 14+ page academic project report has been compiled and saved to:
`report/Banking_System_Project_Report.pdf`

### Customizing the Report with Your Details:
1. Open `report/report_template.html` in any text editor.
2. Search for `[Student Name]`, `[Roll Number]`, `[College / University Name]`, etc., and replace them with your personal information.
3. Recompile the PDF by double-clicking `report/generate_pdf.bat` or running:
   ```powershell
   python report/generate_pdf.py
   ```
