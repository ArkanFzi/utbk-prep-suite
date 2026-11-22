import React from 'react';
import { Target, Flame, Calendar, Award } from 'lucide-react';
import { getCountdownDays } from '../data/scheduleData';

export default function Header({ streak = 14, completedSessions = 42 }) {
  const daysLeft = getCountdownDays();

  return (
    <header className="w-full bg-surface border-b border-borderSubtle sticky top-0 z-40 backdrop-blur-md bg-surface/90">
      <div className="max-w-5xl mx-auto px-4 py-3 flex flex-wrap items-center justify-between gap-3">
        {/* Left: Brand & Target */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-red-600 to-rose-700 flex items-center justify-center text-white shadow-lg shadow-red-900/30">
            <Target className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-bold text-base text-gray-100 tracking-tight">UTBK 2027</span>
              <span className="text-[10px] uppercase font-semibold px-2 py-0.5 rounded-full bg-red-500/10 text-red-400 border border-red-500/20">
                SMK RPL
              </span>
            </div>
            <p className="text-xs text-gray-400 font-medium">
              Target: <span className="text-gray-200">S1/D4 Informatika (ITS • UB • POLINEMA)</span>
            </p>
          </div>
        </div>

        {/* Right: Countdown & Stats */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Countdown Badge */}
          <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-red-950/40 border border-red-600/30 text-red-300 shadow-sm">
            <Calendar className="w-4 h-4 text-red-400" />
            <span className="text-xs font-semibold">H-{daysLeft} Hari</span>
          </div>

          {/* Streak Badge */}
          <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-amber-950/30 border border-amber-600/30 text-amber-300 shadow-sm">
            <Flame className="w-4 h-4 text-amber-400 animate-pulse" />
            <span className="text-xs font-semibold">{streak} Hari Streak</span>
          </div>

          {/* Total Sessions */}
          <div className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-surfaceHighlight border border-borderSubtle text-gray-300">
            <Award className="w-4 h-4 text-emerald-400" />
            <span className="text-xs font-medium">{completedSessions} Selesai</span>
          </div>
        </div>
      </div>
    </header>
  );
}
