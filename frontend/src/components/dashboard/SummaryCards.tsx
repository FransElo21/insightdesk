"use client";

import { DashboardSummary } from "@/types/dashboard";

type Props = {
  data: DashboardSummary;
};

export default function SummaryCards({
  data,
}: Props) {
  const topCategory = Object.entries(
    data.categories
  ).sort(
    (a, b) => b[1] - a[1]
  )[0];

  const negativeCount =
    data.sentiments["Negatif"] || 0;

  const negativeRate =
    (
      negativeCount /
      data.total_complaints
    ) * 100;

  const cards = [
    {
      title: "Total Complaints",
      value: data.total_complaints,
    },
    {
      title: "Top Category",
      value: topCategory?.[0] ?? "-",
    },
    {
      title: "Negative Rate",
      value: `${negativeRate.toFixed(
        1
      )}%`,
    },
    {
      title: "Categories",
      value: Object.keys(
        data.categories
      ).length,
    },
  ];

  return (
    <div
      className="
      grid
      gap-6
      md:grid-cols-2
      xl:grid-cols-4
      "
    >
      {cards.map((card) => (
        <div
          key={card.title}
          className="
          rounded-3xl
          border
          border-slate-200
          bg-white/90
          p-6
          shadow-sm
          shadow-blue-100/60
          backdrop-blur
          transition
          hover:-translate-y-0.5
          hover:border-blue-200
          hover:shadow-lg
          "
        >
          <p className="text-gray-500">
            {card.title}
          </p>

          <h2
            className="
            mt-3
            text-3xl
            font-bold
            "
          >
            {card.value}
          </h2>
        </div>
      ))}
    </div>
  );
}