import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import csv
from gff_parser import parse_gff3
from block_extractor import get_gene_block
from block_comparer import lcs

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ortholog Block Comparator")
        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Genome 1 GFF3:").grid(row=0, column=0)
        self.gff1_entry = tk.Entry(self.root, width=50)
        self.gff1_entry.grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.load_gff1).grid(row=0, column=2)

        tk.Label(self.root, text="Genome 2 GFF3:").grid(row=1, column=0)
        self.gff2_entry = tk.Entry(self.root, width=50)
        self.gff2_entry.grid(row=1, column=1)
        tk.Button(self.root, text="Browse", command=self.load_gff2).grid(row=1, column=2)

        tk.Label(self.root, text="Ortholog CSV:").grid(row=2, column=0)
        self.ortholog_entry = tk.Entry(self.root, width=50)
        self.ortholog_entry.grid(row=2, column=1)
        tk.Button(self.root, text="Browse", command=self.load_ortholog).grid(row=2, column=2)

        tk.Label(self.root, text="±N genes:").grid(row=3, column=0)
        self.n_entry = tk.Entry(self.root)
        self.n_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Compare Blocks", command=self.compare).grid(row=4, column=1)

        self.output = scrolledtext.ScrolledText(self.root, width=90, height=25)
        self.output.grid(row=5, column=0, columnspan=3)

    def load_gff1(self):
        self.gff1_entry.delete(0, tk.END)
        file = filedialog.askopenfilename(filetypes=[("GFF3 files", "*.gff3")])
        if file:
            self.gff1_entry.insert(0, file)

    def load_gff2(self):
        self.gff2_entry.delete(0, tk.END)
        file = filedialog.askopenfilename(filetypes=[("GFF3 files", "*.gff3")])
        if file:
            self.gff2_entry.insert(0, file)

    def load_ortholog(self):
        self.ortholog_entry.delete(0, tk.END)
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            self.ortholog_entry.insert(0, file)

    def compare(self):
        try:
            N = int(self.n_entry.get())
            gff1, gff2 = self.gff1_entry.get(), self.gff2_entry.get()
            ortholog_file = self.ortholog_entry.get()

            gene_dict1, gene_order1 = parse_gff3(gff1)
            gene_dict2, gene_order2 = parse_gff3(gff2)

            with open(ortholog_file, 'r') as f:
                reader = csv.reader(f)
                header = next(reader)
                results = []

                for row in reader:
                    gene1, gene2 = row
                    block1 = get_gene_block(gene1, gene_dict1, gene_order1, N)
                    block2 = get_gene_block(gene2, gene_dict2, gene_order2, N)
                    match_len, lcs_seq = lcs(block1, block2)
                    match_pct = round((match_len / max(len(block1), len(block2))) * 100, 2)

                    result = f"🧬 {gene1} ↔ {gene2}\nBlock1: {block1}\nBlock2: {block2}\n" \
                             f"Match %: {match_pct}%, LCS: {lcs_seq}\n---\n"
                    results.append(result)

            self.output.delete(1.0, tk.END)
            self.output.insert(tk.END, "".join(results))

        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()