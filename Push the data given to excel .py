import openpyxl

def push_data_to_excel(data):
    # Create a new Excel file
    excel_file = openpyxl.Workbook()

    # Create a new sheet in the Excel file
    sheet = excel_file.active

    # Add the roll number and name to the sheet
    sheet["A1"] = "Roll Number"
    sheet["B1"] = "Name"

    # Iterate through the data and add it to the sheet
    for row in range(len(data)):
        roll_number = data[row][0]
        name = data[row][1]
        sheet["A" + str(row + 2)] = roll_number
        sheet["B" + str(row + 2)] = name

    # Save the Excel file
    excel_file.save("/content/std info.xlsx")

if __name__ == "__main__":
    # Get the data from the user
    data = []
    for _ in range(int(input("Enter the number of students: "))):
        roll_number = input("Enter the roll number: ")
        name = input("Enter the name: ")
        data.append((roll_number, name))

    # Push the data to Excel
    push_data_to_excel(data)
    print("Successfully pushed the data to Excel.")
