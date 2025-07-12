# Ortholog_Block_Compare
Objectives
1. Parse GFF3 genome annotations into structured gene data


Extract ±N neighboring genes around ortholog anchors


Determine gene order conservation using the Longest Common Subsequence (LCS) algorithm


Try visualizing synteny blocks with rearrangement metrics


Generate comparative reports
Inputs:
genome1.gff3, genome2.gff3 (Annotation files in GFF3 format)


orthologs.csv (Gene pairs: gene1_id,gene2_id)


Block size parameter (±N genes)


Outputs:
Console/GUI text report showing matched orthologs, gene blocks, LCS, and rearrangements


CSV report: ortholog_results.csv


Gene block visualization (Unsure to be implemented)


Data Structures Used
Hash Maps/Dictionaries
	For gene position finding based on gene ID
Sorted Arrays
	For efficient extraction of neighboring genes using binary search
Dynamic Programming Matrix
	For computing gene order similarity by using the LCS algorithm


Technologies
Python 3.10+
Biopython
Pandas
Tkinter
Matplotlib
PyInstaller
