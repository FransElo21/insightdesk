type Props = {
  content: string;
};

export default function InsightCard({ content }: Props) {
  return (
    <div className="rounded-xl border p-6">
      <h2 className="mb-4 text-xl font-semibold">Latest AI Insight</h2>
      <div className="whitespace-pre-wrap">{content}</div>
    </div>
  );
}
