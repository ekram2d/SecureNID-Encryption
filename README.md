

---

### **📌 Secure ID Card Processing with Encryption**
This project extracts an ID number from an image using OCR, encrypts it using AES-256, modifies the image to mask the ID, and allows decryption to restore the original ID.  

## **🛠 Features**
✅ Extracts ID number from an image using **EasyOCR**  
✅ Encrypts the ID number using **AES-256 (Fernet encryption)**  
✅ Replaces the ID number in the image with an **encrypted version**  
✅ Allows **decryption** and restoration of the **original ID number**  
✅ Saves **original, modified, and restored images**  
✅ Provides **visualization** of the encryption and decryption process  

---

## **📌 Prerequisites**
Ensure you have **Python 3.7 or later** installed on your system.  

---

## **📌 Installation (Local Machine)**
### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/yourusername/secure-id-encryption.git
cd secure-id-encryption
```

### 2️⃣ **Install Required Dependencies**  
```sh
pip install -r requirements.txt
```
_If you don’t have `requirements.txt`, install manually:_  
```sh
pip install easyocr pillow cryptography numpy matplotlib
```

### 3️⃣ **Run the Script**
```sh
python incrypted_decrypted.py
```

---

## **📌 Running in Google Colab**
If you want to run this project in **Google Colab**, follow these steps:  

### 1️⃣ **Open Google Colab**  
- Go to **[Google Colab](https://colab.research.google.com/)**  

### 2️⃣ **Upload Your Image**  
- Click on the left **File icon 📂**
- Upload your **ID card image** to `/content/`  

### 3️⃣ **Install Dependencies in Colab**  
Run the following command in a Colab **code cell**:  
```python
!pip install easyocr pillow cryptography numpy matplotlib
```

### 4️⃣ **Upload the Script**
- Click on **File > Upload** and upload `incrypted_decrypted.py`  
- Run the script using:  
```python
!python incrypted_decrypted.py
```

### 5️⃣ **Download Processed Images**
After execution, download the images using:  
```python
from google.colab import files
files.download("original_id_card.jpg")
files.download("modified_id_card.jpg")
files.download("decrypted_id_card.jpg")
```

---

## **📌 Expected Output**
The script will generate and save three images:  
📌 **`original_id_card.jpg`** – Original ID image  
📌 **`modified_id_card.jpg`** – Encrypted ID image (masked)  
📌 **`decrypted_id_card.jpg`** – Restored image with the original ID  

---

## **📌 Notes**
🔹 Ensure your image path is correctly set in `incrypted_decrypted.py`.  
🔹 If you run into **font issues**, install DejaVu font or use the default system font.  
🔹 Google Colab **downloads the processed images automatically** if you use the provided script.  

---

## **📌 License**
This project is open-source under the **MIT License**.  

---
