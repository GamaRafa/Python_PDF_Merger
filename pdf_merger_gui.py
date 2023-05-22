import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog
import PyPDF2
import os


def merge_pdfs():
    # Escolhe a pasta de origem
    input_folder = filedialog.askdirectory(title='Escolher pasta de origem')
    if input_folder:
        # Escolhe a pasta de destino e o nome do novo arquivo
        output_file = filedialog.asksaveasfilename(title='Salvar PDF mesclado como: ', defaultextension='.pdf',
                                                   filetypes=[('PDF Files', "*.pdf")])
        if output_file:
            merger = PyPDF2.PdfFileMerger(strict=False)

            # Pega todos os PDF da pasta
            pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

            # Junta os PDF
            for file in pdf_files:
                file_path = os.path.join(input_folder, file)
                merger.append(file_path)

            # Escreve o PDF mesclado no arquivo de saída
            merger.write(output_file)
            merger.close()
            status_label.config(text='Arquivos mesclados!')


# Cria a janela
root = tk.Tk()
root.title('PDF Merger App')
root.geometry('800x600')
root.resizable(False, False)

# Create the widgets

custom_font = tkfont.Font(size=14)

sidebar_frame = tk.Frame(root, bg='lightblue', width=200)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

instructions_label = tk.Label(sidebar_frame, text='Instruções de uso:\n'
                                                  '\n- Crie uma nova pasta, e nela coloque\ntodos os arquivos a serem '
                                                  'mesclados\n '
                                                  '\n- Na janela "Escolher pasta de origem",\nselecionar a pasta '
                                                  'criada.\n '
                                                  '\n- Na janela "Salvar PDF mesclado como: ",\nselecione a pasta de '
                                                  'destino e o nome do arquivo.',
                              font=custom_font, anchor='w', justify='left')
instructions_label.pack(side=tk.LEFT)

merge_button = tk.Button(root, bg='lightblue', text='Mesclar PDFs', font=custom_font, command=merge_pdfs, width=12,
                         height=2)
merge_button.place(relx=0.8, y=300, anchor=tk.CENTER)

status_label = tk.Label(root, text='', font=custom_font)
status_label.pack(side=tk.BOTTOM)

# Run the main event loop
root.mainloop()
