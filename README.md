[README.md](https://github.com/user-attachments/files/32160302/README.md)
# Task 3: Random Password Generator

**Internship:** Oasis Infobyte SIP (OIBSIP)  
**Domain:** Python Development  
**Task:** Task 3 – Random Password Generator

---

## 🎯 Overview
In today's digital landscape, strong and unpredictable passwords are a critical defense against credential stuffing, brute-force attacks, and unauthorized access.

This project is an interactive, secure Python command-line password generator built for the **Oasis Infobyte SIP** internship. It allows users to create customized, highly secure passwords tailored to specific length and character type criteria.

Unlike standard generators that rely on Python's pseudo-random `random` module, this implementation uses Python's built-in **`secrets`** module to ensure **cryptographically secure random generation** (CSPRNG) suitable for managing security-sensitive credentials.

---

## 🔒 Security & Architecture Highlights

- **Cryptographically Secure PRNG:** Uses Python's standard `secrets` library (introduced in PEP 506), which accesses the operating system's highest-quality entropy source (`/dev/urandom` on Unix-like systems, `CryptGenRandom` / `BCryptGenRandom` on Windows).
- **Guaranteed Character Representation:** Automatically injects at least one character from every selected category before filling the remaining length, ensuring full compliance with the user's requirements.
- **Cryptographic Shuffling:** Shuffles character positions using `secrets.SystemRandom().shuffle()` so that initial character insertions cannot be predicted based on category selection order.
- **Strict Diversity Enforcement:** Requires a minimum of 2 character types and a minimum length of 8 characters to prevent weak or trivially crackable passwords.

---

## 🔠 Supported Character Types

| Option | Character Type | Sample Characters |
| :---: | :--- | :--- |
| **1** | Uppercase Letters | `A, B, C, ..., Z` |
| **2** | Lowercase Letters | `a, b, c, ..., z` |
| **3** | Numbers | `0, 1, 2, ..., 9` |
| **4** | Special Symbols | `!, @, #, $, %, ^, &, *, (, ), ...` |

---

## ✨ Features Checklist

- [x] **Enforced Minimum Length:** Prompts user for desired length with strict enforcement of $\ge 8$ characters.
- [x] **Character Type Selection:** Interactive menu to pick uppercase, lowercase, numbers, and symbols in any combination.
- [x] **Diversity Requirement:** Enforces selection of at least 2 distinct character types.
- [x] **Cryptographically Secure:** Powered by the `secrets` module instead of `random`.
- [x] **Guaranteed Coverage:** Guarantees at least one character from each chosen type.
- [x] **Secure Random Shuffling:** Shuffles the final string to eliminate predictable character placement.
- [x] **Input Validation:** Comprehensive error handling for invalid lengths, non-integer inputs, duplicate choices, and out-of-range options.
- [x] **Multi-Generation Loop:** Allows generating multiple passwords repeatedly without restarting the script.

---

## 💻 Sample Output

```text
=============================================
      RANDOM PASSWORD GENERATOR
=============================================

Enter password length (minimum 8): 16

Choose character types:
1. Uppercase Letters (A-Z)
2. Lowercase Letters (a-z)
3. Numbers (0-9)
4. Symbols (!, @, #, etc.)

Enter your choices (Example: 1234 or 23): 1234

=============================================
GENERATED PASSWORD:
mK#9$eT2!wX8^vL1
=============================================

Do you want to generate another password? (Y/N): n

Thank you for using the Password Generator.
Stay secure!
```

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd "python task-3 RandomPasswordGenetor"
   ```
3. Run the script:
   ```bash
   python main.py
   ```
