import qrcode
import tkinter as tk
from tkinter import filedialog 

#untuk membuat QR Code Nya
def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    gambar = qr.make_image(fill_color="black", back_color="white")
    gambar.save(file_name)


# Membuat file QR Code Nya
def click_generate():
    data = entry_data.get()
    if data:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if file_path:
            generate_qr_code(data, file_path)

if __name__ == "__main__":
    app = tk.Tk() # Membuat jendela utama aplikasi
    app.title("QR Code Generator")

    window_width = 600
    window_height = 300

    # Mengatur ukuran jendela nya
    app.geometry(f"{window_width}x{window_height}")

    # Untuk label di atas nya
    label = tk.Label(app, text="Masukkan data:")
    # Mengatur jarak label nya
    label.pack(pady=10)

    # Mengatur masukkan nya
    entry_data = tk.Entry(app, width=40)
    entry_data.pack(pady=5)
    
    # Untuk tombol nya
    generate_button = tk.Button(app, text="Generate QR Code", command=click_generate)
    generate_button.pack(pady=10)

    app.mainloop()