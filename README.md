
# URL Masking Tool

## Description

This tool allows users to mask URLs with a custom domain and keyword. The main purpose is to generate a masked URL from an original URL, making it look like it belongs to the custom domain while incorporating a keyword.

## Features

- **URL Validation**: Ensures that the input URL is in a valid format.
- **Custom Domain Validation**: Ensures that the custom domain is valid.
- **Keyword Validation**: Ensures that the keyword is a valid string without spaces and within the maximum length.
- **URL Shortening**: Uses the `pyshorteners` library to shorten the original URL.
- **Masked URL Generation**: Combines the custom domain, keyword, and shortened URL to create a masked URL.

## Requirements

- Python 3.x
- `pyshorteners`
- `colorama`

You can install the required Python packages using pip:

```sh
pip install pyshorteners colorama
```

## Usage

1. **Clone the Repository**

   ```sh
   git clone https://github.com/apkaless/url-masking-tool.git
   cd url-masking-tool
   ```

2. **Run the Script**

   ```sh
   python url_masking_tool.py
   ```

3. **Follow the Prompts**

   - **URL To Mask**: Enter the URL you want to mask.
   - **Custom Domain**: Enter the custom domain (e.g., `google.com`).
   - **Phish Keyword**: Enter a keyword (e.g., `login`, `free`, etc.).

## Example

```
 ↳ URL To Mask → https://example.com
 ↳ Custom Domain (ex: google.com) → google.com
 ↳ Phish Keyword (ex: login, free, anything) → login

[~] Original URL → https://example.com
[~] Masked URL → https://google.com-login@short.url/abc123
```

## Code Explanation

- **print_banner()**: Displays the tool's banner with version, GitHub, Instagram, and region information.
- **validate_url(url)**: Validates the input URL format.
- **validate_custom_domain(custom_domain)**: Validates the custom domain format.
- **validate_keyword(keyword)**: Validates the keyword format and length.
- **short_url(web_url)**: Shortens the original URL using `pyshorteners`.
- **mask_url(custom_domain, keyword, url)**: Creates a masked URL by combining the custom domain, keyword, and shortened URL.
- **main()**: Main function to handle user input and output the masked URL.

## Notes

- Ensure that your input values are correct and follow the expected formats.
- The script is intended for educational purposes only. Use responsibly.

## Author

- GitHub: [apkaless](https://github.com/apkaless)
- Instagram: [apkaless](https://instagram.com/apkaless)

## License

This project is licensed under the MIT License.
