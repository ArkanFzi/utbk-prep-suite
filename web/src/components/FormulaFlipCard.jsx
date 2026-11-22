import React, { useState } from 'react';
import { Lightbulb, ChevronLeft, ChevronRight, RotateCw, Check, Sparkles } from 'lucide-react';
import { STARTER_FORMULAS } from '../data/starterFormulas';

export default function FormulaFlipCard() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  const formula = STARTER_FORMULAS[currentIndex] || STARTER_FORMULAS[0];

  const handleNext = () => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1) % STARTER_FORMULAS.length);
  };

  const handlePrev = () => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 + STARTER_FORMULAS.length) % STARTER_FORMULAS.length);
  };

  return (
    <div className="bg-surface rounded-2xl border border-borderSubtle p-5 shadow-lg flex flex-col justify-between">
      {/* Card Top Navigation */}
      <div className="flex items-center justify-between pb-3 border-b border-borderSubtle">
        <div className="flex items-center gap-2">
          <Lightbulb className="w-4 h-4 text-amber-400" />
          <h3 className="font-semibold text-sm text-gray-200">Formula & Trik of the Day</h3>
        </div>
        <div className="flex items-center gap-1 text-xs text-gray-400">
          <span>{currentIndex + 1}</span>
          <span>/</span>
          <span>{STARTER_FORMULAS.length}</span>
        </div>
      </div>

      {/* 3D Flip Card Container */}
      <div
        onClick={() => setIsFlipped(!isFlipped)}
        className="my-4 h-56 w-full cursor-pointer perspective-1000 select-none group"
      >
        <div
          className={`relative w-full h-full duration-500 transform-style-3d transition-transform ${
            isFlipped ? "rotate-y-180" : ""
          }`}
        >
          {/* FRONT SIDE */}
          <div className="absolute w-full h-full rounded-xl bg-surfaceHighlight/80 border border-borderSubtle p-4 flex flex-col justify-between backface-hidden shadow-inner hover:border-gray-600 transition-colors">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">
                  {formula.subtest} • {formula.tag}
                </span>
                <span className="text-[11px] text-gray-500 flex items-center gap-1 group-hover:text-amber-400 transition-colors">
                  <RotateCw className="w-3 h-3" /> Klik untuk jawaban
                </span>
              </div>
              <p className="text-sm sm:text-base font-semibold text-gray-100 leading-relaxed mt-2">
                {formula.front}
              </p>
            </div>
            <div className="flex items-center justify-between text-xs text-gray-400 pt-2 border-t border-borderSubtle/50">
              <span className="italic">Uji ingatan rumusmu</span>
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
            </div>
          </div>

          {/* BACK SIDE */}
          <div className="absolute w-full h-full rounded-xl bg-gradient-to-br from-gray-900 to-surfaceHighlight border border-emerald-500/30 p-4 flex flex-col justify-between backface-hidden rotate-y-180 shadow-lg">
            <div>
              <div className="flex items-center justify-between mb-2">
                <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                  Solusi & Trik Cepat
                </span>
                <span className="text-[11px] text-emerald-400 flex items-center gap-1">
                  <Check className="w-3 h-3" /> FSRS Memory
                </span>
              </div>
              <p className="text-xs sm:text-sm text-gray-200 whitespace-pre-line leading-relaxed font-mono">
                {formula.back}
              </p>
            </div>
            <div className="text-[11px] text-gray-500 pt-2 border-t border-borderSubtle/50 text-right">
              Klik kartu untuk membalik kembali
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Card Controls */}
      <div className="flex items-center justify-between pt-2 border-t border-borderSubtle">
        <button
          onClick={handlePrev}
          className="flex items-center gap-1 px-3 py-1.5 rounded-lg bg-surfaceHighlight hover:bg-gray-800 text-gray-300 text-xs font-medium border border-borderSubtle transition-all active:scale-95"
        >
          <ChevronLeft className="w-3.5 h-3.5" />
          <span>Sebelumnya</span>
        </button>

        <button
          onClick={() => setIsFlipped(!isFlipped)}
          className="text-xs text-gray-400 hover:text-white flex items-center gap-1 transition-colors"
        >
          <RotateCw className="w-3 h-3" />
          <span>Balik</span>
        </button>

        <button
          onClick={handleNext}
          className="flex items-center gap-1 px-3 py-1.5 rounded-lg bg-surfaceHighlight hover:bg-gray-800 text-gray-300 text-xs font-medium border border-borderSubtle transition-all active:scale-95"
        >
          <span>Berikutnya</span>
          <ChevronRight className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
}
