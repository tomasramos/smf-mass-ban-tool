from itertools import product

def combinations_with_dots(string_value, suffix=""):
    n = len(string_value)
    positions = n - 1

    for combo in product([False, True], repeat=positions):
        result = string_value[0]
        for i in range(positions):
            if combo[i]:
                result += '.'
            result += string_value[i + 1]
        yield result + suffix


# ---- CONFIG ----

email_account = "emailusername"
email_domain = "@gmail.com"

id_ban_group = 5  # <-- use here the ID from smf_ban_groups table to be used

output_file = "ban_emails.sql"
table_name = "smf_ban_items"   # Change if your installation uses another prefix


# ---- GENERATE ----

values = []

for variant in combinations_with_dots(email_account, email_domain):
    values.append(f"({id_ban_group}, '{variant}')")

sql_text = (
    f"INSERT INTO {table_name} (id_ban_group, email_address)\n"
    f"VALUES\n" + ",\n".join(values) + ";\n"
)

# ---- EXPORT ----

with open(output_file, "w", encoding="utf-8") as f:
    f.write(sql_text)

print(f"File has been generated: {output_file}")
