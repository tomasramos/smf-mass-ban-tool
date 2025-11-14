# SMF Mass Email Ban Generator

This project provides a Python script that automatically generates all possible combinations of a username by inserting dots (`.`) between characters and exports a SQL file containing ban entries for **Simple Machines Forum (SMF)**. This helps block Gmail users who can exploit Gmail's dot‑alias feature to bypass bans.

## 🧩 Motivation

Simple Machines Forum (SMF) does not offer an easy method to block all variations of a Gmail address. Gmail treats any number of dots in the local part of an email as equivalent (e.g., `example@gmail.com`, `ex.ample@gmail.com`, and `e.x.a.m.p.l.e@gmail.com` all refer to the same mailbox). Because of this, spammers can evade bans by creating accounts using new dot‑based variants of the same email.

This script solves the problem by generating **every possible dotted variant** of a base string and producing a SQL script that bans all of them at once.

## 🚀 Features

The script:

* Generates all possible dotted combinations for a given base string.
* Appends an optional email suffix (such as `@gmail.com`).
* Assigns all generated emails to the same `id_ban_group`.
* Exports a ready‑to‑run SQL file (`ban_emails.sql`).

## 📂 Project Files

* `smf_mass_email_ban_generator.py` — Main script.
* `ban_emails.sql` — Automatically generated SQL output.
* `README.md` — This file.

## 🔧 Requirements

* Python 3.7 or higher
* Permission to write files in the project directory

## 📌 Usage

1. Open `smf_mass_email_ban_generator.py` and configure:

   * `email_account` → the base string used to generate combinations
   * `email_domain` → the email domain (e.g., `@gmail.com`)
   * `id_ban_group` → an existing ID from the `smf_ban_groups` table

2. Run the script:

   ```bash
   python3 smf_mass_email_ban_generator.py
   ```

3. The script generates a file named `ban_emails.sql`.

4. Import the generated SQL into your SMF database via:

   * phpMyAdmin (SQL tab)
   * MySQL CLI
   * or any MySQL administration tool

## 📝 Example Output

```sql
INSERT INTO smf_ban_items (id_ban_group, email_address)
VALUES
(3, 'spammer@gmail.com'),
(3, 'spamme.r@gmail.com'),
(3, 'spamm.er@gmail.com'),
...
;
```

## ⚠️ Important Notes

* Ensure the `id_ban_group` value exists in your installation.
* Review the SQL file before importing it.
* Depending on the length of the word, this script can generate **thousands** of results.

## 📄 License

This project is free and open to use.

## 📬 Contact

If you want to expand this tool or suggest improvements, feel free to submit an issue or pull request.
