"use client";

import { useEffect, useState } from "react";

import AppShell from "@/components/layout/AppShell";
import InsightCard from "@/components/insight/InsightCard";
import InsightHistoryCard from "@/components/insight/InsightHistoryCard";

import {
  generateInsight,
  getInsights,
} from "@/services/api";

import { Insight } from "@/types/insight";

export default function InsightsPage() {

  const [insights, setInsights] =
    useState<Insight[]>([]);

  const [days, setDays] =
    useState<number>(30);

  const [loading, setLoading] =
    useState(false);

  const [pageLoading, setPageLoading] =
    useState(true);

  const loadData = async () => {

    try {

      const data =
        await getInsights();

      setInsights(data);

    } catch (error) {

      console.error(
        "Failed to load insights:",
        error
      );

    } finally {

      setPageLoading(false);

    }
  };

  useEffect(() => {

    void loadData();

  }, []);

  const handleGenerate =
    async () => {

      try {

        setLoading(true);

        await generateInsight(
          days
        );

        await loadData();

      } catch (error) {

        console.error(
          "Failed to generate insight:",
          error
        );

      } finally {

        setLoading(false);

      }
    };

  if (pageLoading) {

    return (
      <AppShell>
        <div className="p-10">
          Loading insights...
        </div>
      </AppShell>
    );
  }

  return (
    <AppShell>

      <section
        className="
        rounded-3xl
        border
        border-slate-200
        bg-white
        p-8
        shadow-sm
        "
      >

        <div
          className="
          flex
          flex-col
          gap-4
          lg:flex-row
          lg:items-center
          lg:justify-between
          "
        >

          <div>

            <p
              className="
              text-sm
              uppercase
              tracking-widest
              text-blue-600
              "
            >
              AI Analytics
            </p>

            <h1
              className="
              mt-2
              text-3xl
              font-bold
              text-slate-900
              "
            >
              AI Insights
            </h1>

            <p
              className="
              mt-2
              text-slate-500
              "
            >
              Generate AI-powered analysis from complaint data.
            </p>

          </div>

          <div
            className="
            flex
            flex-col
            gap-3
            sm:flex-row
            "
          >

            <select
              value={days}
              onChange={(e) =>
                setDays(
                  Number(
                    e.target.value
                  )
                )
              }
              className="
              rounded-xl
              border
              border-slate-300
              px-4
              py-3
              "
            >

              <option value={7}>
                Last 7 Days
              </option>

              <option value={30}>
                Last 30 Days
              </option>

            </select>

            <button
              onClick={
                handleGenerate
              }
              disabled={loading}
              className="
              rounded-xl
              bg-blue-600
              px-5
              py-3
              font-medium
              text-white
              transition
              hover:bg-blue-700
              disabled:opacity-50
              "
            >
              {loading
                ? "Generating..."
                : "Generate Insight"}
            </button>

          </div>

        </div>

      </section>

      {insights.length > 0 && (

        <section
          className="
          mt-6
          "
        >

          <InsightCard
            content={
              insights[0].content
            }
          />

        </section>

      )}

      <section
        className="
        mt-6
        "
      >

        <div
          className="
          mb-4
          "
        >

          <h2
            className="
            text-xl
            font-semibold
            "
          >
            Insight History
          </h2>

          <p
            className="
            text-sm
            text-slate-500
            "
          >
            Previously generated AI insights.
          </p>

        </div>

        <div
          className="
          grid
          gap-4
          "
        >

          {insights.map(
            (insight) => (

              <InsightHistoryCard
                key={insight.id}
                insight={insight}
              />

            )
          )}

        </div>

      </section>

    </AppShell>
  );
}