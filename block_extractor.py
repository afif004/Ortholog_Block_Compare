def get_gene_block(gene_id, gene_dict, gene_order, N):
    if gene_id not in gene_dict:
        return []

    chr_id = gene_dict[gene_id][0]
    if chr_id not in gene_order:
        return []

    gene_list = gene_order[chr_id]
    i = gene_list.index(gene_id)

    start = max(0, i - N)
    end = min(len(gene_list), i + N + 1)
    return gene_list[start:end]
