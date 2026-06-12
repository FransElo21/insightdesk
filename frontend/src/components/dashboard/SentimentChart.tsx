"use client";

import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";

const COLORS = ["#ef4444", "#22c55e", "#f59e0b"];

type Props = {
  data: {
    sentiment: string;
    count: number;
  }[];
};

export default function SentimentChart({ data }: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white/90 p-6 shadow-sm shadow-blue-100/60 backdrop-blur">
      <h2 className="mb-4 text-xl font-semibold text-slate-900">Sentiment Distribution</h2>

      <ResponsiveContainer width="100%" height={300}>
        <PieChart>
          <Pie data={data} dataKey="count" nameKey="sentiment" outerRadius={100}>
            {data.map((_, index) => (
              <Cell key={index} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
