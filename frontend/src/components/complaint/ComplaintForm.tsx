"use client";

import { useState } from "react";

import {
  createComplaint
} from "@/services/api";

export default function ComplaintForm() {

  const [title, setTitle] =
    useState("");

  const [description,
    setDescription] =
    useState("");

  const [location,
    setLocation] =
    useState("");

  const [loading,
    setLoading] =
    useState(false);

  const handleSubmit =
    async (
      e: React.FormEvent
    ) => {

      e.preventDefault();

      setLoading(true);

      try {

        await createComplaint({
          title,
          description,
          location,
        });

        alert(
          "Complaint submitted successfully"
        );

        setTitle("");
        setDescription("");
        setLocation("");

      } catch {

        alert(
          "Failed to submit complaint"
        );

      } finally {

        setLoading(false);

      }
    };

  return (
    <form
      onSubmit={handleSubmit}
      className="
      rounded-3xl
      border
      bg-white
      p-8
      shadow-sm
      "
    >

      <h2
        className="
        mb-6
        text-2xl
        font-bold
        "
      >
        Create Complaint
      </h2>

      <div className="space-y-4">

        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) =>
            setTitle(
              e.target.value
            )
          }
          className="
          w-full
          rounded-xl
          border
          p-3
          "
          required
        />

        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) =>
            setDescription(
              e.target.value
            )
          }
          rows={5}
          className="
          w-full
          rounded-xl
          border
          p-3
          "
          required
        />

        <input
          type="text"
          placeholder="Location"
          value={location}
          onChange={(e) =>
            setLocation(
              e.target.value
            )
          }
          className="
          w-full
          rounded-xl
          border
          p-3
          "
          required
        />

        <button
          type="submit"
          disabled={loading}
          className="
          rounded-xl
          bg-blue-600
          px-5
          py-3
          text-white
          "
        >
          {loading
            ? "Submitting..."
            : "Submit Complaint"}
        </button>

      </div>

    </form>
  );
}