
import React from 'react';
import { Calendar, MessageCircle } from 'lucide-react';

const CTASection: React.FC = () => {
  return (
    <section className="py-24 bg-slate-900 relative overflow-hidden">
      {/* Abstract background blobs */}
      <div className="absolute top-0 right-0 w-96 h-96 bg-primary-green/10 blur-[100px] rounded-full -mr-48 -mt-48"></div>
      <div className="absolute bottom-0 left-0 w-96 h-96 bg-blue-600/10 blur-[100px] rounded-full -ml-48 -mb-48"></div>

      <div className="max-w-4xl mx-auto px-4 text-center relative z-10">
        <h2 className="text-4xl lg:text-5xl font-extrabold text-white mb-8">
          ¿Listo para ordenar tu cuenta y volver a crecer en Mercado Libre?
        </h2>
        <p className="text-slate-400 text-xl mb-12 max-w-2xl mx-auto leading-relaxed">
          Conversemos sobre tu situación actual, revisemos tu cuenta y definamos si Creseller es el acompañamiento estratégico que necesitás.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button className="bg-primary-green text-slate-900 px-8 py-5 rounded-2xl font-black flex items-center justify-center gap-3 hover:bg-green-500 transition-all shadow-xl shadow-green-900/20">
            <Calendar className="w-6 h-6" />
            Agendar llamada de diagnóstico
          </button>
          <button className="bg-white/10 backdrop-blur-md text-white border border-white/20 px-8 py-5 rounded-2xl font-bold flex items-center justify-center gap-3 hover:bg-white/20 transition-all">
            <MessageCircle className="w-6 h-6 text-green-400" />
            Escribir por WhatsApp
          </button>
        </div>
      </div>
    </section>
  );
};

export default CTASection;
