"use client";

import Sidebar from "@/components/layout/Sidebar";

export default function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-transparent">
      <Sidebar />
      <main className="flex-1 p-6 md:p-8 lg:p-10">
        <div className="mx-auto flex max-w-7xl flex-col gap-8">{children}</div>
      </main>
    </div>
  );
}
