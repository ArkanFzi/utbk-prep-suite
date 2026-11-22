import React from 'react';
import { Calendar, Clock, BookOpen, Target, CheckCircle2 } from 'lucide-react';
import { WEEKDAY_SCHEDULE } from '../data/scheduleData';

export default function TodayAgenda({ isDone = false, onToggleDone }) {
  const today = new Date();
  const dayIndex = today.getDay(); // 0 is Sunday, 1 is Monday ...
  const agenda = WEEKDAY_SCHEDULE[dayIndex] || WEEKDAY_SCHEDULE[1];

  const dateFormatted = today.toLocaleDateString('id-ID', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });

  return (
    <div className="bg-surface rounded-2xl border border-borderSubtle p-5 shadow-lg flex flex-col justify-between">
      <div>
        {/* Card Header */}
        <div className="flex items-center justify-between pb-3 border-b border-borderSubtle">
          <div className="flex items-center gap-2">
            <Calendar className="w-4 h-4 text-blue-400" />
            <h3 className="font-semibold text-sm text-gray-200">Agenda Belajar Hari Ini</h3>
          </div>
          <span className="text-xs text-gray-400 font-medium">{dateFormatted}</span>
        </div>

        {/* Subtest & Time */}
        <div className="mt-4 flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <span className={`text-xs font-bold px-2.5 py-1 rounded-lg border ${agenda.badgeBg}`}>
              {agenda.code}
            </span>
            <span className="font-bold text-base text-gray-100">{agenda.subtest}</span>
          </div>

          <div className="flex items-center gap-1.5 text-xs text-gray-400 bg-surfaceHighlight px-2.5 py-1 rounded-lg border border-borderSubtle">
            <Clock className="w-3.5 h-3.5 text-amber-400" />
            <span>{agenda.time}</span>
          </div>
        </div>

        {/* Topic & Target */}
        <div className="mt-4 space-y-3">
          <div className="bg-surfaceHighlight/60 p-3 rounded-xl border border-borderSubtle/60">
            <div className="flex items-center gap-1.5 text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1">
              <BookOpen className="w-3.5 h-3.5 text-blue-400" />
              <span>Materi Fokus</span>
            </div>
            <p className="text-sm font-medium text-gray-100 leading-relaxed">
              {agenda.topic}
            </p>
          </div>

          <div className="bg-surfaceHighlight/60 p-3 rounded-xl border border-borderSubtle/60">
            <div className="flex items-center gap-1.5 text-xs font-semibold text-gray-400 uppercase tracking-wider mb-1">
              <Target className="w-3.5 h-3.5 text-red-400" />
              <span>Target Sesi</span>
            </div>
            <p className="text-xs text-gray-300 leading-relaxed">
              {agenda.target}
            </p>
          </div>
        </div>
      </div>

      {/* Completion status bar */}
      <div className="mt-5 pt-3 border-t border-borderSubtle flex items-center justify-between">
        <span className="text-xs text-gray-400">
          Status sesi: <span className={isDone ? "text-emerald-400 font-semibold" : "text-amber-400 font-semibold"}>
            {isDone ? "Sudah Selesai [DONE]" : "Belum Selesai [TODO]"}
          </span>
        </span>

        <button
          onClick={onToggleDone}
          className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all active:scale-95 ${
            isDone
              ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/30"
              : "bg-surfaceHighlight hover:bg-gray-800 text-gray-300 border border-borderSubtle"
          }`}
        >
          <CheckCircle2 className={`w-3.5 h-3.5 ${isDone ? "text-emerald-400" : "text-gray-400"}`} />
          <span>{isDone ? "Tandai Belum Selesai" : "Tandai Selesai"}</span>
        </button>
      </div>
    </div>
  );
}
