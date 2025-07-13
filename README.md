# Ortholog_Block_Compare

## 🎯 Objectives
1. Parse GFF3 genome annotations into structured gene data  
2. Extract ±N neighboring genes around ortholog anchors  
3. Determine gene order conservation using the Longest Common Subsequence (LCS) algorithm  
4. Visualize synteny blocks with rearrangement metrics *(optional/experimental)*  
5. Generate comparative reports  

---

## 📥 Inputs
- `genome1.gff3`, `genome2.gff3`  
  Annotation files in **GFF3** format  
- `orthologs.csv`  
  List of orthologous gene pairs in the format:  


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
- [Matplotlib](https://matplotlib.org/) *(for future updates)*  
- [PyInstaller](https://www.pyinstaller.org/) *(for packaging)*  
