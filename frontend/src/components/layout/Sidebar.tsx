"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

import {
  LayoutDashboard,
  FileText,
  BrainCircuit,
} from "lucide-react";

export default function Sidebar() {
  const pathname = usePathname();

  const menuItems = [
    {
      name: "Dashboard",
      href: "/",
      icon: LayoutDashboard,
    },
    {
      name: "Complaints",
      href: "/complaints",
      icon: FileText,
    },
    {
      name: "Insights",
      href: "/insights",
      icon: BrainCircuit,
    },
  ];

  return (
    <aside
      className="
      hidden
      w-72
      min-h-screen
      border-r
      border-slate-200
      bg-white/90
      p-6
      shadow-sm
      backdrop-blur
      lg:block
      "
    >
      <div className="mb-10 rounded-3xl bg-gradient-to-r from-blue-600 to-cyan-500 p-4 text-white shadow-lg">
        <p className="text-xs uppercase tracking-[0.3em] text-blue-100">InsightDesk</p>
        <h1 className="mt-2 text-2xl font-bold">AI Complaint Hub</h1>
        <p className="mt-1 text-sm text-blue-100">Modern analytics untuk tim support dan operasional.</p>
      </div>

      <nav className="space-y-2">
        {menuItems.map((item) => {
          const Icon = item.icon;

          const isActive =
            pathname === item.href;

          return (
            <Link
              key={item.href}
              href={item.href}
              className={`
                flex
                items-center
                gap-3
                rounded-lg
                px-4
                py-3
                transition
                ${
                  isActive
                    ? "bg-blue-600 text-white"
                    : "text-gray-700 hover:bg-gray-100"
                }
              `}
            >
              <Icon size={20} />

              <span>
                {item.name}
              </span>
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}