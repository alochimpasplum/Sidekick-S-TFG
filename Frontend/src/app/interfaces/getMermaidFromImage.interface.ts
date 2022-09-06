export interface GetMermaidFromImage {
    mermaid_blocks:        MermaidBlock[];
    image_with_detections: string;
    image_mermaid: string;
}

export interface MermaidBlock {
    block_name:               string;
    text:                     string;
    previous_blocks:          any[];
    next_blocks:              string[];
    next_blocks_conditionals: { [key: string]: string };
    object_type:              string;
}
