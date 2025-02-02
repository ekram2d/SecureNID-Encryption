

---

# Encrypted ID Card Processing

This project securely processes ID card images by extracting the ID number using Optical Character Recognition (OCR), encrypting it with AES-256 encryption, and modifying the image to hide the original ID number. The encrypted version of the ID number is displayed on the image, and the system also provides a decryption mechanism to restore the original ID number.

## Features

- **OCR-Based ID Number Extraction**: Uses `EasyOCR` to extract the ID number from images.
- **AES-256 Encryption**: Encrypts the extracted ID number to prevent unauthorized access.
- **Image Modification**: Automatically replaces the original ID number in the image with an encrypted version.
- **Decryption & Restoration**: Provides the ability to decrypt and restore the original ID number.
- **Visualization & Comparison**: Displays side-by-side comparisons of the original, modified, and restored images.

## Folder Structure

```
encrypted_decrypted_process/
│── incrypted_decrypted.py  # Main script for ID encryption & decryption
│── nid1.jpg                # Example NID card image
│── original_id_card.jpg     # Output: Original image (saved after processing)
│── modified_id_card.jpg     # Output: Image with encrypted ID
│── decrypted_id_card.jpg    # Output: Restored original ID card
│── README.md                # Project documentation
```

## Requirements

Ensure you have the required Python libraries installed before running the script:

```bash
pip install easyocr cryptography pillow matplotlib numpy
```

## How It Works

1. The script extracts text from the provided ID card image using OCR.
2. It searches for the ID number using a regex pattern.
3. If the ID number is found, it is **encrypted** using AES-256 encryption.
4. The extracted ID number is removed from the image, and the encrypted version is displayed.
5. The encrypted ID can later be **decrypted** to restore the original ID number.
6. The script visualizes and saves the **original**, **modified**, and **decrypted** images.

## How to Run the Script

### Step 1: Place the ID Card Image
Save your ID card image as `nid1.jpg` (or provide a different path in the script).

### Step 2: Run the Script
Execute the Python script:

```bash
python incrypted_decrypted.py
```

### Step 3: View and Download Processed Images
After execution:
- `original_id_card.jpg`: The original image before modification.
- `modified_id_card.jpg`: The image with the encrypted ID number.
- `decrypted_id_card.jpg`: The restored original image.

## Running in Google Colab

If you're running this script in **Google Colab**, follow these steps:

1. Upload the `nid1.jpg` file to your Colab environment.
2. Install the dependencies:

   ```python
   !pip install easyocr cryptography pillow matplotlib numpy
   ```

3. Run the script using:

   ```python
   !python incrypted_decrypted.py
   ```

4. Download the processed images:

   ```python
   from google.colab import files
   files.download("original_id_card.jpg")
   files.download("modified_id_card.jpg")
   files.download("decrypted_id_card.jpg")
   ```

## Functions

### `encrypt_text(text)`
- **Encrypts** a given text using AES-256.
- Returns an encrypted string.

### `decrypt_text(ciphertext)`
- **Decrypts** the encrypted ID number.
- Returns the original plaintext ID number.

### `extract_id_number(text)`
- Uses **Regex** to identify and extract the ID number from OCR text.
- Returns the ID number if found.

### `process_id_image(image_path, languages=['en', 'bn'], show_plot=True)`
- Extracts the **ID number** from the image.
- Encrypts and **modifies** the image by replacing the original ID number.
- Saves and **displays** the original, modified, and decrypted images.
- Returns the processed images.

## Example Output

After running the script, you will see:

1. **Original ID Card Image**  
![original_id_card](https://github.com/user-attachments/assets/eb52a8d4-80eb-4be2-a393-e3f40b84fae8)

2. **Modified ID Card (With Encrypted ID)**  
![modified_id_card](https://github.com/user-attachments/assets/ffd1bf8e-2174-42f2-82b1-7126508b8c2c)

3. **Restored ID Card (After Decryption)**  
![decrypted_id_card](https://github.com/user-attachments/assets/fe532d3d-b7a5-430d-95f5-0b5cb1bcabb6)

## License

This project is licensed under the **MIT License**.

---

