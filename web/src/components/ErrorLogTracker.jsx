import React, { useState, useEffect } from 'react';
import { AlertCircle, Plus, Trash2, CheckCircle2, BarChart3, Filter } from 'lucide-react';

const STORAGE_KEY = 'utbk_error_logs_v1';

export default function ErrorLogTracker() {
  const [logs, setLogs] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      return saved ? JSON.parse(saved) : [
        {
          id: 1,
          date: new Date().toISOString().slice(0, 10),
          subtest: "PK",
          topic: "Pertidaksamaan Nilai Mutlak",
          rootCause: "Kurang Teliti",
          solution: "Lupa membalik tanda saat dikali bilangan negatif.",
          isResolved: false
        },
        {
          id: 2,
          date: new Date().toISOString().slice(0, 10),
          subtest: "PM",
          topic: "Aritmatika Sosial Diskon Bertingkat",
          rootCause: "Konsep Dasar",
          solution: "Diskon bertingkat 50%+20% adalah 60%, bukan 70%. Gunakan (1-d1)(1-d2).",
          isResolved: true
        }
      ];
    } catch {
      return [];
    }
  });

  const [form, setForm] = useState({
    subtest: "PK",
    topic: "",
    rootCause: "Konsep Dasar",
    solution: ""
  });

  const [filterSubtest, setFilterSubtest] = useState("ALL");

  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(logs));
  }, [logs]);

  const handleAdd = (e) => {
    e.preventDefault();
    if (!form.topic.trim()) return;

    const newLog = {
      id: Date.now(),
      date: new Date().toISOString().slice(0, 10),
      subtest: form.subtest,
      topic: form.topic.trim(),
      rootCause: form.rootCause,
      solution: form.solution.trim() || "-",
      isResolved: false
    };

    setLogs([newLog, ...logs]);
    setForm({
      subtest: "PK",
      topic: "",
      rootCause: "Konsep Dasar",
      solution: ""
    });
  };

  const handleDelete = (id) => {
    setLogs(logs.filter((l) => l.id !== id));
  };

  const handleToggleResolve = (id) => {
    setLogs(
      logs.map((l) => (l.id === id ? { ...l, isResolved: !l.isResolved } : l))
    );
  };

  // Weakness distribution calculation
  const totalLogs = logs.length;
  const countByCause = {
    "Konsep Dasar": logs.filter((l) => l.rootCause === "Konsep Dasar").length,
    "Kurang Teliti": logs.filter((l) => l.rootCause === "Kurang Teliti").length,
    "Kehabisan Waktu": logs.filter((l) => l.rootCause === "Kehabisan Waktu").length,
  };

  const filteredLogs = filterSubtest === "ALL"
    ? logs
    : logs.filter((l) => l.subtest === filterSubtest);

  return (
    <div className="bg-surface rounded-2xl border border-borderSubtle p-5 shadow-lg">
      <div className="flex flex-wrap items-center justify-between pb-3 border-b border-borderSubtle gap-2">
        <div className="flex items-center gap-2">
          <AlertCircle className="w-4 h-4 text-rose-400" />
          <h3 className="font-semibold text-sm text-gray-200">Error Log & Evaluasi Soal Salah</h3>
        </div>
        <span className="text-xs text-gray-400">
          Total Terdata: <span className="font-bold text-gray-100">{totalLogs} Soal</span>
        </span>
      </div>

      {/* Visual Weakness Bar Chart */}
      <div className="my-4 p-3 rounded-xl bg-surfaceHighlight/70 border border-borderSubtle">
        <div className="flex items-center gap-1.5 text-xs font-semibold text-gray-300 mb-2">
          <BarChart3 className="w-3.5 h-3.5 text-blue-400" />
          <span>Distribusi Akar Masalah (Root Cause)</span>
        </div>
        <div className="grid grid-cols-3 gap-2 text-center text-xs">
          <div className="bg-red-500/10 border border-red-500/20 p-2 rounded-lg">
            <span className="text-[11px] text-red-400 font-semibold block">Konsep Dasar</span>
            <span className="text-base font-bold text-white">{countByCause["Konsep Dasar"]}</span>
          </div>
          <div className="bg-amber-500/10 border border-amber-500/20 p-2 rounded-lg">
            <span className="text-[11px] text-amber-400 font-semibold block">Kurang Teliti</span>
            <span className="text-base font-bold text-white">{countByCause["Kurang Teliti"]}</span>
          </div>
          <div className="bg-blue-500/10 border border-blue-500/20 p-2 rounded-lg">
            <span className="text-[11px] text-blue-400 font-semibold block">Habis Waktu</span>
            <span className="text-base font-bold text-white">{countByCause["Kehabisan Waktu"]}</span>
          </div>
        </div>
      </div>

      {/* Input Form */}
      <form onSubmit={handleAdd} className="space-y-3 bg-surfaceHighlight/40 p-3 rounded-xl border border-borderSubtle/60">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
          <div>
            <label className="text-[11px] text-gray-400 font-medium block mb-1">Subtes</label>
            <select
              value={form.subtest}
              onChange={(e) => setForm({ ...form, subtest: e.target.value })}
              className="w-full bg-surface border border-borderSubtle rounded-lg px-2.5 py-1.5 text-xs text-gray-200 focus:outline-none focus:border-red-500"
            >
              <option value="PK">PK (Pengetahuan Kuantitatif)</option>
              <option value="PU">PU (Penalaran Umum)</option>
              <option value="PM">PM (Penalaran Matematika)</option>
              <option value="Literasi">Literasi (Bahasa)</option>
            </select>
          </div>

          <div>
            <label className="text-[11px] text-gray-400 font-medium block mb-1">Akar Masalah</label>
            <select
              value={form.rootCause}
              onChange={(e) => setForm({ ...form, rootCause: e.target.value })}
              className="w-full bg-surface border border-borderSubtle rounded-lg px-2.5 py-1.5 text-xs text-gray-200 focus:outline-none focus:border-red-500"
            >
              <option value="Konsep Dasar">Konsep Dasar (Belum Paham)</option>
              <option value="Kurang Teliti">Kurang Teliti (Blunder Hitung)</option>
              <option value="Kehabisan Waktu">Kehabisan Waktu</option>
            </select>
          </div>

          <div>
            <label className="text-[11px] text-gray-400 font-medium block mb-1">Topik / Soal</label>
            <input
              type="text"
              placeholder="Misal: Eksponen, Silogisme..."
              value={form.topic}
              onChange={(e) => setForm({ ...form, topic: e.target.value })}
              className="w-full bg-surface border border-borderSubtle rounded-lg px-2.5 py-1.5 text-xs text-gray-200 focus:outline-none focus:border-red-500"
              required
            />
          </div>
        </div>

        <div>
          <label className="text-[11px] text-gray-400 font-medium block mb-1">Catatan Solusi / Trik Cepat</label>
          <input
            type="text"
            placeholder="Tulis kunci rumus atau trik agar tidak salah lagi..."
            value={form.solution}
            onChange={(e) => setForm({ ...form, solution: e.target.value })}
            className="w-full bg-surface border border-borderSubtle rounded-lg px-2.5 py-1.5 text-xs text-gray-200 focus:outline-none focus:border-red-500"
          />
        </div>

        <button
          type="submit"
          className="w-full flex items-center justify-center gap-1.5 bg-red-600 hover:bg-red-500 text-white font-semibold text-xs py-2 rounded-lg transition-all shadow-md active:scale-95"
        >
          <Plus className="w-3.5 h-3.5" />
          <span>Tambah ke Error Log</span>
        </button>
      </form>

      {/* Filter and List */}
      <div className="mt-4">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-1 text-xs text-gray-400">
            <Filter className="w-3 h-3" />
            <span>Filter:</span>
          </div>
          <div className="flex gap-1 text-[11px]">
            {["ALL", "PK", "PU", "PM", "Literasi"].map((tab) => (
              <button
                key={tab}
                onClick={() => setFilterSubtest(tab)}
                className={`px-2 py-0.5 rounded transition-all ${
                  filterSubtest === tab
                    ? "bg-red-600 text-white font-semibold"
                    : "bg-surfaceHighlight text-gray-400 hover:text-white"
                }`}
              >
                {tab}
              </button>
            ))}
          </div>
        </div>

        <div className="space-y-2 max-h-60 overflow-y-auto pr-1">
          {filteredLogs.length === 0 ? (
            <p className="text-center text-xs text-gray-500 py-6">
              Belum ada soal salah tercatat. Mantap!
            </p>
          ) : (
            filteredLogs.map((item) => (
              <div
                key={item.id}
                className={`p-3 rounded-xl border transition-all flex items-start justify-between gap-2 ${
                  item.isResolved
                    ? "bg-surfaceHighlight/30 border-borderSubtle/50 opacity-60"
                    : "bg-surfaceHighlight/80 border-borderSubtle"
                }`}
              >
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-surface border border-borderSubtle text-gray-300">
                      {item.subtest}
                    </span>
                    <span className="text-[10px] px-1.5 py-0.5 rounded bg-red-500/10 text-red-400 border border-red-500/20">
                      {item.rootCause}
                    </span>
                    <span className="text-[10px] text-gray-500">{item.date}</span>
                  </div>
                  <p className={`text-xs font-semibold ${item.isResolved ? "line-through text-gray-400" : "text-gray-100"}`}>
                    {item.topic}
                  </p>
                  <p className="text-[11px] text-gray-400 italic">
                    💡 {item.solution}
                  </p>
                </div>

                <div className="flex items-center gap-1 shrink-0">
                  <button
                    onClick={() => handleToggleResolve(item.id)}
                    className={`p-1.5 rounded-lg border transition-colors ${
                      item.isResolved
                        ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                        : "bg-surface text-gray-400 hover:text-white border-borderSubtle"
                    }`}
                    title={item.isResolved ? "Tandai Belum Paham" : "Tandai Sudah Paham"}
                  >
                    <CheckCircle2 className="w-3.5 h-3.5" />
                  </button>
                  <button
                    onClick={() => handleDelete(item.id)}
                    className="p-1.5 rounded-lg bg-surface text-gray-400 hover:text-red-400 border border-borderSubtle transition-colors"
                    title="Hapus"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}
