"use client";

import { Complaint } from "@/types/complaint";

type Props = {
  complaints: Complaint[];
};

export default function ComplaintTable({
  complaints,
}: Props) {

  return (
    <div className="overflow-hidden rounded-xl border">

      <table className="w-full">

        <thead>

          <tr className="border-b bg-gray-100">

            <th className="p-4 text-left">
              Title
            </th>

            <th className="p-4 text-left">
              Category
            </th>

            <th className="p-4 text-left">
              Sentiment
            </th>

            <th className="p-4 text-left">
              Location
            </th>

            <th className="p-4 text-left">
              Date
            </th>

          </tr>

        </thead>

        <tbody>

          {complaints.map(
            (complaint) => (

              <tr
                key={complaint.id}
                className="border-b"
              >

                <td className="p-4">
                  {complaint.title}
                </td>

                <td className="p-4">
                  {complaint.category}
                </td>

                <td className="p-4">

                  <span
                    className="
                    rounded-full
                    px-3
                    py-1
                    text-sm
                    bg-gray-100
                  "
                  >
                    {complaint.sentiment}
                  </span>

                </td>

                <td className="p-4">
                  {complaint.location}
                </td>

                <td className="p-4">
                  {new Date(
                    complaint.created_at
                  ).toLocaleDateString()}
                </td>

              </tr>

            )
          )}

        </tbody>

      </table>

    </div>
  );
}