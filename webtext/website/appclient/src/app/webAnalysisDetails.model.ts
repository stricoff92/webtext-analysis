
export type WordCounts = {
    [key: string]: number;
}

// Structure for a web analysis with all info (for a detailed view)
export class WebAnalysisFullDetails {
    analysis_mode:string;
    created_at:string;
    page_content:string;
    page_content_length:number;
    page_content_type:string;
    slug:string;
    target_url:string;
    word_counts:WordCounts;
}

// Structure for a web analysis with limited info (for a list)
export class WebAnalysisListDetails {
    analysis_mode:string;
    created_at:string;
    page_content_length:number;
    page_content_type:string;
    slug:string;
    target_url:string;

    // Verbose info is optional
    word_counts?:WordCounts;
    page_content?:string;
}
