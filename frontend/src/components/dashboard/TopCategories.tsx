"use client";

import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

type Props = {
  data: {
    category: string;
    count: number;
  }[];
};

export default function TopCategoriesChart({ data }: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white/90 p-6 shadow-sm shadow-blue-100/60 backdrop-blur">
      <h2 className="mb-4 text-xl font-semibold text-slate-900">Top Categories</h2>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <XAxis dataKey="category" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="count" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
