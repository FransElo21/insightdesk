"use client";

import { useEffect, useState } from "react";

import Link from "next/link";

import AppShell from "@/components/layout/AppShell";

import ComplaintCard from "@/components/complaint/ComplaintCard";

import { getComplaints } from "@/services/api";

import { Complaint } from "@/types/complaint";

export default function ComplaintsPage() {

  const [complaints, setComplaints] =
    useState<Complaint[]>([]);

  const [loading, setLoading] =
    useState(true);

  const loadData = async () => {

    try {

      const data =
        await getComplaints();

      setComplaints(data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);

    }
  };

  useEffect(() => {

    void loadData();

  }, []);

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
          md:flex-row
          md:items-center
          md:justify-between
          "
        >

          <div>

            <h1
              className="
              text-3xl
              font-bold
              text-slate-900
              "
            >
              Complaints
            </h1>

            <p
              className="
              mt-2
              text-slate-500
              "
            >
              Monitor all complaints submitted by users.
            </p>

          </div>

          <Link
            href="/complaints/new"
            className="
            inline-flex
            items-center
            justify-center
            rounded-xl
            bg-blue-600
            px-5
            py-3
            font-medium
            text-white
            transition
            hover:bg-blue-700
            "
          >
            New Complaint
          </Link>

        </div>

      </section>

      <section
        className="
        mt-6
        grid
        gap-4
        "
      >

        {loading && (

          <div
            className="
            rounded-2xl
            border
            p-10
            text-center
            text-slate-500
            "
          >
            Loading complaints...
          </div>

        )}

        {!loading &&
          complaints.length === 0 && (

            <div
              className="
              rounded-2xl
              border
              border-dashed
              border-slate-300
              p-10
              text-center
              text-slate-500
              "
            >
              No complaints found.
            </div>

          )}

        {!loading &&
          complaints.map(
            (complaint) => (

              <ComplaintCard
                key={complaint.id}
                complaint={complaint}
              />

            )
          )}

      </section>

    </AppShell>
  );
}