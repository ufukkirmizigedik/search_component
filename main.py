
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import shutil
import os
from weller import get_product_link_weller
from dmc import get_product_link_dmc
from harvin import get_product_link_harwin

def browse_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
    label.config(text=file_path)

def start():
    global file_path
    if file_path:
        target_folder = 'C:/Users/user/Desktop/Searcher'
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        try:
            shutil.copy(file_path, target_folder)
            label.config(text="File has been successfully attached")
        except Exception as e:
            label.config(text=f"Error: {e}")
    else:
        label.config(text="Please attach a file before starting")
    root.destroy()

root = tk.Tk()
root.title("Search Component,Tools..etc")
root.geometry("500x300")
root.configure(bg="#f0f0f0")
label = tk.Label(root, text="Upload your Excel file", font=("Arial", 18), bg="#f0f0f0")
label.pack(pady=20)
browse_button = tk.Button(root, text="Attach", command=browse_file, bg="#4CAF50", fg="white", font=("Arial", 14))
browse_button.pack(pady=10)
start_button = tk.Button(root, text="Start", command=start, bg="#008CBA", fg="white", font=("Arial", 14))
start_button.pack(pady=10)
root.mainloop()

df = pd.read_excel('veri.xlsx', dtype={'reference': str})
print(df)

for index, row in df.iterrows():
    product_name = row['Name']
    catalog = row['catalog']
    if pd.notna(catalog):

        if catalog == 'weller':
            product_link = get_product_link_weller(product_name)
            if product_link is not None:
                df.at[index, 'reference'] = "www.weller-tools.com" + product_link
        elif catalog == 'dmc':
            product_link = get_product_link_dmc(product_name)
            if product_link is not None:
                df.at[index, 'reference'] = product_link
        elif catalog == 'harwin':
            product_link = get_product_link_harwin(product_name)
            if product_link is not None:
                df.at[index,'reference'] = product_link
    else:
        weller_product_link = get_product_link_weller(product_name)
        if weller_product_link is not None:
            df.at[index, 'reference'] = "www.weller-tools.com" + weller_product_link
            df.at[index,'catalog'] = 'weller'

        else:
            dmc_product_link = get_product_link_dmc(product_name)
            if dmc_product_link is not None:
                df.at[index, 'reference'] = dmc_product_link
                df.at[index,'catalog'] = 'dmc'
            else:
                harwin_product_link = get_product_link_harwin(product_name)
                if harwin_product_link is not None:
                    df.at[index,'reference'] = harwin_product_link
                    df.at[index,'catalog'] = 'harwin'


df.to_excel('guncellenmis_veri.xlsx', index=False)
file_path = 'guncellenmis_veri.xlsx'
os.startfile(file_path)
