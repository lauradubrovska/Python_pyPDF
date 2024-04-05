# Electricity price analysis task

### Taks description

Your assignment is to determine the potential overpayment for electricity when compared to the Nordpool electricity rate. Here's what you need to do:

1. Examine the provided invoice PDF file.
2. Extract the price and the quantity of electricity used in a specific month (all relevant details are in the PDF).
3. Calculate any potential savings or excess costs by comparing your invoice's static price to the Nordpool electricity prices.

Remember, the goal is to find out if using Nordpool electricity rates would be more economical than your current billing rate.

**You should submit your program as `result.py` file.**

### Input data
At the start of the program, please input the path to the invoice PDF file. For instance, you can enter `invoices/invoice1.pdf`.

### Output data
The program should output a result in float format, rounded to one decimal place. This figure represents the potential savings or extra costs when using Nordpool electricity prices, compared to the fixed electricity price noted in your invoice. If the system cannot locate the file, it should return a result of '0'. Similarly, if the electricity consumption is recorded as '0', the output should also be '0'.

### PDF file structure
The provided PDF file is an invoice detailing the electricity usage and its associated costs. The total charge is a sum of the electricity cost and other fees related to transfer and management. For this task, we are focusing solely on the price of electricity per kWh.

Please review the invoice thoroughly to pinpoint the electricity price. On the first page, you'll find the overall charge for the electricity consumed during a specific period. The second page provides a breakdown, detailing both the quantity of electricity used and its price per kWh.

For your calculations, it's essential to extract the following four values from the PDF:

1. Total charge for electricity (found on the 1st page).
2. Quantity of electricity consumed (found on the 2nd page).
3. Price per kWh (found on the 2nd page).
4. The time frame during which the electricity was used (found on the 1st page).

### nordpool.csv file structure
The file is in CSV format and provides an hourly breakdown of historical electricity cost data.

### PyPDF2 library
When you see the line `import PyPDF2` in a Python script, it indicates that the script will be utilizing the `PyPDF2` library. Here's a detailed explanation of why one might use `PyPDF2`:

**PyPDF2** is a widely-used Python library that allows developers to work with PDF files. Here are the main reasons why someone might use `PyPDF2`:

1. **Reading PDFs**: PyPDF2 can be used to extract text and other data from PDF files. This is especially useful for scripts or applications that need to pull content from such files for further processing or analysis.

2. **Merging PDFs**: If there's a need to combine multiple PDF files into one, PyPDF2 offers functionality to merge them seamlessly.

3. **Splitting PDFs**: Conversely, PyPDF2 can also split a single PDF into multiple separate files based on pages or page ranges.

4. **Encrypting and Decrypting PDFs**: PyPDF2 supports adding password protection to PDF files as well as removing such protection from encrypted files.

5. **Manipulating Pages**: You can use PyPDF2 to add, rearrange, rotate, or delete pages within a PDF file.

6. **General PDF Analysis**: The library provides functions to retrieve general information about a PDF, such as the number of pages, metadata, and more.

By importing `PyPDF2`, a developer gains access to all these functionalities and can integrate them into their Python script or application. In the context of your previous questions, it's likely being used to extract data from an invoice stored in PDF format.

### Necessary resources
To address this problem set, you can refer to the tutorial video [here](https://youtu.be/vsrxkJ9HF24), which provides guidance on processing PDF files. Additionally, example source code can be accessed on GitHub at [this link](https://github.com/ajurenoks/dip225_3).
