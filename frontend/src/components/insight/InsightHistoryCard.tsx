import { Insight } from "@/types/insight";

type Props = {
  insight: Insight;
};

export default function InsightHistoryCard({
  insight,
}: Props) {

  return (
    <div
      className="
      rounded-2xl
      border
      border-slate-200
      bg-white
      p-5
      shadow-sm
      "
    >

      <div
        className="
        mb-4
        text-sm
        text-slate-500
        "
      >
        {new Date(
          insight.generated_at
        ).toLocaleString()}
      </div>

      <div
        className="
        whitespace-pre-wrap
        text-sm
        text-slate-700
        "
      >
        {insight.content}
      </div>

    </div>
  );
}