from gff_parser import parse_gff3
if __name__ == "__main__":
    print("GFF3 Parser")
    filepath = input("Enter the path to GFF3 file: ")
    
    try:
        gene_dict, gene_order = parse_gff3(filepath)
        print(f"\n Successfully parsed {len(gene_dict)} genes from {filepath}\n")
        
        print("Sample genes (showing first 10):\n")
        for i, (gene_id, (chr, start, end)) in enumerate(gene_dict.items()):
            print(f"{gene_id}: {chr}, {start}-{end}")
            if i == 9:
                break   
    except FileNotFoundError:
        print("❌ File not found. Please check the path and try again.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")