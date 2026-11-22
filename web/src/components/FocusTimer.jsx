import React, { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw, CheckCircle2, Music, Bell } from 'lucide-react';

export default function FocusTimer({ durationMinutes = 90, onSessionComplete, subtest = "Pengetahuan Kuantitatif" }) {
  const [timeLeft, setTimeLeft] = useState(durationMinutes * 60);
  const [isRunning, setIsRunning] = useState(false);
  const [isCompleted, setIsCompleted] = useState(false);
  const timerRef = useRef(null);

  const totalSeconds = durationMinutes * 60;
  const progressPercent = ((totalSeconds - timeLeft) / totalSeconds) * 100;

  // Sound generator with Web Audio API (Offline, Zero external audio file needed)
  const playChime = (frequency = 587.33, duration = 0.5) => {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(frequency, ctx.currentTime);
      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {
      console.log('Web audio error:', e);
    }
  };

  useEffect(() => {
    if (isRunning && timeLeft > 0) {
      timerRef.current = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev <= 1) {
            clearInterval(timerRef.current);
            setIsRunning(false);
            setIsCompleted(true);
            playChime(880, 1.2); // Success high chime
            if (onSessionComplete) onSessionComplete();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    } else {
      clearInterval(timerRef.current);
    }
    return () => clearInterval(timerRef.current);
  }, [isRunning, timeLeft]);

  const toggleTimer = () => {
    if (!isRunning) {
      playChime(523.25, 0.3); // C5 chime on start
    }
    setIsRunning(!isRunning);
  };

  const resetTimer = () => {
    setIsRunning(false);
    setTimeLeft(totalSeconds);
    setIsCompleted(false);
  };

  const markManualDone = () => {
    setIsRunning(false);
    setIsCompleted(true);
    playChime(659.25, 0.8);
    if (onSessionComplete) onSessionComplete();
  };

  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;
  const formattedTime = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

  // Circular SVG progress math
  const radius = 105;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (progressPercent / 100) * circumference;

  return (
    <div className="bg-surface rounded-2xl border border-borderSubtle p-6 flex flex-col items-center shadow-xl relative overflow-hidden">
      {/* Decorative background glow */}
      <div className="absolute -top-16 -left-16 w-48 h-48 bg-red-600/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute -bottom-16 -right-16 w-48 h-48 bg-blue-600/10 rounded-full blur-3xl pointer-events-none" />

      <div className="flex items-center justify-between w-full mb-4">
        <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-gray-400">
          <Bell className="w-3.5 h-3.5 text-red-400" />
          <span>Deep Focus Timer</span>
        </div>
        <span className="text-xs px-2.5 py-0.5 rounded-full font-medium bg-surfaceHighlight text-gray-300 border border-borderSubtle">
          {subtest}
        </span>
      </div>

      {/* Circular SVG Timer */}
      <div className="relative my-2 flex items-center justify-center">
        <svg className="w-60 h-60 transform -rotate-90">
          {/* Background Track */}
          <circle
            cx="120"
            cy="120"
            r={radius}
            stroke="#1A202C"
            strokeWidth="12"
            fill="transparent"
          />
          {/* Active Progress */}
          <circle
            cx="120"
            cy="120"
            r={radius}
            stroke={isCompleted ? "#10B981" : "#EF4444"}
            strokeWidth="12"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            fill="transparent"
            className="transition-all duration-500 ease-linear"
          />
        </svg>

        {/* Center Display */}
        <div className="absolute flex flex-col items-center text-center">
          <span className="font-mono text-5xl font-bold tracking-tight text-white">
            {formattedTime}
          </span>
          <span className="text-xs text-gray-400 font-medium mt-1">
            {isCompleted ? "🎉 Selesai!" : isRunning ? "Fokus Sedang Berjalan" : "Siap Mulai"}
          </span>
        </div>
      </div>

      {/* Control Buttons */}
      <div className="flex items-center gap-3 mt-6">
        <button
          onClick={toggleTimer}
          className={`flex items-center gap-2 px-6 py-2.5 rounded-xl font-semibold text-sm transition-all shadow-md active:scale-95 ${
            isRunning
              ? "bg-amber-600 hover:bg-amber-500 text-white shadow-amber-900/30"
              : "bg-red-600 hover:bg-red-500 text-white shadow-red-900/30"
          }`}
        >
          {isRunning ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4 fill-white" />}
          <span>{isRunning ? "Jeda" : "Mulai (90m)"}</span>
        </button>

        <button
          onClick={resetTimer}
          className="p-2.5 rounded-xl bg-surfaceHighlight hover:bg-gray-800 text-gray-400 hover:text-white border border-borderSubtle transition-all active:scale-95"
          title="Reset Timer"
        >
          <RotateCcw className="w-4 h-4" />
        </button>

        <button
          onClick={markManualDone}
          className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-semibold transition-all active:scale-95"
          title="Tandai Selesai Langsung"
        >
          <CheckCircle2 className="w-4 h-4" />
          <span>Selesai</span>
        </button>
      </div>

      <p className="text-[11px] text-gray-500 mt-4 flex items-center gap-1.5">
        <Music className="w-3.5 h-3.5 text-gray-400" />
        Tips: Putar Spotify Lo-Fi / 40Hz di laptop untuk konsentrasi penuh.
      </p>
    </div>
  );
}
