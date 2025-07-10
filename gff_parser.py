def parse_gff3(filepath):
    gene_dict = {}
    gene_order = {}
    
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split('\t')
            if len(parts) != 9:
                continue

            seqid, source, feature, start, end, score, strand, phase, attributes = parts

            if feature != 'gene':
                continue
            
            attr_parts = attributes.split(';')
            gene_id = None
            for attr in attr_parts:
                attr = attr.strip()
                if attr.startswith("ID="):
                    gene_id = attr.split("ID=")[1].split(":")[-1]
                    break
                elif 'gene_id=' in attr:
                    gene_id = attr.split('gene_id=')[1].split(':')[-1]
                    break
                elif  'Name=' in attr:
                    gene_id = attr.split('Name=')[1].split(':')[-1]
                    break
            if not gene_id:
                continue

            start, end = int(start), int(end)
            gene_dict[gene_id] = (seqid, start, end)

            if seqid not in gene_order:
                gene_order[seqid] = []
            gene_order[seqid].append((start, gene_id))
        
    for chr_id in gene_order:
        gene_order[chr_id].sort()
        gene_order[chr_id] = [gid for _,gid in gene_order[chr_id]]
    return gene_dict, gene_order