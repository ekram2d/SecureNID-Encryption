import easyocr
from PIL import Image, ImageDraw, ImageFont
from cryptography.fernet import Fernet
import re
import numpy as np
import matplotlib.pyplot as plt

# Generate encryption key (do this once and store securely)
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)

def encrypt_text(text):
    """Encrypts text using AES-256."""
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt_text(ciphertext):
    """Decrypts text using AES-256."""
    return cipher_suite.decrypt(ciphertext.encode()).decode()

def extract_id_number(text):
    """Extracts ID number with flexible regex."""
    match = re.search(r'(?:IDNO|IDN|DN\|9|DNI|DNO)[:\s]*(\d+)', text, re.IGNORECASE)
    return match.group(1) if match else None

def process_id_image(image_path, languages=['en', 'bn'], show_plot=True):
    try:
        # Read and process original image
        original_image = Image.open(image_path).convert("RGB")
        reader = easyocr.Reader(languages)
        results = reader.readtext(image_path)

        # OCR processing
        id_number = None
        bbox_to_replace = None
        for bbox, text, confidence in results:
            detected_id = extract_id_number(text)
            if detected_id:
                id_number = detected_id
                bbox_to_replace = bbox
                break

        if not id_number:
            print("❌ No ID number detected.")
            return None, None

        # Encrypt and modify image
        encrypted_id = encrypt_text(id_number)
        modified_image = original_image.copy()
        draw = ImageDraw.Draw(modified_image)

        if bbox_to_replace:
            x1, y1 = bbox_to_replace[0]
            x3, y3 = bbox_to_replace[2]
            draw.rectangle([x1-10, y1-10, x3+10, y3+10], fill="white")

            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 70)
            except:
                font = ImageFont.load_default(size=50)

            text = f"ID NO: {encrypted_id[:12]}..."
            draw.text((x1, y1), text, fill="black", font=font)

        # Save images for download
        original_image.save("original_id_card.jpg")
        modified_image.save("modified_id_card.jpg")

        decrypted_id = decrypt_text(encrypted_id)
        restored_image = original_image.copy()
        restored_image.save("decrypted_id_card.jpg")

        # Visualization
        if show_plot:
            plt.figure(figsize=(18, 10))

            # Original Image
            plt.subplot(1, 3, 1)
            plt.imshow(original_image)
            plt.title("Original ID Card", fontsize=12)
            plt.axis('off')

            # Modified Image
            plt.subplot(1, 3, 2)
            plt.imshow(modified_image)
            plt.title("Modified ID Card", fontsize=12)
            plt.axis('off')

            # Decryption and show plain image
            plt.subplot(1, 3, 3)
            plt.imshow(restored_image)
            plt.title("Decrypted ID Card (Original Restored)", fontsize=12)
            plt.axis('off')

            plt.suptitle("ID Card Security Process", fontsize=16, y=0.95)
            plt.tight_layout()
            plt.show()

        return original_image, modified_image, restored_image

    except Exception as e:
        print(f"⚠ Error: {e}")
        return None, None, None

if __name__ == "__main__":
    image_path = "nid1.jpg"  # Replace with your image path
    original, modified, decrypted = process_id_image(image_path)

    # Provide download links
    from google.colab import files  # Use this if running in Google Colab

    files.download("original_id_card.jpg")
    files.download("modified_id_card.jpg")
    files.download("decrypted_id_card.jpg")
