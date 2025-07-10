from gff_parser import parse_gff3
from block_extractor import get_gene_block

if __name__ == "__main__":

    filepath = input("Enter the path to GFF3 file: ")

    try:
        gene_dict, gene_order = parse_gff3(filepath)
        print(f"\nSuccessfully parsed {len(gene_dict)} genes from {filepath}")

        gene_id = input("\nEnter a gene ID to extract surrounding block: ")
        N = int(input("Enter the ±N gene block size: "))

        if gene_id not in gene_dict:
            print(f"Gene ID '{gene_id}' not found in the file.")
        else:
            block = get_gene_block(gene_id, gene_dict, gene_order, N)
            print(f"\nExtracted Block around '{gene_id}' (±{N} genes):")
            print(" -> " + "  |  ".join(block))

    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except ValueError:
        print("Invalid input. N must be an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")
