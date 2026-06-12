import { Complaint } from "@/types/complaint";

type Props = {
  complaint: Complaint;
};

export default function ComplaintCard({
  complaint,
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
      <div className="flex items-start justify-between">
        <h3 className="text-lg font-semibold">
          {complaint.title}
        </h3>

        <span
          className="
          rounded-full
          bg-red-100
          px-3
          py-1
          text-sm
          "
        >
          {complaint.sentiment}
        </span>
      </div>

      <p className="mt-3 text-slate-600">
        {complaint.description}
      </p>

      <div
        className="
        mt-4
        flex
        gap-2
        flex-wrap
        "
      >
        <span
          className="
          rounded-full
          bg-blue-100
          px-3
          py-1
          text-sm
          "
        >
          {complaint.category}
        </span>

        <span
          className="
          rounded-full
          bg-slate-100
          px-3
          py-1
          text-sm
          "
        >
          {complaint.location}
        </span>
      </div>
    </div>
  );
}