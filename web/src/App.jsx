import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import FocusTimer from './components/FocusTimer';
import TodayAgenda from './components/TodayAgenda';
import FormulaFlipCard from './components/FormulaFlipCard';
import ErrorLogTracker from './components/ErrorLogTracker';
import { LayoutDashboard, Timer, BookMarked, AlertCircle, Sparkles } from 'lucide-react';
import { WEEKDAY_SCHEDULE } from './data/scheduleData';

const PROGRESS_STORAGE_KEY = 'utbk_study_progress_v1';

export default function App() {
  const [activeTab, setActiveTab] = useState('dashboard'); // 'dashboard', 'timer', 'formulas', 'errors'
  const [isSessionDone, setIsSessionDone] = useState(false);
  const [streak, setStreak] = useState(14);
  const [completedCount, setCompletedCount] = useState(42);

  const today = new Date();
  const dayIndex = today.getDay();
  const currentSchedule = WEEKDAY_SCHEDULE[dayIndex] || WEEKDAY_SCHEDULE[1];

  useEffect(() => {
    try {
      const saved = localStorage.getItem(PROGRESS_STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        const todayStr = new Date().toISOString().slice(0, 10);
        if (parsed.completedDates && parsed.completedDates.includes(todayStr)) {
          setIsSessionDone(true);
        }
        if (parsed.streak) setStreak(parsed.streak);
        if (parsed.completedCount) setCompletedCount(parsed.completedCount);
      }
    } catch {
      // fallback
    }
  }, []);

  const handleToggleDone = () => {
    const todayStr = new Date().toISOString().slice(0, 10);
    const newStatus = !isSessionDone;
    setIsSessionDone(newStatus);

    try {
      const saved = localStorage.getItem(PROGRESS_STORAGE_KEY);
      const parsed = saved ? JSON.parse(saved) : { completedDates: [], streak: 14, completedCount: 42 };
      let dates = parsed.completedDates || [];
      if (newStatus) {
        if (!dates.includes(todayStr)) dates.push(todayStr);
        parsed.completedCount = (parsed.completedCount || 42) + 1;
        setCompletedCount(parsed.completedCount);
      } else {
        dates = dates.filter(d => d !== todayStr);
        parsed.completedCount = Math.max(0, (parsed.completedCount || 42) - 1);
        setCompletedCount(parsed.completedCount);
      }
      parsed.completedDates = dates;
      localStorage.setItem(PROGRESS_STORAGE_KEY, JSON.stringify(parsed));
    } catch {
      // fallback
    }
  };

  return (
    <div className="min-h-screen bg-canvas text-gray-100 flex flex-col selection:bg-red-500/20">
      {/* Top Header */}
      <Header streak={streak} completedSessions={completedCount} />

      {/* Main Content Area */}
      <main className="flex-1 max-w-5xl w-full mx-auto px-4 py-6 pb-24 md:pb-8">
        {/* Desktop / Tablet Sub-navigation Tabs */}
        <div className="flex items-center justify-between mb-6 pb-3 border-b border-borderSubtle">
          <div className="flex items-center gap-1 sm:gap-2">
            <button
              onClick={() => setActiveTab('dashboard')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                activeTab === 'dashboard'
                  ? 'bg-red-600 text-white shadow-md shadow-red-900/30'
                  : 'bg-surface hover:bg-gray-800 text-gray-400 hover:text-white border border-borderSubtle'
              }`}
            >
              <LayoutDashboard className="w-4 h-4" />
              <span>Dashboard</span>
            </button>

            <button
              onClick={() => setActiveTab('timer')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                activeTab === 'timer'
                  ? 'bg-red-600 text-white shadow-md shadow-red-900/30'
                  : 'bg-surface hover:bg-gray-800 text-gray-400 hover:text-white border border-borderSubtle'
              }`}
            >
              <Timer className="w-4 h-4" />
              <span>Timer Fokus</span>
            </button>

            <button
              onClick={() => setActiveTab('formulas')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                activeTab === 'formulas'
                  ? 'bg-red-600 text-white shadow-md shadow-red-900/30'
                  : 'bg-surface hover:bg-gray-800 text-gray-400 hover:text-white border border-borderSubtle'
              }`}
            >
              <BookMarked className="w-4 h-4" />
              <span>Rumus of the Day</span>
            </button>

            <button
              onClick={() => setActiveTab('errors')}
              className={`flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all ${
                activeTab === 'errors'
                  ? 'bg-red-600 text-white shadow-md shadow-red-900/30'
                  : 'bg-surface hover:bg-gray-800 text-gray-400 hover:text-white border border-borderSubtle'
              }`}
            >
              <AlertCircle className="w-4 h-4" />
              <span>Error Log</span>
            </button>
          </div>

          <div className="hidden sm:flex items-center gap-1.5 text-xs text-gray-400">
            <Sparkles className="w-3.5 h-3.5 text-amber-400" />
            <span>Fokus S1/D4 Informatika</span>
          </div>
        </div>

        {/* Tab Views */}
        {activeTab === 'dashboard' && (
          <div className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
              {/* Left Column: Agenda & Timer */}
              <div className="lg:col-span-6 space-y-6 flex flex-col justify-between">
                <TodayAgenda isDone={isSessionDone} onToggleDone={handleToggleDone} />
                <FormulaFlipCard />
              </div>

              {/* Right Column: Focus Timer & Error Log */}
              <div className="lg:col-span-6 space-y-6">
                <FocusTimer
                  durationMinutes={currentSchedule.duration}
                  subtest={currentSchedule.code}
                  onSessionComplete={handleToggleDone}
                />
                <ErrorLogTracker />
              </div>
            </div>
          </div>
        )}

        {activeTab === 'timer' && (
          <div className="max-w-md mx-auto">
            <FocusTimer
              durationMinutes={currentSchedule.duration}
              subtest={currentSchedule.code}
              onSessionComplete={handleToggleDone}
            />
          </div>
        )}

        {activeTab === 'formulas' && (
          <div className="max-w-lg mx-auto">
            <FormulaFlipCard />
          </div>
        )}

        {activeTab === 'errors' && (
          <div className="max-w-2xl mx-auto">
            <ErrorLogTracker />
          </div>
        )}
      </main>

      {/* Mobile Bottom Navigation Bar */}
      <nav className="md:hidden fixed bottom-0 left-0 right-0 bg-surface/95 backdrop-blur-lg border-t border-borderSubtle z-50 px-2 py-2">
        <div className="grid grid-cols-4 gap-1">
          <button
            onClick={() => setActiveTab('dashboard')}
            className={`flex flex-col items-center justify-center py-1 rounded-xl text-[10px] font-medium transition-colors ${
              activeTab === 'dashboard' ? 'text-red-400 font-bold' : 'text-gray-400 hover:text-gray-200'
            }`}
          >
            <LayoutDashboard className="w-5 h-5 mb-0.5" />
            <span>Beranda</span>
          </button>

          <button
            onClick={() => setActiveTab('timer')}
            className={`flex flex-col items-center justify-center py-1 rounded-xl text-[10px] font-medium transition-colors ${
              activeTab === 'timer' ? 'text-red-400 font-bold' : 'text-gray-400 hover:text-gray-200'
            }`}
          >
            <Timer className="w-5 h-5 mb-0.5" />
            <span>Timer</span>
          </button>

          <button
            onClick={() => setActiveTab('formulas')}
            className={`flex flex-col items-center justify-center py-1 rounded-xl text-[10px] font-medium transition-colors ${
              activeTab === 'formulas' ? 'text-red-400 font-bold' : 'text-gray-400 hover:text-gray-200'
            }`}
          >
            <BookMarked className="w-5 h-5 mb-0.5" />
            <span>Rumus</span>
          </button>

          <button
            onClick={() => setActiveTab('errors')}
            className={`flex flex-col items-center justify-center py-1 rounded-xl text-[10px] font-medium transition-colors ${
              activeTab === 'errors' ? 'text-red-400 font-bold' : 'text-gray-400 hover:text-gray-200'
            }`}
          >
            <AlertCircle className="w-5 h-5 mb-0.5" />
            <span>Error Log</span>
          </button>
        </div>
      </nav>
    </div>
  );
}
