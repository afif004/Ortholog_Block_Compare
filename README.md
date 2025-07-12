- **Block size parameter**  
Number of upstream and downstream genes to include (±N)

---

## 📤 Outputs
- **Console/GUI Report**  
Displays:
- Matched orthologs  
- Extracted gene blocks  
- LCS similarity score  
- Detected rearrangements  
- **CSV Report**  
`ortholog_results.csv` summarizing comparison results  
- **(Optional)** Gene block visualization using `matplotlib`  

---

## 🧠 Data Structures Used
- **Hash Maps / Dictionaries**  
- For fast lookup of gene positions using gene IDs  
- **Sorted Arrays**  
- For efficient ±N gene extraction via binary search  
- **Dynamic Programming Matrix**  
- For computing the LCS between gene blocks  

---

## 🛠 Technologies
- Python 3.10+  
- [Biopython](https://biopython.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [Tkinter](https://wiki.python.org/moin/TkInter) (for GUI)  
- [Matplotlib](https://matplotlib.org/) *(optional)*  
- [PyInstaller](https://www.pyinstaller.org/) *(for packaging)*  
