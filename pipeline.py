from graphviz import Digraph

def create_manga_ocr_diagram():
    dot = Digraph(comment='Manga OCR Architecture', format='png')
    dot.attr(rankdir='LR', splines='ortho')
    
    # Global Styles mimicking the technical diagrams provided
    dot.attr('node', shape='rect', style='filled', fillcolor='#E3F2FD', fontname='Arial', fontsize='10')
    dot.attr('edge', color='#555555', arrowsize='0.8')

    # --- INPUTS ---
    dot.node('IMG', 'Input Image\n(H x W x 3)', shape='oval', fillcolor='#FFF9C4')
    dot.node('TXT', 'Context Tokens\n(Start / Prev Chars)', shape='oval', fillcolor='#FFF9C4')

    # --- CLUSTER: VISION ENCODER ---
    with dot.subgraph(name='cluster_vit') as c:
        c.attr(label='ViT Encoder (Vision Transformer)', style='dashed', color='#0277BD', bgcolor='#E1F5FE')
        
        # Patch Embedding
        c.node('CONV', 'Patch Embedding\nConv2d (k=16, s=16)\nInput -> 768 dim', fillcolor='#B3E5FC')
        c.node('POS_V', 'Add Position\nEmbeddings', fillcolor='#B3E5FC')
        
        # Transformer Stack
        c.node('ENC_STACK', 'Transformer Encoder\n(x12 Layers)\n[Self-Attention + MLP]', shape='component', fillcolor='#81D4FA')
        
        c.edge('CONV', 'POS_V', label='Flatten')
        c.edge('POS_V', 'ENC_STACK', label='Visual Tokens\n(N x 768)')

    # --- CLUSTER: TEXT DECODER ---
    with dot.subgraph(name='cluster_bert') as c:
        c.attr(label='BERT Decoder (Generative)', style='dashed', color='#F9A825', bgcolor='#FFFDE7')
        
        # Embeddings
        c.node('EMB', 'Text Embedding\nLookup + Positional', fillcolor='#FFF59D')
        
        # Decoder Layer Detail
        c.node('DEC_SA', 'Masked Self-Attention\n(Context)', fillcolor='#FFCC80')
        c.node('DEC_CA', 'CROSS-ATTENTION\n(Query=Text, KV=Image)', fillcolor='#FFAB91', style='filled,bold')
        c.node('DEC_FFN', 'Feed Forward\n(MLP)', fillcolor='#FFCC80')
        
        c.edge('EMB', 'DEC_SA')
        c.edge('DEC_SA', 'DEC_CA')
        c.edge('DEC_CA', 'DEC_FFN')

    # --- OUTPUT HEAD ---
    dot.node('HEAD', 'LM Head\nLinear 768 -> Vocab', fillcolor='#C8E6C9')
    dot.node('PROB', 'Softmax\n(Next Character)', shape='oval', fillcolor='#A5D6A7')

    # --- CONNECTIONS ---
    # Image to Encoder
    dot.edge('IMG', 'CONV')
    
    # Text to Decoder
    dot.edge('TXT', 'EMB')
    
    # The Critical Bridge (Cross Attention)
    dot.edge('ENC_STACK', 'DEC_CA', label='Keys & Values\n(Visual Features)', color='#D32F2F', penwidth='2.0')
    
    # Decoder to Output
    dot.edge('DEC_FFN', 'HEAD', label='Hidden State')
    dot.edge('HEAD', 'PROB')

    # Render
    dot.render('manga_ocr_architecture', view=True)
    print("Diagram generated: manga_ocr_architecture.png")

if __name__ == "__main__":
    try:
        create_manga_ocr_diagram()
    except Exception as e:
        print("Error: Make sure Graphviz is installed on your system path.")
        print(e)