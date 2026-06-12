import api from "@/lib/axios";

const fallbackSummary = {
  total_complaints: 128,
  categories: { Layanan: 42, Teknologi: 31, Keuangan: 25, Operasional: 30 },
  sentiments: { Positif: 54, Netral: 39, Negatif: 35 },
};

const fallbackCategories = [
  { category: "Layanan", count: 42 },
  { category: "Teknologi", count: 31 },
  { category: "Keuangan", count: 25 },
  { category: "Operasional", count: 30 },
];

const fallbackSentiments = [
  { sentiment: "Positif", count: 54 },
  { sentiment: "Netral", count: 39 },
  { sentiment: "Negatif", count: 35 },
];

const fallbackInsight = { content: "Backend belum aktif. Dashboard ini menampilkan data contoh agar tampilan tetap bisa diuji." };

const fallbackComplaints = [
  { id: 1, title: "Layanan aplikasi lambat", description: "Aplikasi terasa lambat saat login.", category: "Teknologi", sentiment: "Negatif", location: "Jakarta", created_at: "2026-06-10T08:30:00Z" },
  { id: 2, title: "Informasi akun tidak jelas", description: "Petunjuk reset password belum jelas.", category: "Layanan", sentiment: "Netral", location: "Bandung", created_at: "2026-06-11T10:15:00Z" },
];

const safeRequest = async <T>(request: () => Promise<T>, fallback: T, label: string) => {
  try {
    return await request();
  } catch (error) {
    console.warn(`API fallback used for ${label}:`, error);
    return fallback;
  }
};

export const getDashboardSummary = async () =>
  safeRequest(async () => (await api.get("/dashboard/summary")).data, fallbackSummary, "summary");

export const getTopCategories = async () =>
  safeRequest(async () => (await api.get("/dashboard/top-categories")).data, { data: fallbackCategories }, "top categories");

export const getSentiments = async () =>
  safeRequest(async () => (await api.get("/dashboard/sentiment-distribution")).data, { data: fallbackSentiments }, "sentiments");

export const getLatestInsight = async () =>
  safeRequest(async () => (await api.get("/insights/latest")).data, fallbackInsight, "latest insight");

export const getComplaints = async () =>
  safeRequest(async () => (await api.get("/complaints")).data, fallbackComplaints, "complaints");

export const createComplaint = async (
  payload: {
    title: string;
    description: string;
    location: string;
  }
) => {

  const response =
    await api.post(
      "/complaints",
      payload
    );

  return response.data;
};

export const generateInsight = async (
  days: number
) => {

  const response =
    await api.post(
      `/insights/generate?days=${days}`
    );

  return response.data;
};

export const getInsights = async () => {

  const response =
    await api.get(
      "/insights"
    );

  return response.data;
};