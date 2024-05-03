import readline

def clean_urls(input_file, output_file):
    with open(input_file, 'r') as f:
        urls = f.readlines()

    cleaned_urls = []
    for url in urls:
        cleaned_url = url.split(' ')[2].strip()
        cleaned_urls.append(cleaned_url)

    with open(output_file, 'w') as f:
        for url in cleaned_urls:
            f.write(url + '\n')

if __name__ == "__main__":
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")

    clean_urls(input_file, output_file)
    print("URLs cleaned and saved to", output_file)
