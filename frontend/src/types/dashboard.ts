export interface DashboardSummary {
  total_complaints: number;
  categories: Record<string, number>;
  sentiments: Record<string, number>;
}

export interface TopCategory {
  category: string;
  count: number;
}

export interface TopCategoryResponse {
  data: TopCategory[];
}

export interface SentimentData {
  sentiment: string;
  count: number;
}

export interface SentimentResponse {
  data: SentimentData[];
}
