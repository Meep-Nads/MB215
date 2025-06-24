data = [
    ["Name", "Department", "Role", "E-Mail", "ID"],
    ["Lottie Curry", "Environmental Health & Safety", "Environmental Officer", "enviro@wlu.ca", "468372922"],
    ["Byro Castro", "Campus Facilities Operations", "Operations Manager", "campusaccesscontrol@wlu.ca", "589683129"],
    ["Kent Mcgee", "Campus Security Services", "Special Constable", "campussecurity@wlu.ca", "192438056"],
    ["Clarie Whitaker", "Environmental Health & Safety", "HR", "hr@wlu.ca", "852870501"],
    ["Deborah MacLatchy", "Campus Facilities Operations", "Special Constable", "campusaccesscontrol@wlu.ca", "674263928"],
    ["Issac Collier", "Campus Transit Office", "Communications Officer", "commstrans@wlu.ca", "909562679"],
    ["Jeffery Norris", "Emergency Management Services", "IT Support", "emergserv@wlu.ca", "616783760"],
    ["Carlos Jamison", "Custodial Services", "Custodian", "custserv@wlu.ca", "567421917"]
]

# Determine column widths
col_widths = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

for i, row in enumerate(data):
    row_str = " | ".join(f"{str(val).ljust(col_widths[j])}" for j, val in enumerate(row))
    print(row_str)
    if i == 0:
        print("-+-".join("-" * w for w in col_widths))