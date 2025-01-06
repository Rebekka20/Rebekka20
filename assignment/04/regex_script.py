import re 


def main():
    
    # Read the CSV file with the product orders
    with open('./orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'

    # Match the regex with the text
    orders = re.findall(regex, text)

    # Print the results
    print(orders)
    

if __name__ == '__main__':
    main()