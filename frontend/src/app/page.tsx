"use client";

import { useEffect, useState } from "react";

import AppShell from "@/components/layout/AppShell";
import SummaryCards from "@/components/dashboard/SummaryCards";
import TopCategoriesChart from "@/components/dashboard/TopCategories";
import SentimentChart from "@/components/dashboard/SentimentChart";
import InsightCard from "@/components/insight/InsightCard";
import type { Insight } from "@/types/insight";

import {
  getDashboardSummary,
  getTopCategories,
  getSentiments,
  getLatestInsight,
} from "@/services/api";

import type {
  DashboardSummary,
  TopCategory,
  SentimentData,
} from "@/types/dashboard";

export default function HomePage() {
  const [summary, setSummary] =
    useState<DashboardSummary | null>(
      null
    );

  const [categories, setCategories] =
    useState<TopCategory[]>([]);

  const [sentiments, setSentiments] =
    useState<SentimentData[]>([]);

  const [insight, setInsight] =
  useState<Insight | null>(null);

  const loadData = async () => {
    const [
      summaryData,
      categoryData,
      sentimentData,
      latestInsight,
    ] = await Promise.all([
      getDashboardSummary(),
      getTopCategories(),
      getSentiments(),
      getLatestInsight(),
    ]);

    setSummary(summaryData);

    setCategories(
      categoryData.data ?? []
    );

    setSentiments(
      sentimentData.data ?? []
    );

    setInsight(latestInsight);
  };

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    void loadData();
  }, []);

  if (!summary) {
    return (
      <div className="p-10">
        Loading...
      </div>
    );
  }

  return (
    <AppShell>
      <section className="rounded-3xl border border-slate-200 bg-white/90 p-6 shadow-sm backdrop-blur md:p-8">
        <p className="text-sm uppercase tracking-[0.25em] text-blue-600">Overview</p>
        <div className="mt-3 flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <h1 className="text-3xl font-bold text-slate-900 md:text-4xl">InsightDesk Dashboard</h1>
            <p className="mt-2 max-w-2xl text-slate-500">Pantau keluhan, sentimen, dan insight AI dalam satu tampilan modern yang siap dipakai.</p>
          </div>
          <div className="rounded-2xl bg-gradient-to-r from-blue-600 to-cyan-500 px-4 py-3 text-sm text-white shadow-lg">Live analytics • backend-ready</div>
        </div>
      </section>

      <section className="rounded-3xl border border-slate-200 bg-white/90 p-6 shadow-sm backdrop-blur md:p-8">
        <SummaryCards data={summary} />

        <div className="mt-8 grid gap-6 lg:grid-cols-2">
          <TopCategoriesChart data={categories} />
          <SentimentChart data={sentiments} />
        </div>

        {insight && (
          <div className="mt-8">
            <InsightCard content={insight.content ?? ""} />
          </div>
        )}
      </section>
    </AppShell>
  );
}